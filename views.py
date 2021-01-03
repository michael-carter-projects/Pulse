from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from django.db.models import Q
from . import twitter_search
from . import reddit_search
from . import youtube_search
# from django.views.generic import CreateView
# 19:56

# Create your views here.

def home(request):
    if request.method == 'POST':
        if request.POST.get('searchTerm'):
            search = Search()
            search.term = request.POST.get('searchTerm')
            search.author = request.user #need to update this asap
            search.save()
            return redirect('pulse-results')

    return render(request, 'pulse_search/home.html')

def about(request):
    return render(request, 'pulse_search/about_pulse.html')

def team(request):
    return render(request, 'pulse_search/pulse_team.html')

def display_results(request):
    #to pull from the database
    # search_term = Search.objects.all(username = user.username).first()???
    #retrieve latest search term from user account
    #run through relavent programs to create a dict of dicts, i.e.:
    # duck_duck_goose = twitter_search.main(search_term)
    # print(duck_duck_goose)
    # context ={
    #     'tweets_dict' : tweets_dict,
    #     'video_dict' : video_dict,
    #     'reddit_dict' : reddit_dict
    # }
    #finally pass into the render request
    search_term = Search.objects.last()
    # print(search_term)
    (tweets_dict1, sentiment_dict1) = twitter_search.main(search_term)
    (reddit_dict1)  =  reddit_search.main(search_term)
    (youtube_dict1) = youtube_search.main(search_term)
    # print(tweets_dict1)
    display_name = {'term' : search_term}
    context =  {'tweets_dict'    : tweets_dict1,
                'reddit_dict'    : reddit_dict1,
                'youtube_dict'   : youtube_dict1,
                'sentiment_dict' : sentiment_dict1,
                'searched_term'  : display_name }
    #to pull from the database
    # context = {'tweets_dict' : Search.objects.all()}
    return render(request, 'pulse_search/display_results.html', context)
