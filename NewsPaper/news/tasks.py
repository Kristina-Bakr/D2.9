from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from NewsPaper.settings import SITE_URL


@shared_task
def send_new_mail(username, email, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуй, {username}. Новая статья в твоём разделе!',
        from_email='DEFF_EMAIL',
        to=[email]
    )

    msg.attach_alternative(html_content, 'text/html')

    msg.send()


@shared_task
def send_send(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'Link': f'{SITE_URL}/news/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='DEFF_EMAIL',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()