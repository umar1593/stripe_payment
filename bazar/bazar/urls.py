from app.views import CancelView, SuccessView, buy_item, item_list, show_item
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name='item_list'),
    path('buy/<int:item_id>/', buy_item, name='buy'),
    path('item/<int:item_id>/', show_item, name='show_item'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
