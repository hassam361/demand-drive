from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Demand(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    d_fulfiller =models.IntegerField(null=True) # demand Fulfiller id
    supp_content=models.FileField(upload_to='supporting_content/')
    f_suggestion=models.CharField(max_length=500) # fulfiller can also give suggestion  
    f_content=models.FileField(upload_to='fullfilled_content/') # fulfilled content 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('demand-detail', kwargs={'pk': self.pk})