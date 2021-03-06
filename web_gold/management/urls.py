from django.urls import path
from .views import *

urlpatterns = [
    # Authenticate
    path('login/', my_login, name='login'),
    path('logout/', my_logout, name='logout'),
    # Customer 
    path('customers', customers, name='customers'),
    path('add_customer', add_customer, name='add_customer'),
    path('edit_customer/<int:cus_id>', edit_customer, name='edit_customer'),
    path('view_customer/<int:cus_id>', view_customer, name='view_customer'),
    path('delete_customer/<int:cus_id>', delete_customer, name='delete_customer'),
    # Pledging
    path('', pledging, name='pledging'),
    path('add_pledging/<int:customer_id>', add_pledging, name='add_pledging'),
    path('view_pledging/<int:pled_id>', view_pledging, name='view_pledging'),
    path('delete_pledging/<int:pled_id>', delete_pledging, name='delete_pledging'),
    path('edit_pledging/<int:pled_id>', edit_pledging, name='edit_pledging'),
    #Log
    path('log', log, name='log'),
    # Other
    path('delete_gold/<int:gold_id>',delete_gold, name='delete_gold'),
    path('edit_admin/<int:admin_id>', edit_admin, name='edit_admin'),
    # APIs
    path('pledging_api', pledging_api, name='pledging_api'),
    path('customers_api', customers_api, name='customers_api'),
    path('log_api', log_api, name='log_api'),
]
