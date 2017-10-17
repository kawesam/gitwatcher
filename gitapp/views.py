# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse("Hellow world")

def test(request):
    return HttpResponse("It works")

def profile(request):
    parsedData = []
    if request.method == "POST" :
        username = request.POST.get('user')
        jsonlist=[]
        req = requests.get('https://api.github.com/users/' + username)
        jsonlist.append(json.loads(req.content))
        userData = {}
        for data in jsonlist:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers']  = data['followers']
            userData['following']  = data['following']

        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})
