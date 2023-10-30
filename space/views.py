from django.shortcuts import render, redirect
from .models import *


def RocketListView(request):
    stages = request.GET.get('stages')
    if stages is not None:
        rockets_all = Rocket.objects.filter(stages=stages)
    else:
        rockets_all = Rocket.objects.all()
    context = {
        'rockets': rockets_all
    }
    return render(request=request, template_name='rocket_list_template.html', context=context)


def RocketDetailView(request, rocket_id):
    rocket = Rocket.objects.get(id=rocket_id)
    context = {
        'rocket': rocket
    }
    return render(request=request, template_name='rocket_detail_template.html', context=context)


def RocketCreateView(request):
    if request.method == 'GET':
        return render(request=request, template_name='rocket_create_template.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        type = request.POST.get('type')
        fuel_condition = request.POST.get('fuel_condition')
        stages = request.POST.get('stages')
        image = request.FILES.get('image')
        rocket = Rocket(title=title, type=type, fuel_condition=fuel_condition, stages=stages, image=image)
        rocket.save()
        return redirect('rocket_list_url')


def RocketUpdateView(request, rocket_id):
    rocket = Rocket.objects.get(id=rocket_id)
    if request.method == 'GET':
        context = {
            'rocket': rocket
        }
        return render(request=request, template_name='rocket_update_template.html', context=context)
    elif request.method == 'POST':
        rocket.title = request.POST.get('title')
        rocket.type = request.POST.get('type')
        rocket.fuel_condition = request.POST.get('fuel_condition')
        rocket.stages = request.POST.get('stages')
        if 'image' in request.FILES:
            rocket.image = request.FILES.get('image')
        rocket.save()
        return redirect('rocket_detail_url', rocket_id)


def RocketDeleteView(request, rocket_id):
    rocket = Rocket.objects.get(id=rocket_id)
    if request.method == 'GET':
        context = {
            'rocket': rocket
        }
        return render(request=request, template_name='rocket_delete_template.html', context=context)
    if request.method == 'POST':
        rocket.delete()
    return redirect('rocket_list_url')

