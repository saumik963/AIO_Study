from django.template import loader
from django.http import HttpResponseServerError
from wikipedia.exceptions import DisambiguationError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from django.views.generic.edit import UpdateView
from .forms import NotesForm, search, cal, Mod
from django.urls import reverse_lazy
from django.contrib import messages
from youtubesearchpython import VideosSearch
import requests
import wikipedia
# Create your views here.

#   factorial calculate


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#   Modulo calculate


def calculate_mod(num, mod):
    try:
        dividend = int(num)
        divisor = int(mod)

        if divisor == 0:
            return 0

        mod_result = dividend % divisor
        return mod_result
    except ValueError:
        return 0


def tooks(request):

    #   factorial calculate

    if request.method == "POST":
        form = cal()
        num_str = request.POST.get('num')

        try:
            num = int(num_str)  # Convert the input to an integer
            result = factorial(num)
        except ValueError:
            result = "Invalid input. Please enter a valid integer."

        context = {
            'form': form,
            "result": result,
            'das_act': "active",
        }

        print(context)
        return render(request, 'dashboard.html', context)

    else:
        context = {
            'das_act': "active",
        }

    return render(request, 'dashboard.html', context)


def Note(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            title = request.POST.get('Title')
            # Use lowercase 'description'
            description = request.POST.get('Description')

            # Check if both title and description are provided
            if title and description:
                # Create a new Notes object and associate it with the current user
                Notes.objects.create(
                    user=request.user, Title=title, Description=description)
                messages.success(request, 'Note added successfully.')
            else:
                messages.error(
                    request, 'Both title and description are required.')
            # Redirect back to the notes page after adding a task
            return redirect('Note')

        # Fetch the user's notes
        notes = Notes.objects.filter(user=request.user)

        return render(request, 'notes.html', {'note_act': "active", "data": notes})


def NoteComplete(request, id):
    notes = Notes.objects.get(id=id)
    if notes.is_completed == False:
        notes.is_completed = True
    else:
        notes.is_completed = False

    notes.save()
    return redirect('Note')


def DeleteNote(request, id):
    notes = Notes.objects.get(pk=id).delete()
    return redirect('Note')


def NoteUpdate(request, pk):
    notes = get_object_or_404(Notes, pk=pk)

    if request.method == "POST":
        form = NotesForm(request.POST, instance=notes)
        if form.is_valid():
            form.save()
            return redirect('Note')
    else:
        form = NotesForm(instance=notes)

    # Access and print the values inside taskTitle and taskDescription
    # print("taskTitle:", task.taskTitle)
    # print("taskDescription:", task.taskDescription)

    return render(request, 'edit_task.html', {'form': form, "notes": notes})

import googleapiclient.discovery
def ytAPI(text):

    DEVELOPER_KEY = "AIzaSyAOYF_7a930oG6UFKWSQEOWfv2y-4AQew4"

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=DEVELOPER_KEY)

    search_query = text
    part = "snippet"

    request = youtube.search().list(
        part=part,
        q=search_query,
        type="video",
        maxResults=30  # Adjust as needed
    )

    response = request.execute()

    videos=[]

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        thumbnails = item["snippet"]["thumbnails"]


        # Create video URL using the video ID
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        channel_request = youtube.videos().list(
        part="snippet",
        id=video_id
        )
        channel_response = channel_request.execute()

        # Access and extract channel name
        channel_name = channel_response["items"][0]["snippet"]["channelTitle"]

        thumbnail_url = thumbnails["medium"]["url"]


        result_dict = {
                    'input': text,
                    'title': title,
                    'thumbnail': thumbnail_url,
                    'channel': channel_name,
                    'link': video_url,
                    'description': description,
                }
        videos.append(result_dict)

    return videos


def Videos(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = search()
            text = request.POST['text']


            result_list = ytAPI(text)

            context = {
                'form': form,
                'yt_act': "active",
                'results': result_list,
            }
            return render(request, 'youtube.html', context)

        else:
            form = search()
        return render(request, 'youtube.html', {"form": form, 'yt_act': "active"})


def books(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = search()
            text = request.POST["text"]
            url = "https://www.googleapis.com/books/v1/volumes?q="+text
            r = requests.get(url)

            answer = r.json()
            result_list = []
            for i in range(10):
                result_dict = {

                    'title': answer['items'][i]['volumeInfo']["title"],
                    'subtitle': answer['items'][i]['volumeInfo'].get("subtitle"),
                    'description': answer['items'][i]['volumeInfo'].get("description"),
                    'count': answer['items'][i]['volumeInfo'].get("pageCount"),
                    'categories': answer['items'][i]['volumeInfo'].get("categories"),
                    'rating': answer['items'][i]['volumeInfo'].get("pageRating"),
                    'thumbnail': answer['items'][i]['volumeInfo'].get("imageLinks").get("thumbnail"),
                    'preview': answer['items'][i]['volumeInfo'].get("previewLink"),

                }
                result_list.append(result_dict)
                context = {
                    "form": form,
                    'book_act': "active",
                    'results': result_list
                }
            return render(request, 'books.html', context)

        form = search()
        context = {
            "form": form,
            'book_act': "active",
        }
        return render(request, 'books.html', context)


def dictionary(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            form = search()
            text = request.POST["text"]
            url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
            r = requests.get(url)

            answer = r.json()

            print(text)

            phonetics = answer[0]["phonetics"][0]['text']
            audio = answer[0]["phonetics"][0]['audio']
            definition = answer[0]["meanings"][0]['definitions'][0]['definition']
            example = answer[0]["meanings"][0]['definitions'][0]['example']
            synonyms = answer[0]["meanings"][0]['definitions'][0]['synonyms']

            context = {
                'form': form,
                "dic_act": "active",
                'input': text,
                'phonetics': phonetics,
                'audio': audio,
                'definition': definition,
                'example': example,
                'synonyms': synonyms,
            }

            return render(request, 'dictionary.html', context)
        else:
            form = search()
            context = {
                'form': form,
                "dic_act": "active",
            }

        return render(request, 'dictionary.html', context)


def wiki(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST":
            text = request.POST["text"]
            form = search()

            try:
                ser = wikipedia.page(text)

                context = {
                    'form': form,
                    'title': ser.title,
                    'link': ser.url,
                    'details': ser.summary,
                }
                return render(request, 'wiki.html', context)

            except DisambiguationError as e:
                options = e.options
                context = {
                    'form': form,
                    'disambiguation_error': True,
                    'options': options,
                }
                return render(request, 'wiki.html', context)

        else:
            form = search()
            context = {
                'form': form,
                "wiki_act": "active",
            }

        return render(request, 'wiki.html', context)


def error_404(request, exception):
    return render(request, 'error_404.html')


def error_500(request):
    template = loader.get_template('error_500.html')
    context = {}  # You can pass any necessary context data here
    return HttpResponseServerError(template.render(context, request))
