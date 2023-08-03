from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app.forms import *

# Create your views here.
class tempinsertdata(TemplateView):
    template_name = 'tempinsertdata.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        st_obj = Studentform()
        context['st_obj'] = st_obj
        return context
    
    def post(self, request):
        SFD = Studentform(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data has been inserted')
