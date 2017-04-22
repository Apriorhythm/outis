from django.views import generic
from django.shortcuts import render



class IndexView(generic.ListView):
    template_name = 'outis_user/index.html'

    def get_queryset(self):
        return None

