from django.shortcuts import render
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):

