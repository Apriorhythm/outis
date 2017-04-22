from django.views import generic
from django.shortcuts import render



class IndexView(generic.ListView):
    template_name = 'outis_post/index.html'
#    context_object_name = 'all_objects'

    def get_queryset(self):
        return None


