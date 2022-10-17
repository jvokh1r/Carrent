from django.db.models import Q
from django.shortcuts import render

from .models import Cars
from apps.blog.models import HowItWorks


def cars_view(request):
    sd = request.POST.get('sd')
    ed = request.POST.get('ed')
    from_ = request.POST.get('from_')
    to_ = request.POST.get('to_')
    free_cars = Cars.objects.filter(~Q(books__go_date__range=[sd, ed]) or ~Q(books__back_date__range=[sd, ed]))
    print(sd)
    print(ed)
    print(from_)
    print(to_)
    print(free_cars)
    step_by_step = HowItWorks.objects.all()
    context = {
        'obj': free_cars,
        'hiw': step_by_step,
        'sd': sd,
        'ed': ed,
        'from_': from_,
        'to_': to_
    }
    return render(request, 'cars.html', context)




