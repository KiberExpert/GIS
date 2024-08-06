from django.db import models

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class NameModel(BaseModel):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True        

class CustomUser(BaseModel):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.EmailField(null=True)
    fullname = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.fullname}  {self.email}"