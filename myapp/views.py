from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import Player
from django.views.generic.base import View
from myapp.forms import PlayerModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')


class PlayerListView(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.filter(creator=str(request.user))
        context = {'players': players, }
        return render(
            request,
            'myapp/playersList.html',
            context)


class PlayerCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {'formulario': PlayerModel2Form, }
        return render(request,
                      "myapp/createPlayer.html", context)

    def post(self, request, *args, **kwargs):
        formulario = PlayerModel2Form(request.POST)
        if formulario.is_valid():
            player = formulario.save()
            player.creator = str(request.user)
            player.save()
            return HttpResponseRedirect(reverse_lazy(
                "myapp:playersList"))

def checkPlayersCountDatabase(request):
  response = {
    'playersCount':
      len(Player.objects.all())
      }
  return JsonResponse(response)


class PlayerUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        player = Player.objects.get(id=pk)
        formulario = PlayerModel2Form(instance=player)
        context = {'player': formulario, }
        return render(request, 'myapp/updatePlayer.html', context)

    def post(self, request, pk, *args, **kwargs):
        player = get_object_or_404(Player, id=pk)
        formulario = PlayerModel2Form(request.POST, instance=player)
        if formulario.is_valid():
            player = formulario.save()
            player.save()
            return HttpResponseRedirect(reverse_lazy("myapp:playersList"))
        else:
            context = {'player': formulario, }
            return render(request, 'myapp/updatePlayer.html', context)


class PlayerDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        player = Player.objects.get(pk=pk)
        context = {'player': player, }
        return render(
            request, 'myapp/deletePlayer.html',
            context)

    def post(self, request, pk, *args, **kwargs):
        player = Player.objects.get(pk=pk)
        player.delete()
        print("Deleting player...", pk)
        return HttpResponseRedirect(
            reverse_lazy("myapp:playersList"))


def segundaPagina(request):
    # processamento antes de mostrar
    # a segunda p??gina
    return render(request, 'myapp/segunda.html')


def index(request):
    return render(request, "index.html")


def register_new_account(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            context = {
                'form': form
            }
            return render(request, 'register.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
