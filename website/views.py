from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Demand,FulfillContent
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import FulfillDemandForm
from django.contrib import messages

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
        'demands': Demand.objects.all(),

    }
    
    return render(request, 'website/index.html')

     

class DemandListView(ListView):
    model = Demand
    template_name = 'website/index.html'  
    context_object_name = 'demands'
    ordering = ['-date_posted']

   
def DemandDetailView(request, pk):
    demand=Demand.objects.get(id=pk)
    if request.method == 'POST':
        form =  FulfillDemandForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
            if ((data['f_suggestion'] =='') and (len(request.FILES) == 0)):
                fulfillers=FulfillContent.objects.filter(demand=demand)
   
                form =FulfillDemandForm()
                messages.info(request,"You have not fulfilled any demand")
                
            else:
                fulfilled_Content=FulfillContent.objects.create(
                    demand=demand,
                    fulfiller=request.user,
                    f_suggestion=data['f_suggestion'],
                    f_content=data['f_content']

                )
                demand.status="fulfilled by "+request.user.username
                demand.save()
                fulfilled_Content.save()
                return HttpResponseRedirect("/demand/{id}/".format(id= demand.id))
        
            
    else:
        form = FulfillDemandForm()
    fulfillers=FulfillContent.objects.filter(demand=demand)
    return render(request,'website/demand_detail.html',context={'object':demand,'form':form,'fulfillers':fulfillers})

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