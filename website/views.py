from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Demand
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import FulfillDemandForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
def home(request):
    context = {
        'demands': Demand.objects.all()
    }
    
    return render(request, 'website/index.html')

def fulfillDemand(request,pk):
    demand=Demand.objects.get(id=pk)
    if request.method == 'POST':
        form =  FulfillDemandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FulfillDemandForm()
    return render(request, 'website/demand_detail.html', {
        'form': form
    })
    
class DemandListView(ListView):
    model = Demand
    template_name = 'website/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'demands'
    ordering = ['-date_posted']
   
def DemandDetailView(request, pk):
    demand=Demand.objects.get(id=pk)
    if request.method == 'POST':
        form =  FulfillDemandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FulfillDemandForm()
    return render(request,'website/demand_detail.html',context={'object':demand,'form':form})

class DemandCreateView(LoginRequiredMixin, CreateView):
    model = Demand
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class DemandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Demand
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        demand = self.get_object()
        if self.request.user == demand.author:
            return True
        return False


class DemandDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Demand
    success_url = '/'

    def test_func(self):
        demand = self.get_object()
        if self.request.user == demand.author:
            return True
        return False