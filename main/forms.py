from crispy_forms.helper import FormHelper
from django import forms
from django.urls import reverse
from crispy_forms.layout import Layout, Div, Submit, Fieldset, Field

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['description', 'attachment', 'name', ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-md-12"),
                css_class="row"),
            Div(
                Div('description', css_class="col-md-12"),
                css_class="row"),
            Div(
                Div('attachment', css_class="col-md-12"),
                css_class="row"),

            Div(
                Div(
                    Submit('save', 'Save Changes', css_class='btn btn-info btn-block'),
                    css_class="col-md-3"),
                css_class="row"),
        )
