from django.contrib import admin
from django.urls import path
from wordapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name="home"),
    path('countS/',views.count, name='count'),
    path('contact/',views.contact, name="contact"),
]
