from django.db import models
from django.utils import timezone

# Create your models here.
class chaivarity(models.Model):
    chai_type_choice=[
        ('mc','masala'),
        ('gc','ginger'),
        ('kc','kiwi'),
        ('pc','plain'),
        ('ec','elichi'),
    ]
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images/")
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=chai_type_choice)
    
    
