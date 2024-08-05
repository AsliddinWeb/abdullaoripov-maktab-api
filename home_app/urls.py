from django.urls import path
from .views import (
    HomeWelcomeView,
    HomeAboutView,
    CounterView,
    HomeLeadersListView,
    HomeLeadersDetailView,
    HomePartnersListView
)

urlpatterns = [
    path('welcome/', HomeWelcomeView.as_view(), name='home-welcome'),
    path('about/', HomeAboutView.as_view(), name='home-about'),
    path('counter/', CounterView.as_view(), name='home-counter'),

    path('leaders/', HomeLeadersListView.as_view(), name='home-leaders-list'),
    path('leaders/<int:pk>/', HomeLeadersDetailView.as_view(), name='home-leaders-detail'),
    path('partners/', HomePartnersListView.as_view(), name='home-partners-list'),
]
