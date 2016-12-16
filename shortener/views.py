from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import TackkleURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        bg_image = 'http://www.attpbgolf.com/content/uploads/2015/09/Pebble-Beach-8th-Hole-1800x1200.jpg'
        context = {
            "title": "nbx.in",
            "form": the_form,
            "bg_image": bg_image
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
class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = TackkleURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404

        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
