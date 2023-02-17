import stripe
from django.conf import settings
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Item
from .utils import get_page_obj

stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponseBadRequest("Invalid item ID")
    domain = "http://127.0.0.1:8000"
    transformedItems = [
        {
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.price * 100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }
    ]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=transformedItems,
        mode='payment',
        success_url=domain + '/success/',
        cancel_url=domain + '/cancel/',
    )
    return JsonResponse({'session_id': session.id})


def item_list(request):
    item_list = Item.objects.all()
    page_obj = get_page_obj(item_list, request.GET.get('page'))
    context = {'page_obj': page_obj, 'index': True}
    return render(request, 'index.html', context)


def show_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponseBadRequest("Invalid item ID")

    return render(request, 'item.html', {'item': item})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
