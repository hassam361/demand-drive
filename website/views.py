from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Demand
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

class DemandListView(ListView):
    model = Demand
    template_name = 'website/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'demands'
    ordering = ['-date_posted']
    paginate_by = 5
class DemandDetailView(DetailView):
    model = Demand
class DemandCreateView(LoginRequiredMixin, CreateView):
    model = Demand
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class DemandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Demand
    fields = ['title', 'content']

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