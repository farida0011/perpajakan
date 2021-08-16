from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
	context = {
	'page_title':'website',
	}

	return render(request, 'index.html',  context)
