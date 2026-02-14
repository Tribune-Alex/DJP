from django import forms
from store.models import Product, ProductImage
from django.forms import inlineformset_factory

class Add_product(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude= ['wishlisted_by']

ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    fields=('image',),
    extra=3,
    can_delete=True
)