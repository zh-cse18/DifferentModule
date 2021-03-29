from django.forms import forms

from core.qtec_app.models import SearchResult


class SearchForm(forms.Form):
    class Meta:
        model = SearchResult
