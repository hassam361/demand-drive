from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Demand,FulfillContent
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import FulfillDemandForm
from django.contrib import messages
#rest Frame work commands
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated 




from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    RedirectView
)
# Create your views here.
def home(request):
    
    context = {
        'demands': Demand.objects.all(),

    }
    
    return render(request, 'website/index.html')

     

class DemandListView(ListView):
    
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Demand.objects.all()
        else:
            queryset = Demand.objects.filter(reviewed=True )

        return queryset

    template_name = 'website/index.html'  
    context_object_name = 'demands'
    ordering = ['-date_posted']




class VoteApiToggle(APIView):
   
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None, format=None):
        obj=get_object_or_404(Demand,pk=pk)
        user= self.request.user
        updated=False
        liked=False 
        
        if user.is_authenticated:
            if user in obj.votes.all():
                obj.votes.remove(user)
                liked=False
            else: 
                obj.votes.add(user)
                liked=True
        updated=True
        data={
        'updated': updated ,
        'liked' : liked
        }
       
        
        return Response(data)

class VoteToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj=get_object_or_404(Demand,pk=kwargs['pk'])
        url_='/'
        user= self.request.user
        if user.is_authenticated:
            if user in obj.votes.all():
                obj.votes.remove(user)
            else: 
                obj.votes.add(user)
        else:
            url_='/login'
        
        return url_
class ReviewDemand(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Demand, pk= kwargs['pk'])
        url_='/'
        user=self.request.user
        if user.is_superuser:
            obj.reviewed=True
            obj.save()
        else:
            url='sdsd'
        return url_


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