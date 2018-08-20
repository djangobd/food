from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages

from .models import Order


def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order number {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}, you can track you food \
                here {}'.format(order.first_name,
                                order.id,
                                'http://127.0.0.1:8000/account/dashboard/')
    mail_sent = send_mail(subject,
                          message,
                          settings.EMAIL_HOST_USER,
                          [order.email])
    return mail_sent
