from django.urls import path
from django.contrib import admin

from app.core.views import LexicalAnalysisView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('analysis/', LexicalAnalysisView.as_view()),
]
