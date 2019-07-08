from django.shortcuts import render
from .models import ImageContent

def grid_show(request):
	images = ImageContent.objects.all()
	return render(request,"grid_display.html",{"images":images})

def detail_show(request,image_id):
	image = ImageContent.objects.get(id=image_id)
	return render(request,'detail_view.html',{'image':image})

def index(request):
	images = ImageContent.objects.all()

	if request.method =="POST":
		print("REQUEST***********************")

	return render(request,"index.html",{"images":images})