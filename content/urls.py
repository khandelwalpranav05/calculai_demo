from django.urls import path
from content import views

app_name = 'content'

urlpatterns = [
	path('',views.grid_show,name = 'display_all'),
	path('<image_id>/detail/',views.detail_show,name = 'detail_image'),
	]
	 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)