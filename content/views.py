from django.shortcuts import render
from .models import ImageContent

# Create your views here.
def grid_show(request):
	images = ImageContent.objects.all()
	return render(request,"grid_display.html",{"images":images})