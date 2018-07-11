from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Deposit, Placebet
from .forms import DepositForm, PlacebetForm

# Create your views here.
