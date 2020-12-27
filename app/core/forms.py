from django.forms import Form, CharField, Textarea, FileField, ChoiceField


LANG_CHOICES = (('en', 'English'), ('ru', 'Russian'), ('de', 'German'), ('fr', 'French'))


class TextForm(Form):
    text = CharField(max_length=10000, widget=Textarea(), min_length=1)


class FileForm(Form):
    file = FileField()


class LangForm(Form):
    text = CharField(max_length=10000, widget=Textarea(), min_length=1)
    lang = ChoiceField(choices=LANG_CHOICES)
