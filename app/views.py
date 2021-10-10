from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from app.models import Data


@login_required(login_url="/login/")
def dashboard(request):
    last_reading = Data.objects.last()
    last_readings = Data.objects.order_by('-id').all()[:30]
    context = {
        'segment': 'index',
        "temperature": last_reading.temperature if last_reading else None,
        "humidity": last_reading.humidity if last_reading else None,
        "last_readings": last_readings,
        "data_by_hour": Data.get_data_grouped_by_hour(),
        "data_by_minutes": Data.get_data_grouped_by_minutes(),
        "data_by_seconds": Data.get_data_grouped_by_seconds(),
    }

    html_template = loader.get_template('dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


# noinspection PyBroadException
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))
