from django.db import models
#from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
from iran_mobile_va import mobile
# Create your models here.
#def validate_phone(value):
#    if not value.startswith('09'):
#        raise ValidationError('Phone number must start with 09')
#    if len(value) !=11:
#        raise ValidationError("Phone number must be exactly 11 digits long")
class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.CharField(max_length=11)

    subject=models.CharField(max_length=255)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
