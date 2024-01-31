from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('expensetracker/', include('expensetracker.urls')),
    path('admin/', admin.site.urls),
]
