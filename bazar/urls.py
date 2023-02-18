from django.contrib import admin
from django.urls import path

from app.views import (
    CancelView,
    SuccessView,
    buy_item,
    item_list,
    order_detail,
    pay_for_order,
    show_item,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('buy/<int:item_id>/', buy_item, name='buy'),
    path('item/<int:item_id>/', show_item, name='show_item'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
    path('order/<int:order_id>/pay/', pay_for_order, name='pay_for_order'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
