from django.urls import path
from .views import (
    NavTypeListView,
    NavTypeDetailView,
    OneNavbarListView,
    OneNavbarDetailView,
    TwoNavbarListView,
    TwoNavbarDetailView,
    ThreeNavbarListView,
    ThreeNavbarDetailView
)

urlpatterns = [
    # NavType URLs
    path('nav-types/', NavTypeListView.as_view(), name='navtype-list'),
    path('nav-types/<int:pk>/', NavTypeDetailView.as_view(), name='navtype-detail'),

    # OneNavbar URLs
    path('one-navbars/', OneNavbarListView.as_view(), name='onenavbar-list'),
    path('one-navbars/<int:pk>/', OneNavbarDetailView.as_view(), name='onenavbar-detail'),

    # TwoNavbar URLs
    path('two-navbars/', TwoNavbarListView.as_view(), name='twonavbar-list'),
    path('two-navbars/<int:pk>/', TwoNavbarDetailView.as_view(), name='twonavbar-detail'),

    # ThreeNavbar URLs
    path('three-navbars/', ThreeNavbarListView.as_view(), name='threenavbar-list'),
    path('three-navbars/<int:pk>/', ThreeNavbarDetailView.as_view(), name='threenavbar-detail'),
]
