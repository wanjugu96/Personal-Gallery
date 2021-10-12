from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def filter_by_location(request,location):
    return render(request,'index.html')

def search_by_category(request,category):
    pass