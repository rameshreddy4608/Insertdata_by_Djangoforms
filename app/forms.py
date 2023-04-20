from django import forms

class Studentform(forms.Form):
    topic_name=forms.CharField(max_length=100)



class Studentformweb(forms.Form):
    topic_name=forms.CharField(max_length=100)
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()


class Studentformaccess(forms.Form):
    name=forms.CharField(max_length=100)
    authour=forms.CharField(max_length=100)
    date=forms.DateField()
    