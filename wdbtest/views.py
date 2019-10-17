# -*- coding: utf-8 -*-
from django.http import HttpResponse


def my_view(request):

    array = []
    for i in range(10):
        array.append(i)
        if i % 2:
            a = i / 0  # fail here

    return HttpResponse("ok")
