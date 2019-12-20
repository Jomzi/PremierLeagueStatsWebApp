from django.shortcuts import render, redirect
from plyrstats.forms import PlayerForm
from plyrstats.models import Player

def emp(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('player/show')
            except:
                pass
    else:
        form = PlayerForm()
    return render(request, 'player/index.html', {'form': form})


def show(request):
    players = Player.objects.all()
    return render(request, "player/show.html", {'players': players})


def edit(request, id):
    player = Player.objects.get(id=id)
    return render(request, 'player/edit.html', {'player': player})


def update(request, id):
    player = Player.objects.get(id=id)
    form = PlayerForm(request.POST, instance=player)
    if form.is_valid():
        form.save()
        return redirect("player/show")
    return render(request, 'player/edit.html', {'player': player})




