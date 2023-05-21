from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationFormKZ


def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_page)
    else:
        form = ApplicationForm()
    return render(request, 'iptv_landing/index.html', {'form': form})


def index_kz(request):
    if request.method == 'POST':
        form = ApplicationFormKZ(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_page_kz)
    else:
        form = ApplicationFormKZ()
    return render(request, 'iptv_landing/index_kz.html', {'form': form})


def success_page(request):
    return render(request, 'iptv_landing/success_page.html')


def success_page_kz(request):
    return render(request, 'iptv_landing/success_page_kz.html')
