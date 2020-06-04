from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

from django.shortcuts import get_list_or_404, render, redirect,get_object_or_404
from django.views.generic.detail import DetailView

from booking.models import Train, Ticket
from booking.forms import TicketForm
from booking.utils import class_name, update_count


def index(request):
    ''' Render index.html '''
    return render(request, 'index.html')


def search_results(request):
    ''' Display search results filter by queries '''
    trains = get_list_or_404(Train.objects.filter(
        date=request.GET.get('date'),
        route__source__name=request.GET.get('source'),
        route__destination__name=request.GET.get('destination'),
    ))
    context = {'trains': trains}
    return render(request, 'search.html', context)


def book_ticket(request):
    ''' Book Tikcet'''
    if request.method == 'GET':
        form = TicketForm()
        train = Train.objects.get(pk=request.GET.get('train'))
        seat_class = request.GET.get('class')
        train_context = {
            'train': train,
            'class_model_name': seat_class,
            'class': class_name(seat_class),
            'seat': getattr(train, seat_class)
        }
    elif request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            train = Train.objects.get(pk=request.POST.get('train'))
            form.instance.train = train
            instance = form.save()
            # update count
     
            update_count(train, request.POST.get('class'))
            return redirect('/')
    else:
        return redirect('/')

    return render(request, 'booking.html', {'form': form, 'train_context': train_context})


def get_ticket(request):  
    if request.method == 'POST':
        ticket = Ticket.objects.get(Ticket.objects.filter(
        pk=request.GET.get('user_name'),))
        return render(request, 'detail.html', {'detail':ticket})
    else:
        return render(request, 'ticket.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid info')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
    




