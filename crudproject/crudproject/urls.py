
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('enroll/', include('enroll.urls')),
    path('admin/', admin.site.urls),
]
