from django.db import models

# Create your models here.

class Action(models.Model):
    verbe=models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')
    def __unicode__(self):
        return self.verbe

class Result(models.Model):
    action_id=models.ForeignKey(Action)
    result=models.CharField(max_length=255)
    def __unicode__(self):
        return self.result
    
class Mode(models.Model):
    action_id=models.ForeignKey(Action)
    mode=models.CharField(max_length=255)
    def __unicode__(self):
        return self.mode
    

    