from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
# customizing models from crash

class MyUserManager(BaseUserManager):
    
    def _create_user(self,mobileno,password,**extrafields):
        if not mobileno :
            raise ValueError('Please Enter Mobile No......')
        user = self.model(mobileno=mobileno,password=password,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self,mobileno,password,**extrafields):
        extrafields.setdefault('is_superuser',False)
        extrafields.setdefault('role','customer')
        user = self._create_user(mobileno,password,**extrafields)
        return user

    def create_superuser(self,mobileno,password,**extrafields):
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('role','owner')
        user = self._create_user(mobileno,password,**extrafields)
        return user 

class MyUser(AbstractBaseUser):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    mobileno = models.BigIntegerField(unique=True)
    role = models.CharField(default = 'customer' ,max_length=30)
    address = models.TextField()
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD  = 'mobileno'
    REQUIRED_FIELDS = []