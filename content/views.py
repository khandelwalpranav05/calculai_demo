from django.shortcuts import render
from .models import ImageContent

def grid_show(request):
	if request.method =="POST":
		a = request.POST['dropdown']

	images = ImageContent.objects.filter(ethnicity = a)
	return render(request,"grid_display.html",{"images":images})

def detail_show(request,image_id):
	image = ImageContent.objects.get(id=image_id)
	return render(request,'detail_view.html',{'image':image})

def index(request):
	return render(request,"index.html")