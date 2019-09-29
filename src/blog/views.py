from django.shortcuts import render

# Create your views here.

posts = [
    {
        'title': 'التدوينة الاولي',
        'content': 'نص التدوينة الاولي كنص تجريبى ',
        'post_date':'29/9/2019',
        'auther':'Asaad Mohammed',
    },
    {
        'title': 'التدوينة الثانية',
        'content': 'نص التدوينة الثانية كنص تجريبى ',
        'post_date':'30/3/2019',
        'auther':'Asaad Mohammed',
    },
    {
        'title': 'التدوينة الثالثة',
        'content': 'نص التدوينة الثالثة كنص تجريبى ',
        'post_date':'16/9/2019',
        'auther':'Asaad Mohammed',
    },
    {
        'title': 'التدوينة الرابعة',
        'content': 'نص التدوينة الرابعة كنص تجريبى ',
        'post_date':'29/1/2019',
        'auther':'Asaad Mohammed',
    },
]

def home(request):
    context = {
        'title':'الصفحة الرئيسية',
        'posts':posts

    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'من انا'})