from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.
from .models import SearchResult


def search(request):
    if request.method == 'POST':
        user = request.user
        word = request.POST.get('search_text')
        instance = SearchResult(user_name=user, keyword=word)
        if instance is not None:
            instance.save()
            return redirect('search')
    else:
        form = SearchResult()
    return render(request, 'search.html', {'form': form})


def search_result(request):
    name = []
    key = []
    result = SearchResult.objects.all()
    for unique_user in result:
        if unique_user.keyword not in key:
            key.append(unique_user.keyword)
        if unique_user.user_name not in name:
            name.append(unique_user.user_name)
    context = {
        'result': result,
        'key': key,
        'name': name

    }
    return render(request, 'search_result.html', context)