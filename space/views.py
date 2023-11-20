from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


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


def signIn(request):
    if request.method == 'GET':
        return render(request=request, template_name='sign_in.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('about_us_url')
        context = {
            'error': 'Не верный логин и/или пароль',
            'email': email
        }
        return render(request=request, template_name='sign_in.html', context=context)


def signOut(request):
    logout(request)
    return redirect('about_us_url')


def signUp(request):
    if request.method == 'GET':
        return render(request=request, template_name='sign_up.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birth_date = request.POST.get('birth_date')
        age = request.POST.get('age')
        custom = CustomUser(email=email, password=password, name=name, surname=surname, birth_date=birth_date, age=age)
        custom.set_password(password)
        custom.save()
        return redirect('sign_in_url')




