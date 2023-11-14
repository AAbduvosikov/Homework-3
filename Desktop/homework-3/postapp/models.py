from django.db import models

class Post(models.Model):
    Nomi = models.CharField(max_length=1000,blank=True,null=True)
    Statiya = models.CharField (max_length=1000)
    Time = models.TimeField(auto_now=True)

    def __str__(self) -> str:
        return self.Nomi