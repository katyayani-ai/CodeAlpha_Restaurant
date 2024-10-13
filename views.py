from django.shortcuts import render, redirect
from .models import MenuItem, Reservation

def home(request):
    return render(request, 'restaurant/home.html')

def menu_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

def reserve_table(request):
    if request.method == "POST":
        # Handle reservation logic
        # Assuming your model has been set correctly to save the data
        customer_name = request.POST['customer_name']
        reservation_date = request.POST['reservation_date']
        table_number = request.POST['table_number']
        Reservation.objects.create(customer_name=customer_name, reservation_date=reservation_date, table_number=table_number)
        return redirect('home')  # Redirect to home after reservation
    return render(request, 'restaurant/reserve.html')
