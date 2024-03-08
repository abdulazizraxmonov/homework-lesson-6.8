from django.shortcuts import render

def weekdays_view(request, language):
    weekdays = {
        'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'ru': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
    }
    context = {
        'weekdays': weekdays.get(language),
    }
    return render(request, 'weekdays/weekdays.html', context)

def weekdays_table_view(request):
    weekdays = {
        'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'ru': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
    }
    context = {
        'weekdays': weekdays,
    }
    return render(request, 'weekdays/weekdays_table.html', context)