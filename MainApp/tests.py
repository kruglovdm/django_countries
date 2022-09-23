from django.test import TestCase

from django.shortcuts import render
from django.http import Http404
import string
from django.core.paginator import Paginator

from MainApp.models import Country, LanguagesCountries

def languages_page(request):
    items = list(x['languages'] for x in countries)
    items = sorted(list(set(j for i in items for j in i)))

    context = {
        'items': items,
        'alphabet': alphabet
    }
    return render(request, 'languages.html', context)


def test():

    itemsSQL = LanguagesCountries.obects.raw("SQL * FROM myapp_languagescountries")

    a = 1