from django.urls import path
from .views import HomeView, ContactPageView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('contact/', ContactPageView.as_view(), name='contact_page')
]