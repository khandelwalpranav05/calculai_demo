from django.urls import path
from content import views

app_name = 'content'

urlpatterns = [
		path('all/',views.grid_show,name = 'display_all'),
		path('',views.index,name = 'index'),
		path('detail/<image_id>/',views.detail_show,name = 'detail_image'),
	]