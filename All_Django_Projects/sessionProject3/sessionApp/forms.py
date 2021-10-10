from django import forms #importing the forms from django module

#here we have to write the form Class

class Index_Form(forms.Form):
    item_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the Item Name"}))
    item_quantity=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Enter Item Quantity"}))
