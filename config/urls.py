from django.urls import path
from django.contrib import admin

from app.core.views import MainMenu, LexicalAnalysisView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMenu.as_view()),
    path('lab1/', LexicalAnalysisView.as_view()),
]
