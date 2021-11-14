from django.urls.conf import path
from myapp import views
app_name = "myapp"
urlpatterns = [
  path('create/', views.PlayerCreateView.as_view(), name='createPlayer'),
  path('update/<int:pk>/', views.PlayerUpdateView.as_view(), name='updatePlayer'), 
  path('list/', views.PlayerListView.as_view(), name='playersList'),
  path('delete/<int:pk>/', views.PlayerDeleteView.as_view(), name='deletePlayer'),
  path('', views.PlayerListView.as_view(), name='home'),
 ]