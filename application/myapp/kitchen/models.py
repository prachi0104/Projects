from django.db import models

# Create your models here.

class ItemModel(models.Model):
    product=models.CharField(max_length=10)
    unit=models.CharField(max_length=50)
    qty=models.IntegerField()


    def __str__(self):
        return self.product
    


YEAR = (
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
    )
MONTH= (
        ('january', 'january'),
        ('february', 'february'),
        ('march', 'march'),
        ('april', 'april'),
        ('may', 'may'),
        ('june', 'june'),
        ('july', 'july'),
        ('august', 'august'),
        ('september', 'september'),
        ('october', 'october'),
        ('november', 'november'),
        ('december', 'december'),
    )

class MonthlyList(models.Model):
    year = models.CharField(max_length=256, null=True, choices=YEAR)
    month = models.CharField(max_length=255, null=True, choices=MONTH)
    product=models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty=models.IntegerField()
    unit=models.CharField(max_length=50,default='GRM')


    def __str__(self):
        return self.year
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    message=models.TextField()


    def __str__(self):
        return self.name
