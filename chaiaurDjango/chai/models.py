from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class chaiVarity(models.Model):
    CHAI_TYPES_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KI', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    # price_cup={
    #     "ml":15,
    #     "gr":15,
    #     "ki":25,
    #     "pl":10,
    #     "el":10,
    # }
   
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPES_CHOICE)
    #price= models.CharField(max_length=2,choices=price_cup)
    description = models.TextField(default="")
    
    
    def __str__(self):
        return self.name 
    
# one to many
class chai_review(models.Model):
    chai=models.ForeignKey(chaiVarity,on_delete=models.CASCADE,related_name="review")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_add=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many

class store(models.Model):
    names=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varieties=models.ManyToManyField(chaiVarity,related_name='stores')

    def __str__(self):
        return self.names


# one to one

class cetificate(models.Model):
    chai_n=models.OneToOneField(chaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issue_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    # def __str__(self):
    #     return f'certificate for {self.name.chai}'