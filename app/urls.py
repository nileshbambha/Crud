from django.urls import path
from .views import detail_view,delete_view,create_view,list_view,update_view
  
urlpatterns = [
    path('', list_view,name="list"),
    path('<id>/', detail_view,name="detail" ),
    path('<id>/update', update_view,name="update"),
    path('create', create_view,name="create"),
    path('<id>/delete', delete_view,name="delete" ), 
] 