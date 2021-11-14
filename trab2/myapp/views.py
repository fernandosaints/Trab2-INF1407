from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Player
from django.views.generic.base import View
from myapp.forms import PlayerModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.
def home(request):
  return render(request, 'myapp/home.html')

class PlayerListView(View):
 def get(self, request, *args, **kwargs):
  players = Player.objects.all()
  context = { 'players': players, }
  return render(
  request, 
  'myapp/playersList.html', 
  context)

class PlayerCreateView(View):
  def get(self, request, *args, **kwargs):
    context = { 'formulario': PlayerModel2Form, }
    return render(request, 
    "myapp/createPlayer.html", context)
 
  def post(self, request, *args, **kwargs):
    formulario = PlayerModel2Form(request.POST)
    if formulario.is_valid():
      player = formulario.save()
      player.save()
      return HttpResponseRedirect(reverse_lazy(
      "myapp:playersList"))



def segundaPagina(request):
 # processamento antes de mostrar
 # a segunda página
 return render(request, 'myapp/segunda.html')
