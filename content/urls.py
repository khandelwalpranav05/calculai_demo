from django.urls import path
from content import views

urlpatterns = [
	path('',views.grid_show,name = 'display_all'),
	]
	 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)