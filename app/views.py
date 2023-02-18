import stripe
from django.conf import settings
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import Item, Order
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
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item.html', {'item': item})


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
        'total': order.total,
    }
    return render(request, 'order_detail.html', context)


@csrf_exempt
def pay_for_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=int(order.total * 100),
        currency='usd',
        metadata={'order_id': order.pk},
    )
    order.stripe_payment_intent_id = intent.id
    order.save()

    return JsonResponse({'client_secret': intent.client_secret})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"
