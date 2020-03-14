from django.forms import Form, CharField, Textarea


class InputForm(Form):
    text = CharField(max_length=10000, widget=Textarea(), min_length=1)
