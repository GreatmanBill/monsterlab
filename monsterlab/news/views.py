# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def index(request):
	context = {}
	return render(request, 'news/index.html', context)
