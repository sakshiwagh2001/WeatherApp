"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]




# C:\Users\saksh\Desktop\Weather App\weather_project\weather_project\urls.py

from django.contrib import admin
from django.urls import path, include
from weather_data.views import weather_table_view  # import your view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather_data.urls')),  # Only API routes under /api/
    path('', weather_table_view, name='home'),   # 👈 ADD this line for home '/'

]