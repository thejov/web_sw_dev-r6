from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import simplejson as json

from models import Continent, Country

def continent_json(request, continent_code):
    """ Write your answer in 6.2 here. """
    continent = get_object_or_404(Continent, code = continent_code)
    countries = Country.objects.all()
    cont_countries = {}
    for country in countries:
        if country.continent.code == continent_code:
            cont_countries[country.code] = country.name

    json_dump = json.dumps(cont_countries, sort_keys=True, indent=2 * ' ')

    if request.GET.has_key("callback"):
        callback = request.GET.get("callback")
        json_dump = '%s(%s)' % (callback, json_dump)

    return HttpResponse(json_dump, mimetype='application/json; charset=utf-8')

def country_json(request, continent_code, country_code):
    """ Write your answer in 6.2 here. """
    country = get_object_or_404(Country, code = country_code)
    if country.continent.code != continent_code:
        raise Http404
    json_dump = json.dumps({"area" : country.area, "population" : country.population, "capital" : country.capital}, sort_keys=True, indent=2 * ' ')

    if request.GET.has_key("callback"):
        callback = request.GET.get("callback")
        json_dump = '%s(%s)' % (callback, json_dump)

    return HttpResponse(json_dump, mimetype='application/json; charset=utf-8')


def show_continent(request, continent_code=None):
    context = {"all_continents": Continent.objects.all()}
    if continent_code:
        continent = get_object_or_404(Continent, code=continent_code)
        context["continent"] = continent

        # Add your answer in 6.3 here
        countries = Country.objects.all()
        cont_countries = []
        for country in countries:
            if country.continent.code == continent_code:
                cont_countries.append(country)
        context["countries"] = cont_countries

    if request.is_ajax():
        return render_to_response("countrydata/countrytable.html", context)
    else:
        return render_to_response("countrydata/index.html", context)

def render_javascript(request):
    """ NOTE: This is a really bad way of serving a static file!
        It is only used in this exercise to serve this single JS file easily. """
    return render_to_response("countrydata/ajax_ui.js", mimetype="text/javascript")