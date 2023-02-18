from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, null=True, blank=True
    )
    tax = models.ForeignKey(
        Tax, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        items_total = sum(item.price for item in self.items.all())
        discount_amount = self.discount.amount if self.discount else 0
        tax_amount = self.tax.amount if self.tax else 0
        return items_total - discount_amount + tax_amount
