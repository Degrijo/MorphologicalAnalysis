from django.forms import Form, CharField, Textarea, FileField


class InputForm(Form):
    text = CharField(max_length=10000, widget=Textarea(), min_length=1)


class FileForm(Form):
    file = FileField()
