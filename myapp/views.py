from django.shortcuts import render, get_object_or_404
from .models import Item
from django.urls import reverse

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

    return render(request, 'qr_display.html', {'items': qr_items})
