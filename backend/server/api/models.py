from django.db import models
import bcrypt
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def __str__(self):
        return self.username

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    number = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    email = models.EmailField(max_length=50, null=True)
    address = models.TextField(max_length=200, null=True)
    city = models.CharField(max_length=20, null=True)
    pin = models.IntegerField(null=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    comment = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name