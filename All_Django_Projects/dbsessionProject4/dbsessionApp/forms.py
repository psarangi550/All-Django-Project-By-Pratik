from django import forms #importing the forms from the django module

#create the form class

class Item(forms.Form):
    item=forms.CharField()
    quantity=forms.IntegerField()
