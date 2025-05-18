from django import forms
from .models import *
from category.models import Category
class ProductFormModel(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'category': 'Product Category'  # Custom label
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].label_from_instance = lambda obj: obj.name

class ProductFormUpdate(forms.Form):
    name=forms.CharField(required=True,max_length=100)
    description=forms.CharField(max_length=1000)
    price = forms.IntegerField()
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Product Category'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = lambda obj: obj.name


