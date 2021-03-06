from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app.core.views import SemesterChoice, FirstSemester, SecondSemester, LexicalAnalysisView, SyntacticTreeView, \
    SemanticAnalysisView, LogicalSearch, TextSummarizer, TextTranslator, TextSynthesizer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SemesterChoice.as_view()),
    path('semester1/', FirstSemester.as_view(), name='sem-1'),
    path('semester2/', SecondSemester.as_view(), name='sem-2'),
    path('semester1/lab1/', LexicalAnalysisView.as_view(), name='lab1-1'),
    path('semester1/lab2/', LexicalAnalysisView.as_view(), name='lab2-1'),
    path('semester1/lab3/', SyntacticTreeView.as_view(), name='lab3-1'),
    path('semester1/lab4/', SemanticAnalysisView.as_view(), name='lab4-1'),
    path('semester2/lab1/', LogicalSearch.as_view(), name='lab1-2'),
    path('semester2/lab3/', TextSummarizer.as_view(), name='lab3-2'),
    path('semester2/lab4/', TextTranslator.as_view(), name='lab4-2'),
    path('semester2/lab5/', TextSynthesizer.as_view(), name='lab5-2')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
