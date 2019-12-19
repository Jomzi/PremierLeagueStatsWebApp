from django.shortcuts import render, redirect
from premlgueapp.forms import OverviewForm
from premlgueapp.models import Overview

def emp(request):
    if request.method == "POST":
        form = OverviewForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = OverviewForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    overviews = Overview.objects.all()
    return render(request, "show.html", {'overviews': overviews})





