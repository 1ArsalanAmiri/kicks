from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem


def update_order_total(order):
    total = sum(item.get_total() for item in order.items.all())
    order.total_price = total
    order.save(update_fields=["total_price"])


@receiver(post_save, sender=OrderItem)
def update_order_total_on_save(sender, instance, **kwargs):
    update_order_total(instance.order)


@receiver(post_delete, sender=OrderItem)
def update_order_total_on_delete(sender, instance, **kwargs):
    update_order_total(instance.order)