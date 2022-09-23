from django.shortcuts import render
from django.http import Http404
import string
from django.core.paginator import Paginator
from MainApp.models import Country, LanguagesCountries
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def main_page(request):
    context = {
        'h': 'Home',
    }
    return render(request, 'index.html', context)


def countries_page(request):
    sample = Country.objects.all()

    paginator = Paginator(sample, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'h': 'countries',
        'page_obj': page_obj,
        'header': "Список стран",
        'alphabet': string.ascii_uppercase
    }
    return render(request, 'countries.html', context)


def languages_page(request):
    # Теоретически вставлять сырые SQL допустимо, но стоит этого избегать, если есть готовое решение в ORM:
    # https://docs.djangoproject.com/en/dev/ref/models/querysets/#distinct
    sample = LanguagesCountries.objects.raw("SELECT * FROM MainApp_languagescountries DIFFIRENT")

    context = {
        'h': 'languages',
        'page_obj': sample,
        'alphabet': string.ascii_uppercase
    }
    return render(request, 'languages.html', context)


def country_page(request, country_param):
    # Тут нужно добавить обработку исключения(DoesNotExist), если страна с именем country_param не существует в БД
    res_country = Country.objects.get(name=country_param)
    res_languagescountries = LanguagesCountries.objects.filter(country=res_country)

    context = {
        'h': 'country',
        'country': res_country.name,
        'languages': res_languagescountries,
    }
    return render(request, 'country.html', context)


def countries_letter_page(request, letter_country_param):
    sample = Country.objects.filter(name__startswith=letter_country_param)

    paginator = Paginator(sample, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'h': 'letter',
        'h2': 'Страны на букву '+letter_country_param,
        'page_obj': page_obj,
        'header': f"Список стран на букву {letter_country_param}",
        'alphabet': string.ascii_uppercase,
    }
    return render(request, 'countries.html', context)

def countries_language_page(request, language_country_param):
    items = LanguagesCountries.objects.filter(languages=language_country_param)
    items_page = []
    for el in items:
        items_page.append(el.country)

    paginator = Paginator(items_page, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'h': 'countries_language',
        'h2': 'Страны, в которых говорят на ' + language_country_param,
        'page_obj': page_obj,
        'header': f"Список стран с языком {language_country_param}",
    }
    return render(request, 'countries.html', context)

