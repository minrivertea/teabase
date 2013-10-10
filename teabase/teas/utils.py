from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404


#render shortcut
def _render(request, template, context_dict=None, **kwargs):
        
    return render_to_response(
        template, context_dict or {}, context_instance=RequestContext(request),
                              **kwargs
    )

