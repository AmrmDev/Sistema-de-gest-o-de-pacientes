from django.shortcuts import render


def doctor_login_view(request):
    return render(request, 'doctors/logindoctor.html')