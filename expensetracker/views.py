from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Expense

def index(request):
   allProductsList = Expense.objects.order_by("-purchaseDate")
   output = {"allProductsList": allProductsList}
   # print(request.user)
   # print(request.GET.get('thrash-17'))
   data = {
      'req_method': request.method,
      # 'req_header': request.headers,
      'req_body': request.body,
      'get_params': request.GET,
      # 'post_params': request.POST,
      # 'delete_params': request.DELETE,
      # 'cookies': request.COOKIES,
      'user': request.user,
   }
   print(data)

   return render(request, "expensetracker/index.html", output)

def delete_entry(request, thrash_id):
   if request.method == 'DELETE':
      try:
         entry = Expense.objects.get(pk=thrash_id)
         entry.delete();
         data = {'message': 'Entry deleted succesfully!'}
         return JsonResponse(data)
      except Expense.DoesNotExist:
         data = {'message': 'Delete failed!'}
         return JsonResponse(data)
   else:
      return JsonResponse({'error': 'Method not allowed!'}, status=405)