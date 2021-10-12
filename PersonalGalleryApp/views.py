from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    images=Image.allimages()
    return render(request,'index.html',{"images":images})

def filter_by_location(request,value):
    context={'value_from_link':value}

    return render(request,'bylocation.html',{"context":context})

def search_category(request):
    if 'category' in request.GET and  request.GET["category"]:
        search_term=request.GET.get("category")
        searched_images=Image.search_image(search_term)
        message=f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
