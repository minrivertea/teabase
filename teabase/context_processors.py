from django.conf import settings
from django.contrib.sites.models import get_current_site




def common(request):
    context = {}
    context['ga_is_on'] = settings.GA_IS_ON
    context['base_template'] = settings.BASE_TEMPLATE 
     

    return context
    
 
