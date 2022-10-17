from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, About, Team, History, HowItWorks, Category
from apps.services.models import Service
from apps.cars.models import Cars
from apps.cars.forms import BookForm, Book
from apps.feedback.models import FeedBack
from apps.comment.forms import CommentForm
from django.http import Http404


def home(request):
    cars = Cars.objects.all().order_by('-id')[:1]
    cars_single = Cars.objects.all()
    blog = Article.objects.all().order_by('-id')[:3]
    objects = Service.objects.all()
    step_by_step = HowItWorks.objects.all()
    back = FeedBack.objects.all().order_by('-id')[:3]
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        sd = request.POST.get('sd')
        ed = request.POST.get('ed')
        free_cars = Cars.objects.filter(~Q(books__go_date__range=[sd, ed]) or ~Q(books__back_date__range=[sd, ed]))
        print(sd)
        print(ed)
        print(free_cars)

    count = Cars.objects.all().count()
    # if form.is_valid():
    #    form.save()
    #     return redirect('/')
    context = {
        'post': blog,
        'service': objects,
        'item': cars,
        'item_2': cars_single,
        'hiw': step_by_step,
        'form': form,
        'count': count,
        'feed': back,
    }
    return render(request, 'index.html', context)


def rent_view(request, pk):
    sd = request.GET.get('sd')
    ed = request.GET.get('ed')
    from_ = request.GET.get('from_')
    to_ = request.GET.get('to_')
    print(sd)
    print(ed)
    print(from_)
    print(to_)
    if request.method == 'POST':
        Book.objects.create(
            car_id=pk,
            where_from=from_,
            where_to=to_,
            go_date=sd,
            back_date=ed
        )
    car = request.GET.get('car')
    obj = Cars.objects.get(id=pk)
    if car:
        objs = obj.filter(name__icontains=car)
        return objs
    context = {
        'obj': obj,
    }
    return render(request, 'rent.html', context)


def blog_view(request):
    blog = Article.objects.all()
    step_by_step = HowItWorks.objects.all()
    page_number = request.GET.get('page')
    p = Paginator(blog, 1)
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'post': blog,
        'obj': step_by_step,
        'page': page_obj
    }
    return render(request, 'blog.html', context)


def about_view(request):
    about = About.objects.all()
    team = Team.objects.all()
    history = History.objects.all()
    step_by_step = HowItWorks.objects.all()
    for i in team:
        print(i.role)
    context = {
        'abouts': about,
        'hist': history,
        'people': team,
        'obj': step_by_step
    }
    return render(request, 'about.html', context)


def blog_single(request, pk=None):
    # if pk is not None:
    post = Article.objects.get(id=pk)
    categories = Category.objects.all().order_by('-id')
    user = request.user
    author = user.profile
    form = CommentForm()
    cat = request.GET.get('category')
    if cat:
        post = post.filter(title__icontains=cat)
        return post
    if request.method == "POST":
        if user.is_authenticated:
            form = CommentForm(request.POST, request.FILES)
            if form.is_valid():
                com = form.save(commit=False)
                com.post = post
                com.author = author
                com.save()
                return redirect('/')
        # some error
        return Http404
    context = {
        'article': post,
        'categories': categories,
        'form': form
    }
    return render(request, 'single.html', context)
