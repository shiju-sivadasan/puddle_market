from django.shortcuts import render,redirect
from django.http import HttpResponse
from items.models import Item,Category
from .forms import SignUpForm,LoginForm
# Create your views here.
def index(request):
    item = Item.objects.filter(is_sold=True)[0:6]
    category = Category.objects.all()
    return render(request,'index.html',{'categories' : category , 'items' : item})
def base(request):
    return render(request,'base.html')
def contact(request):
    return render(request,'contact.html')
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print(form.errors)  # This will show any validation errors
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})
def login(request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})