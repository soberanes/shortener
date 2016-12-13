from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REIRECT_URL = getattr(settings, "DEFAULT_REIRECT_URL", "http://www.nbx.in:8000")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REIRECT_URL
    if path is not None:
        new_url = DEFAULT_REIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)
