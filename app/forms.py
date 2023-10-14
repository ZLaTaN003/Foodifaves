from .models import Item
from django import forms


class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_description", "item_price", "item_img"]
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'item_description': forms.Textarea(attrs={'class': 'form-control'}),
            'item_price': forms.TextInput(attrs={'class': 'form-control'}),
             
            
        }
