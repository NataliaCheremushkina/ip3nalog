from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import FeedbackForm


def landing(request):
    return render(request, 'landing/block/block.html')


def send_feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        subject = f'Новая заявка на сайте ip3nalog.ru.'
        message = f'Привет! На сайте https://ip3nalog.ru/ оставили новую заявку.\n\n' \
                    f'Контактные данные пользователя: \n\n' \
                    f'Имя: {cd["name"]} \n\n' \
                    f'Email: {cd["email"]} \n\n'
        send_mail(subject, message, 'admin@admin.com', ['admin@admin.com'])
    return redirect('landing:landing')
