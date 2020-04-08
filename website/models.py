from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Count

# Create your models here.
class Demand(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    supp_content=models.FileField(upload_to='supporting_content/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    votes=models.ManyToManyField(User,blank=True, related_name='demand_votes')
    status=models.CharField(null=True ,max_length=100)
    reviewed = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('demand-detail', kwargs={'pk': self.pk})
    def get_vote_url(self):
        return reverse('demand-detail',kwargs={'pk': self.pk})
    def get_fulfillers_count(self):
        obj=FulfillContent.objects.filter(demand=self.id).count()
        return obj
    def get_author_name(self):
        return self.author.username

class FulfillContent(models.Model):
    demand=models.ForeignKey(Demand,on_delete=models.CASCADE,null=True)
    fulfiller=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    f_suggestion=models.CharField(max_length=500,null=True,default='') # fulfiller can also give suggestion  
    f_content=models.FileField(upload_to='fullfilled_content/',null=True) # fulfilled content 
    date_fulfilled = models.DateTimeField(default=timezone.now)
    user_votes=models.ManyToManyField(User,blank=True, related_name='user_votes')
    def get_vote_up_url(self , *args, **kwargs):
        return reverse('user-vote-up',kwargs={ 'pk': self.demand.id ,'fill':self.pk})
    def get_vote_down_url(self , *args, **kwargs):
        return reverse('user-vote-down',kwargs={ 'pk': self.demand.id ,'fill':self.pk})


