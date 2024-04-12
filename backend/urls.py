from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/manager/' , include("api.v1.manager.urls")),
    path('api/v1/auth/' , include("api.v1.auth.urls")),
]
