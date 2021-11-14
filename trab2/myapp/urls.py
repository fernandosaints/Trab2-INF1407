from django.urls.conf import path
from myapp import views
app_name = "myapp"
urlpatterns = [
  path('create/', views.PlayerCreateView.as_view(), 
 name='createPlayer'),
 path('list/', views.PlayerListView.as_view(), 
 name='playersList'),
 path('', views.PlayerListView.as_view(), 
 name='home'),
 ]