from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()
# Create your models here.


class BookCategory(models.Model):
    category=[
        ('theology','THEOLOGY'),
        ('education','EDUCATION'),
        ('music','MUSIC'),
        ('programming','PROGRAMMING'),
        ('sports','SPORT')
    ]

    isbn= models.CharField(max_length=50,null=False,unique=True)
    book_title=models.CharField(max_length=100,null=False)
    book_category=models.CharField(max_length=100,choices=category,blank=False,null=False)
    book_author=models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.book_title



def expiration():
    return datetime.today() + timedelta(days=15)

class Borrowing(models.Model):
    booktitle=models.ForeignKey(BookCategory,related_name='book',max_length=50,on_delete=models.CASCADE)
    borrowed_by=models.ForeignKey(User, max_length=50,on_delete=models.CASCADE)
    borrowed_date=models.DateField(auto_now_add=True)
    returning_date=models.DateField(default= expiration)

    def __str__(self):
        return self.borrowed_by
