from django.db import models

# Create your models here.
class TOPICFORM(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self) -> str:
        return self.topic_name
    

class WEBPAGESFORM(models.Model):
    topic_name=models.ForeignKey(TOPICFORM,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name
    

class ACCESSRECORDSFORM(models.Model):
    name=models.ForeignKey(WEBPAGESFORM,on_delete=models.CASCADE)
    authour=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self) -> str:
        return self.authour


