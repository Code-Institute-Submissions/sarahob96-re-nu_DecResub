from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order_number


@receiver(post_save, sender=Order_number)
def update_order_on_save(sender, instance, created, **kwargs):

    instance.order.update_total_cost()


@receiver(post_delete, sender=Order_number)
def update_order_on_delete(sender, instance, **kwargs):

    instance.order.update_total_cost()
