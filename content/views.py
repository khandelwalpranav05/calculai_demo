from django.shortcuts import render
from .models import ImageContent

# Create your views here.
def grid_show(request):
	images = ImageContent.objects.all()
	return render(request,"grid_display.html",{"images":images})

def detail_show(request,image_id):
	image = ImageContent.objects.get(id=image_id)
	# image = ImageContent.get_object().pk
	return render(request,'detail_view.html',{'image':image})