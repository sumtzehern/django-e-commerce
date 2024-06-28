from django.shortcuts import get_object_or_404, render
from .models import Item

# Create your views here.
def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })