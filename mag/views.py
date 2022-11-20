from django.shortcuts import render


def post_list(request):
    return render(request, 'mag/post_list.html', {})
