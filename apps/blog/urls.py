from django.urls import path
from .views import home, blog_view, about_view, rent_view, blog_single

urlpatterns = [
    path('', home),
    path('blog/', blog_view),
    path('about/', about_view),
    path('rent/<int:pk>/', rent_view),
    path('detail/<int:pk>/', blog_single),
]