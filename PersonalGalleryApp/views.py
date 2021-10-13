from django.http.response import Http404
from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def index(request):
    images=Image.allimages()
    locations=Location.alllocations()



    return render(request,'index.html',{"images":images, "locations":locations})

def filter_by_location(request,location):
    locations=Location.alllocations()
    
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

def singleimage(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})