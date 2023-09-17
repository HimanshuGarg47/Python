from django.shortcuts import render
from .scrape import scraping
from django.http import HttpResponse

# Create your views here.
def index(request): 
    scraping()
    return HttpResponse("updated!")
