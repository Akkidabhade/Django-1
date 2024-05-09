from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .models import Product,CartItems

#sing your views here
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm



#signup or register form
def user_signup(request):
     if request.method=='POST' :
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login')
     else:
              form=SignupForm()
     return render(request,'signup.html',{'form' :form})
         

#login
def user_login(request):
     if request.method=='POST':
       form = LoginForm(request.POST)
       if form.is_valid():
          username=form.cleaned_data['username']
          password=form.cleaned_data['password']
          user = authenticate(request, username=username, password=password)
          if user:
               login(request, user)
               return redirect('list')
     else:
         form=LoginForm()
     return render(request, 'login.html',{'form':form})

#logout
def user_logout(request):
     logout(request)
     return redirect('login')
            

def home(request):
    # Fetch some example items from the database
    items = Item.objects.all()[:4]  # Assuming you want to display 4 items on the homepage
    context = {
        'items': items
    }
    return render(request, 'home.html', context)

def products(request):
    # Fetch all items from the database
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'products.html', context)

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render
from .models import Item

def search(request):
    return render(request, 'search.html')

def search(request):
    query = request.GET.get('query')
    if query:
        items = Item.objects.filter(name__icontains=query)
    else:
        items = None
    return render(request, 'search.html', {'items': items})

def product_list(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def view_cart(request):
    cart_items = CartItems.objects.filter(user=request.user)
    total_price = sum(item.product.price*item.quantity for item in cart_items)
    return render(request,'cart.html',{'cart_items':cart_items,'total_price':total_price})

def add_to_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart_item,created=CartItems.objects.get_or_create(product=product,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('view_cart')

def remove_from_cart(request,item_id):
    cart_item = CartItems.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
