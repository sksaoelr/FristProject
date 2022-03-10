from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

# http://localhost/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', RedirectView.as_view(url="/home/", permanent=True)),
    path('user/', include('user.urls')),
]
