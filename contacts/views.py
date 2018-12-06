from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST' and request.user.is_authenticated:
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        listing = request.POST['listing']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Проверка делали ли авторизованный пользователь запрос по дому

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Вы уже делали запрос по этому дому')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                      phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email

        send_mail(
            'Исходящий запрос с сайта BTRE: ' + listing,
            'Запрос по дому' + listing + '. Зайдите в панель администратора, чтобы узнать больше.'
            + 'Электронная почта клиента: ' + email + '. Контактный телефон: ' + phone,
            'krupin_anton@mail.ru',
            [realtor_email, 'krupin_anton@mail.ru', 'krupinanton87@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Ваш запрос был отправлен. Риэлтор скоро свяжется с вами')

        return redirect('/listings/'+listing_id)

    else:
        listing_id = request.POST['listing_id']
        messages.error(request, 'Зарегистрирутесь или авторизуйтесь, чтобы оставить запрос.')
        return redirect('/listings/'+listing_id)
