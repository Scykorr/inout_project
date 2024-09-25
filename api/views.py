import json

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def trial(request):
    body = request.body.decode('utf-8')
    body = body.replace('\n', '')
    content = json.loads(body)
    response = requests.post(
        url='https://trials.inoutproject.ru/squid_tenants.json',
        json=content,
        headers={
            'Content-Type': 'application/json',
            'X-Redmine-API-Key': '15461da5477281f86c9699ab124cd6c31693d39f'
        }
    )

    return HttpResponse(
        content_type='application/json',
        content=response.json().get('autologin_url')
    )


@csrf_exempt
def crm(request):
    body = request.body.decode('utf-8')
    body = body.replace('\n', '')
    content = json.loads(body)
    response = requests.post(
        url='https://ip.inoutproject.ru/easy_leads.json?key=cfc9f757838e3013701e39fa28bd5c3a211ebd77',
        json=content,
        headers={
            'Content-Type': 'application/json',
            'X-Redmine-API-Key': 'cfc9f757838e3013701e39fa28bd5c3a211ebd77'
        }
    )

    return HttpResponse('Ok')
