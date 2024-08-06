from django.urls import path

from .views import SchoolInfoView, SchoolLeadersListView, TeachersListView, EducationSystemView, GalleryListView, ApplyInfoView

urlpatterns = [
    path('info/', SchoolInfoView.as_view(), name='school-info'),
    path('leaders/', SchoolLeadersListView.as_view(), name='school-leaders'),
    path('teachers/', TeachersListView.as_view(), name='school-teachers'),
    path('education-system/', EducationSystemView.as_view(), name='school-education-system'),
    path('gallery/', GalleryListView.as_view(), name='school-gallery'),
    path('apply-info/', ApplyInfoView.as_view(), name='school-apply-info'),
]
