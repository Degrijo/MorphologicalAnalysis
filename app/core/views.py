from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from app.core.forms import InputForm
from app.core.utils.lab1 import process_text


class MainMenu(TemplateView):
    template_name = 'menu.html'


class LexicalAnalysisView(FormView):
    form_class = InputForm
    template_name = 'input.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        new_text = process_text(form.cleaned_data['text'])
        return self.render_to_response(self.get_context_data(form=form, new_text=new_text))
