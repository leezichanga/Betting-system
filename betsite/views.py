from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Deposit, Placebet
from .forms import DepositForm, PlacebetForm
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def deposit(request):
    current_user = request.user
    mobile_number = Number.get_number()
    id_no = Id.get_id()
    amount = Amount.get_amount()
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = current_user
            deposit.save()
            return redirect('home')

@login_required(login_url='/accounts/login/')
def place_bet(request):
    current_user = request.user
    game_id = game.get_game()
    amount = Amount.get_amount()
    prediction = Prediction.get_prediction()
    if request.method == 'POST':
        form = PlacebetForm(request.POST)
        if form.is_valid():
            placebet = form.save(commit=False)
            placebet.user = current_user
            placebet.save()
            return redirect('home')

def view_balance(request):
    mobile_number = request.POST.get('mobile_number')
    email = request.POST.get(email)
    balance = request.POST.get(balance)

    recipient = View_BalanceRecipients(mobile_number=mobile_number, email=email, balance=balance)
    recipient.save()
    send_balance(name, email, balance)
    data = {'success': 'Your balance amount is'}
    return JsonResponse(data) 
