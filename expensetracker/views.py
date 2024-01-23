from django.shortcuts import render
from django.http import HttpResponse

from .models import Expense

def index(request):
   allProductsList = Expense.objects.order_by("-purchaseDate")
   output = {"allProductsList": allProductsList}

   return render(request, "expensetracker/index.html", output)