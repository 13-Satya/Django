"""HMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from oyo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('booking',views.booking, name='booking'),
    path('admin', admin.site.urls),
    path('customer_login',views.customer_login, name='customer_login'),
    path('customer',views.customer_login, name='customer_login'),
    path('customer_login/customer_home',views.customer_home, name='customer_home'),
    path('customer_login/customer_home/view_hotel',views.view_hotel, name='view_hotel'),
    path('customer_login/customer_home/view_hotel/booking',views.booking, name='booking'),
    path('customer_signup/customer_signup',views.customer_signup, name='customer_signup'),
    path('manager_login',views.manager_login, name="manager_login"),
    path('manager_login/manager',views.manager, name="manager"),
    path('manager_login/manager/search_cust',views.search_cust, name="search_cust"),
    path('manager_login/manager/all_booking',views.all_booking, name="all_booking"),
    path('manager_login/manager/all_employee',views.all_employee, name="all_employee"),
    path('manager_signup',views.manager_sign, name="manager_sign")
]
