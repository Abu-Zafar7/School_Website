from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage),
    path('homepage/',views.homepage,name='homepage'),
    path('about/',views.about,name='about'),
    path('academics/',views.academics,name='academics'),
    path('contact/',views.contact,name='contact')
]