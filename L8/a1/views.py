from django.shortcuts import render, redirect
from .forms import BillForm

# Fixed prices
PRICES = {
    'hp_mobile': 30000,
    'hp_laptop': 50000,
    'nokia_mobile': 15000,
    'nokia_laptop': 0,
    'samsung_mobile': 25000,
    'samsung_laptop': 45000,
    'motorola_mobile': 20000,
    'motorola_laptop': 0,
    'apple_mobile': 70000,
    'apple_laptop': 100000,
}

def bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            devices = form.cleaned_data['devices']
            quantity = form.cleaned_data['quantity']
            
            request.session['brand'] = brand
            request.session['devices'] = devices
            request.session['quantity'] = quantity
            
            return redirect('a1:result')
    else:
        form = BillForm()
    
    return render(request, 'a1/bill.html', {'form': form})

def result(request):
    brand = request.session.get('brand', 'hp')
    devices = request.session.get('devices', [])
    quantity = request.session.get('quantity', 1)
    
    items = []
    total_amount = 0
    
    for device in devices:
        key = f"{brand}_{device}"
        price = PRICES.get(key, 0)
        if price > 0:
            item_total = price * quantity
            items.append({
                'brand': brand.capitalize(),
                'device': device.capitalize(),
                'price': price,
                'quantity': quantity,
                'total': item_total
            })
            total_amount += item_total
    
    return render(request, 'a1/result.html', {
        'items': items,
        'total_amount': total_amount
    })
