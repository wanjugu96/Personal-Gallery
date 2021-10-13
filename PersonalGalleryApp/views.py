from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def index(request):
    images=Image.allimages()
    locations=Location.alllocations()



    return render(request,'index.html',{"images":images, "locations":locations})

def filter_by_location(request,value):
    locations=Location.alllocations()
    if request.method=='GET':
        location = request.GET.get('location')
        if not location:
            return render(request, 'index.html')
        else:
            images=Image.filter_by_location(location)
            
            return render(request,'bylocation.html',{"images":images})

def search_category(request):
    if 'category' in request.GET and  request.GET["category"]:
        search_term=request.GET.get("category")
        searched_images=Image.search_image(search_term)
        message=f"{search_term}"
        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
