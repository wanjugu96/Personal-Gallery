from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
    images=Image.allimages()
    return render(request,'index.html',{"images":images})

def filter_by_location(request,location):
    return render(request,'index.html')

def search_category(request):
    if 'image' in request.GET and  request.GET["image"]:
        search_term=request.GET.get("image")
        searched_images=Image.search_image(search_term)
        message=f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
