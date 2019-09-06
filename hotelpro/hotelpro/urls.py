from django.conf.urls import url
from django.contrib import admin
from hotelapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.homeview),
    url(r'confirm/',views.bookingconfirm),
    url(r'cancel/',views.cancelbooking)
]
