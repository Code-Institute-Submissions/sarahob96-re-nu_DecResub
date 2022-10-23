from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

class StripeWebHook_handler:

    def __init__(self, request):
        self.request = request

     
    def _confirmation_email(self, order):
        customer_email = order.email
        subject = render_to_string(
            'checkout/emails/confirmation_subject.txt',
            {'order': order})
        body = render_to_string('checkout/emails/confirmation_body.txt',
                                {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )


    def event_handler(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
        
    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
       