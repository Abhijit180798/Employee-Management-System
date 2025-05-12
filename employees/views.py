from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            position=request.POST['position'],
            department=request.POST['department']
        )
        return redirect('index')
    return render(request, 'add.html')

def edit_employee(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        emp.name = request.POST['name']
        emp.position = request.POST['position']
        emp.department = request.POST['department']
        emp.save()
        return redirect('index')
    return render(request, 'edit.html', {'employee': emp})

def delete_employee(request, emp_id):
    emp = get_object_or_404(Employee, id=emp_id)
    emp.delete()
    return redirect('index')
def home(request):
    return render(request, 'home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def user_login(request):
    return render(request, 'user_login.html')