from django.contrib import admin
from django.urls import path

from app.views import CancelView, SuccessView, buy_item, show_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', buy_item, name='buy'),
    path('item/<int:item_id>/', show_item),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
]
