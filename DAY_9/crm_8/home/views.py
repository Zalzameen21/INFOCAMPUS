from django.shortcuts import render

def index(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')


def customer_list(request):
    customers = [
        {"name": "Amit", "email": "amit@gmail.com", "status": "Lead"},
        {"name": "Priya", "email": "priya@gmail.com", "status": "Customer"},
        {"name": "Rahul", "email": "rahul@gmail.com", "status": "Client"},
    ]

    return render(request, 'customers.html', {"customers": customers})