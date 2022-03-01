from django.db import models
import datetime
import uuid

# Create your models here.

class Author(models.Model):
    first_name = models.CharField (max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

#class Customer(models.Model):
#    first_name = models.CharField (max_length=100)
#    last_name = models.CharField(max_length=100)
#    email = models.EmailField()
#    address = models.CharField(max_length=100)
#    books = models.ForeignKey(Book, on_delete=models.CASCADE)
#    def __str__(self):
#        return f"{self.first_name}{self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('year published')
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
#    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def storage(self):
        return self.bookinstance_set.count()
    storage.admin_order_field = 'storage'
    def avail(self):
        return self.bookinstance_set.filter(loan_status='A').count()
    avail.admin_order_field = 'available_num'
    def __str__(self):
        return ("{0}:{1}".format(self.title))
#    def __str__(self):
#        return f"{self.title} ({self.pub_date.year})"

#class BookInstance(models.Model):
#    uid = models.UUIDField(default=uuid.uuid4)
#    book = models.ForeignKey(Book, on_delete=models.SET_NULL,null=True)
#    imprint = models.CharField(max_length=100, null=True)
#    location = models.CharField(max_length=20, unique=True)
#    LOAN_STATUS_CHOICE = [
#        ('A', 'Available'),
#        ('O', 'On Loan'),
#    ]
#    loan_status = models.CharField(max_length=1,choices=LOAN_STATUS_CHOICE, default='A')
#
#    def __str__(self):
#        return ('{0} ({1})'.format(self.book.title, self.location))

#class Borrow(models.Model):
#    bookins = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
#    bor_time = models.DateField("borrow time", auto_now_add=True)
    
#    BOR_STATUS_CHOICES = [
#        ('K', 'keeping'),
#        ('R', 'returned'),
#    ]
#    bor_status = models.CharField(max_length=1,choices=BOR_STATUS_CHOICES,default='K')
#    f = models.DecimalField("Final Fine",max_digits=6,decimal_places=2,default=0)
    
#    def loc(self):
#        location = self.bookins.location
#        return ('{}'.format(location))

#    @property
#    def loca(self):
#        return self.loc()
