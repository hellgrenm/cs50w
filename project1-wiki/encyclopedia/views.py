from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django import forms
from django.urls import reverse
from markdown2 import markdown
import random

from . import util

class NewTaskForm(forms.Form):
    entry = forms.CharField(label="Title")
    content = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":"5", "cols": "40"}))


class EditForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 40})
    )


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    content = util.get_entry(title)

    if (content == None):
        return render(request, "encyclopedia/entry.html",{
            "message" : "Page not found."
        })
    else:
        content = markdown(content)

        return render(request, "encyclopedia/entry.html",{
            "title" : title, "entry" : content
        })



def edit(request, title):
    content = util.get_entry(title)

    if (request.method == "POST"):
        form = EditForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            content = content.replace("\r\n", "\n")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", args=[title]))
    else:
        form = EditForm(initial={"content": content})

    return render(request, "encyclopedia/edit.html",{
        "title": title,
        "form": form
    })




def new(request):
    if (request.method == "POST"):
        form = NewTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["entry"]
            content = form.cleaned_data["content"]

            if (util.get_entry(name)):
                return render(request, "encyclopedia/new.html", {
                    "message" : "Page already exists",
                    "form" : form
                })
            else:
                util.save_entry(name, content)
                return HttpResponseRedirect(reverse("entry", args=[name]))
        else:
            return render(request, "encyclopedia/new.html", {
                "form" : form
            })
    
    return render(request, "encyclopedia/new.html",{
        "form": NewTaskForm()
    })

def search(request):
    if request.method == "POST":
        search = request.POST.get('q').strip().lower()
        results = []

        for item in util.list_entries():
            if search == item.lower():
                return HttpResponseRedirect(reverse("entry", args=[item]))
            elif search in item.lower():
                results.append(item)

        if results:
            return render(request, "encyclopedia/searches.html", {
                "entries": results
            })
        else:
            return render(request, "encyclopedia/searches.html", {
                "message": f"No results for {search}"
            })

            
def random_article(request):
    articles = util.list_entries()
    return HttpResponseRedirect(reverse("entry", args=[random.choice(articles)]))

