from django.shortcuts import render

posts = [
    {
        'author': 'Krupesh Anadkat',
        'title': 'Introduction To Blockchain & Cryptocurrency',
        'content': 'In this article, we would like to understand Blockchain & Cryptocurrency. Why it exists & how could you leverage it as a developer. We will not look at any piece of code in this article, but definitely yes in the coming post. I am a full stack developer by passion, started learning blockchain about 1 and half years ago.',
        'date': 'July 15, 2021'
    },
    {
        'author': 'John Rening',
        'title': 'Deploying React Js Project on Google Firebase',
        'content': 'We will not spend time in writing React Redux app rather let me share with you a readymade redux-scaffold-project. Please grab your copy from github repository here. In case you want to test the application then please follow the Installation steps written in project Readme.',
        'date': 'November 09, 2020'
    },
]

# Create your views here.


def home(request):
    context = {'posts': posts, 'title': 'Latest Articles'}
    return render(request, 'app_blog/home.html', context)


def about(request):
    context = {'title': 'About This Blog'}
    return render(request, 'app_blog/about.html', context)
