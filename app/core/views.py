from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.conf import settings

from app.core.forms import TextForm, FileForm, LangForm
from app.core.utils.lab1 import process_text
from app.core.utils.lab3 import get_tree
from app.core.utils.lab4 import semantic_parse
from app.core.django_utils import get_closest_docs
from app.core.algorithms import custom_summarize, keywords, translate, synthesize


class SemesterChoice(TemplateView):
    template_name = 'semester_menu.html'


class FirstSemester(TemplateView):
    template_name = 'semester_1.html'


class SecondSemester(TemplateView):
    template_name = 'semester_2.html'


class LexicalAnalysisView(FormView):
    form_class = TextForm
    template_name = 'semester_1/lab1.html'

    def form_valid(self, form):
        new_text = process_text(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))


class SyntacticTreeView(FormView):
    form_class = TextForm
    template_name = 'semester_1/lab3.html'

    def form_valid(self, form):
        new_text = get_tree(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=str(new_text.pformat())))


class SemanticAnalysisView(FormView):
    form_class = TextForm
    template_name = 'semester_1/lab4.html'

    def form_valid(self, form):
        new_text = semantic_parse(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))


class LogicalSearch(FormView):
    form_class = TextForm
    template_name = 'semester_2/lab1.html'

    def form_valid(self, form):
        data = form.cleaned_data
        documents = get_closest_docs(data['text'])
        return self.render_to_response(self.get_context_data(form=form, documents=documents))


class TextSummarizer(FormView):
    form_class = FileForm
    template_name = 'semester_2/lab3.html'

    def form_valid(self, form):
        data = form.cleaned_data
        text = data['file'].read().decode('utf-8')
        return self.render_to_response(self.get_context_data(form=form,
                                                             summarizing=custom_summarize(text),
                                                             key_words=keywords(text)))


class TextTranslator(FormView):
    form_class = TextForm
    template_name = 'semester_2/lab4.html'

    def form_valid(self, form):
        data = form.cleaned_data
        translated_text = translate(data['text'])
        return self.render_to_response(self.get_context_data(form=form, translated_text=translated_text))


class TextSynthesizer(FormView):
    form_class = LangForm
    template_name = 'semester_2/lab5.html'

    def form_valid(self, form):
        data = form.cleaned_data
        synthesized_text_url = synthesize(data['text'], data['lang'], settings.MEDIA_ROOT)
        return self.render_to_response(self.get_context_data(form=form, synthesized_text_url=synthesized_text_url))
