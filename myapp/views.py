from django.shortcuts import render, get_object_or_404
from .models import Item,WeatherSettings
from django.urls import reverse
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'qr_detail.html', {'item': item})

def show_qr(request):
    items = Item.objects.all()
    qr_items = []

    for item in items:
        item_url = request.build_absolute_uri(reverse('item_detail', args=[item.id]))
        print(item_url)
        qr_url = f"https://quickchart.io/qr?text={item_url}"
        qr_items.append({"name": item.name, "qr_url": qr_url})

        settings = WeatherSettings.objects.first()
    city = settings.city if settings else "Mysuru"

    api_key = "e1df2f4794f96139e687cac6f1eddd5f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
    }

    return render(request, 'qr_display.html', {'items': qr_items, 'weather': weather})



def search_product(request):
    product_name =add_product(request)  # Default: "nutella"
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&search_simple=1&action=process&json=1"

    response = requests.get(url)
    data = response.json()

    products = data.get("products", [])
    results = []
    for product in products:
        results.append({
            "product_name": product.get("product_name"),
            "brands": product.get("brands"),
            "code": product.get("code"),
            "image": product.get("image_front_url"),
            "description": product.get("allergens_from_ingredients"),
        })

    if results:
        item = results[0]
    else:
        item = {"product_name": "Not Found", "description": "N/A"}

    return render(request, 'qr_detail.html', {
        'item': item  
    })


@csrf_exempt
@require_POST
def add_product(request):
    data = json.loads(request.body)

    name = data.get("product_name")
    brand = data.get("brands")
    image = data.get("image")
    code = data.get("code")
    

    # no dupli
    item, created = Item.objects.get_or_create(
        code=code,
        defaults={
            "name": name,
            "brand": brand,
            "image": image,
        }
    )

    return JsonResponse({
        "success": True,
        "message": "Item added" if created else "Item already exists",
        "item_id": item.id
    })
