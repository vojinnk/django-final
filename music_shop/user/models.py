from django.db import models
from  django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self,username, password,email, number= None, town = None):
        if username is None:
            raise TypeError('Users must have an username.')
        user = User(username=username, number=number,  
        email=self.normalize_email(email),town=town)
        user.set_password(password)
        user.save()
        return user
    def get_by_natural_key(self, username):
        return self.get(username=username)
        

 
class User(AbstractBaseUser):
    number =models.CharField(max_length=15,blank=False,null=False)
    username= models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True, db_index=True)
    password= models.CharField(max_length=128,blank=False,null=False)  
    createdtime= models.TimeField(auto_now_add=True)   
    is_seller = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']
    readonly_fields=('is_seller', )
    objects = UserManager()
 
    def __str__(self):
        return self.username


class UserToken(models.Model):
    token= models.CharField(max_length=200, blank=False,null=False,db_index=True) 
    user= models.ForeignKey(User, related_name='token',on_delete=models.CASCADE)
    def __str__(self):
        return self.token