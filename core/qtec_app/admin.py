from django.contrib import admin
from .models import SearchResult, NewSearchResult


class SearchResultAdmin(admin.ModelAdmin):
    class Meta:
        model = SearchResult
    list_display = ['user_name', 'keyword', 'searched_at']
    search_fields = ('user_name', 'keyword', 'searched_at')


admin.site.register(SearchResult, SearchResultAdmin)


class NewSearchResultAdmin(admin.ModelAdmin):
    class Meta:
        model = NewSearchResult
    list_display = [ 'keyword', 'searched_at']
    search_fields = ('user_name', 'keyword', 'searched_at')


admin.site.register(NewSearchResult, NewSearchResultAdmin)
