from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import TackkleURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "nbx.in",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "nbx.in",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            print(form.cleaned_data.get("url"))
            new_url = form.cleaned_data.get("url")
            obj, created = TackkleURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created
            }
            if(created):
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"


        return render(request, template, context)


#
# #function based view
# def tackkle_redirect_view(request, shortcode=None, *args, **kwargs):
#     obj = get_object_or_404(TackkleURL, shortcode=shortcode)
#     # do something
#     return HttpResponseRedirect(obj.url)

#class based view
class TackkleCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(TackkleURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
