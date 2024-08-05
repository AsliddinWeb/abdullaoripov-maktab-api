from django.urls import path
from .views import (
    SeoSettingsLastView,
    HeaderSettingsLastView,
    FooterSettingsLastView,
    SocialSettingsLastView,
    MoreTitlesLastView,
    ErrorTextsLastView,
    FooterLinkCategoryListView,
    FooterLinkListView
)

urlpatterns = [
    # Last
    path('seo-settings/', SeoSettingsLastView.as_view(), name='seo-settings-last'),
    path('header-settings/', HeaderSettingsLastView.as_view(), name='header-settings-last'),
    path('footer-settings/', FooterSettingsLastView.as_view(), name='footer-settings-last'),
    path('more-titles/', MoreTitlesLastView.as_view(), name='more-titles-last'),
    path('error-texts/', ErrorTextsLastView.as_view(), name='error-texts-last'),

    # All
    path('social-networks/', SocialSettingsLastView.as_view(), name='social-settings-list'),
    path('footer-link-categories/', FooterLinkCategoryListView.as_view(), name='footer-link-categories-list'),
    path('footer-links/', FooterLinkListView.as_view(), name='footer-links-list'),
]
