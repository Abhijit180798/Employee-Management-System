from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('user-login/', views.user_login, name='user_login'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),
]
