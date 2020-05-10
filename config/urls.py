from django.urls import path
from django.contrib import admin

from app.core.views import MainMenu, LexicalAnalysisView, SyntacticTreeView, SemanticAnalysisView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainMenu.as_view()),
    path('lab1/', LexicalAnalysisView.as_view()),
    path('lab2/', LexicalAnalysisView.as_view()),
    path('lab3/', SyntacticTreeView.as_view()),
    path('lab4/', SemanticAnalysisView.as_view()),
]
