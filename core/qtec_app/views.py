from datetime import date, timedelta

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
    return render(request, 'qtec/search.html', {'form': form})


def search_result(request):
    name = []
    key = []
    final_result = {}
    all_result = SearchResult.objects.all()
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        yestrday = request.POST.get('yesterday')
        lastweek = request.POST.get('lastweek')
        print(yestrday)
        print(lastweek)

        if yestrday:
            today =date.today()
            yesterday = today - timedelta(days=1)
            result = SearchResult.objects.filter(searched_at=yesterday)
            print(yesterday)

        if lastweek:
            today = date.today()
            lastday = today - timedelta(days=6)
            result = SearchResult.objects.filter(searched_at__gte=today, searched_at__lte=lastday)
            print(lastday)

        if start_date and end_date:
            result = SearchResult.objects.filter(searched_at__gte=start_date, searched_at__lte=end_date)

        all_selected_word = request.POST.getlist('select_word')
        all_selected_user = request.POST.getlist('select_user')  
        if all_selected_word:
            for each_word in all_selected_word:
                result_eachword = SearchResult.objects.filter(keyword=each_word)
                # final_result[each_word] = result_eachword
                final_result[each_word] = len(result_eachword)
                print(final_result)

        for unique_user in all_result:
            if unique_user.keyword not in key:
                key.append(unique_user.keyword)
            if unique_user.user_name not in name:
                name.append(unique_user.user_name)

        context = {
        'result': all_result,
        'key': key,
        'name': name,
        'final_result': final_result
        }
        return render(request, 'qtec/search_result.html', context)

    else:
        for unique_user in all_result:
            if unique_user.keyword not in key:
                key.append(unique_user.keyword)
            if unique_user.user_name not in name:
                name.append(unique_user.user_name)

    context = {
        'result': all_result,
        'key': key,
        'name': name,
        'final_result': final_result
    }
    return render(request, 'qtec/search_result.html', context)