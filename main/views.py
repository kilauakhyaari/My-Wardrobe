from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from django.core import serializers
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    last_login = request.COOKIES.get('last_login', 'Not available')

    context = {
        'app': 'My Wardrobe',
        'name': request.user.username,
        'items': items,
        'last_login': last_login,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Format current date and time
            now = timezone.localtime(timezone.now())
            formatted_date = now.strftime("%B %-d, %Y")
            formatted_time = now.strftime("%H:%M")
            last_login_str = f"{formatted_date} at {formatted_time}"

            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', last_login_str)
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def increase_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    item.amount += 1
    item.save()
    return JsonResponse({'amount': item.amount})

def decrease_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    if item.amount > 0:  
        item.amount -= 1
        item.save()
    return JsonResponse({'amount': item.amount})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_item(request, id):
    item = Item.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_item.html", context)

def get_item_json(request):
    if not request.user.is_authenticated:
        return JsonResponse([], safe=False) 

    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        in_laundry = request.POST.get("in_laundry") == "on"
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, in_laundry=in_laundry, user=user)
        new_item.save()

        data = {
            'id': new_item.pk,
            'name': new_item.name,
            'amount': new_item.amount,
            'description': new_item.description,
            'in_laundry': new_item.in_laundry
        }
        return JsonResponse(data)

    return HttpResponseNotFound()
