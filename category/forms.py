from django import forms
from .models import Category
class ProductFormModel(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

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


