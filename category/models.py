from django.db import models

# Create your models here.

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=1000,null=False)


    @classmethod
    def getall(cls):
        context=cls.objects.all()
        return context
    @classmethod
    def get_single_category(cls,id):
        return cls.objects.get(pk=id)

    @classmethod
    def delete_single_category(cls,id):
        category = cls.objects.get(pk=id)
        category.delete()
        return True