from django.shortcuts import render
from .models import Service
from apps.blog.models import HowItWorks


def service_view(request):
    services = Service.objects.all()
    step_by_step = HowItWorks.objects.all()
    context = {
        'obj': services,
        'hiw': step_by_step
    }
    return render(request, 'services.html', context)

