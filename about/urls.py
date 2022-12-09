from django.urls import path
from .views import AboutPage

urlpatterns = {
    path('',AboutPage.as_view(),name='about')
}