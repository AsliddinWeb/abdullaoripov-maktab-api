from django.urls import path
from .views import SendMessageView

urlpatterns = [
    # Existing URL patterns
    path('send/', SendMessageView.as_view(), name='send-message'),
]
