from site import setquit

from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):
    id=models.AutoField(primary_key=True,null=False)
    name=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=1000,null=True)
    price=models.BigIntegerField(null=False)
    stock=models.BigIntegerField(null=False)
    image=models.ImageField(upload_to='{%static%}/imgs',blank=True,null=True)
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    @classmethod
    def get_all_products(cls):
        context=cls.objects.filter(status=True)
        return context
    @classmethod
    def get_single_product(cls,id):
        single_product=cls.objects.get(id=id)
        return single_product
    @classmethod
    def delete_single_product(cls,id):
        product = cls.objects.get(id=id)
        product.delete()
        return True, "Product deleted successfully"
