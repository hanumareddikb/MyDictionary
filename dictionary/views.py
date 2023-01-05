from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from dictionary.models import Dictionary
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
"""
view for searching word meaning
"""
def search_word(request):
    # if user searches for meaning
    if request.method == "POST":
        word = request.POST['word']

        # check if the required word already exists in db(ie. in Dictionary model)
        check_word = Dictionary.objects.filter(word=word)
        
        # if required word already exists, 
        # than display the same with it's meaning to user
        if check_word.exists():
            data = Dictionary.objects.all().get(word=word)
            context = {'word': data.word, 'meaning': data.meaning}
            return render(request, 'dictionary/search_word.html', context)
        
        # if user searches the word for first time(ie. required word doesn't exists)
        # than call the external api dictionary.com and add word to it's url
        url = 'https://www.dictionary.com/browse/'+word

        # send a get request to above url
        req = requests.get(url)
        data = req.content # save the content of the reponse

        # parse the above html page using BeautifulSoup
        soup = BeautifulSoup(data, 'html.parser')

        # extract only 0th index data in one-click-content class in html page
        span = soup.find_all('span', {"class": "one-click-content"})

        # check word is valid or not
        try:
            meaning = span[0].text
        except IndexError: # if word is in valid
            messages.error(request, 'Soryy!! Your word is Invalid')
            return render(request, 'dictionary/search_word.html')
        
        # save the word and it's meaning in db(ie. in Dictionary model)
        dict = Dictionary(word=word.lower(), meaning=meaning)
        dict.save()
        
        # get user email
        email = request.user.email
        messages.success(request, "An Email with word and it's meaning sent to you!!")
        
        # send email to user
        send_mail("Your word meaning from MyDictionary",
                    f"Word: {word}\nMeaning: {meaning}",
                    "mailtrap@mydictionary.com",
                    [f'{email}'])

        # display the same to user
        context = {'word': word, 'meaning': meaning}
        return render(request, 'dictionary/search_word.html', context)

    return render(request, 'dictionary/search_word.html')


"""
view for displaying all words, those are in Dictionary model, 
to get it's meaning on click
"""
def list_words(request):
    # retrieve words from Dictionary model in db
    words_list = Dictionary.objects.order_by('word')
    paginator = Paginator(words_list,8)  # for pagination
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)
    context = {'words_list': page_obj}
    return render(request, 'dictionary/list_words.html', context)

"""
view to display word and it's meaning for the click on word in list_words.html page
"""
def word_meaning(request, word_id):
    # retrieve word and it's meaning from Dictionary model in db
    word_meaning1 = Dictionary.objects.filter(id=word_id) # pass the word_id from url 
    context = {'word_meaning': word_meaning1}
    return render(request,'dictionary/meaning.html', context)