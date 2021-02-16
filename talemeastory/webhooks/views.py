import os
import hashlib
import hmac
import subprocess

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.
from rest_framework.response import Response
from rest_framework import status


@api_view(['post'])
@parser_classes((JSONParser,))
def pull_request(request):
    github_pr_key = settings.GITHUB_PR_SECRET_KEY
    if github_pr_key is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    github_pr_key = str.encode(github_pr_key)
    digest = hmac.HMAC(github_pr_key, request.stream.body, 'sha256')
    digest_output = 'sha256=' + digest.hexdigest()
    if hmac.compare_digest(digest_output, request.stream.headers['X-Hub-Signature-256']):
        if request.data['action'] == 'closed' and request.data['pull_request']['merged']:
            subprocess.run(["git", "pull"])
            subprocess.run(["sudo", "systemctl", "restart", "talemeastory"])
            return Response()
    return Response('Nothing to do. Webhook done. Bye.')
