from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from app.core.forms import InputForm
from app.core.utils.lab1 import process_text
from app.core.utils.lab3 import get_tree
from app.core.utils.lab4 import semantic_parse


class SemesterChoice(TemplateView):
    template_name = 'semester_menu.html'


class FirstSemester(TemplateView):
    template_name = 'semester_1.html'


class SecondSemester(TemplateView):
    template_name = 'semester_2.html'


class LexicalAnalysisView(FormView):
    form_class = InputForm
    template_name = 'semester_1/lab1.html'

    def form_valid(self, form):
        new_text = process_text(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))


class SyntacticTreeView(FormView):
    form_class = InputForm
    template_name = 'semester_1/lab3.html'

    def form_valid(self, form):
        new_text = get_tree(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=str(new_text.pformat())))


class SemanticAnalysisView(FormView):
    form_class = InputForm
    template_name = 'semester_1/lab4.html'

    def form_valid(self, form):
        new_text = semantic_parse(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))
