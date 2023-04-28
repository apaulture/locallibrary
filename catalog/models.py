from django.db import models
from django.conf import settings
from django.urls import reverse

# class Genre(models.Model):


# class Author(models.Model):
#     name = models.CharField()
#     date_of_birth = models.DateField()
#     date_of_death = models.DateField()

# class Book(models.Model):
#     author = models.ForeignKey(Author)
#     title = models.CharField()
#     genre = models.ForeignKey(Genre)

#     class Meta:
#         ordering = ['author', 'title']
#         unique_together = [['author', 'title']]
    
#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('model-detail-view', args = [str(self.id)])

# class BookInstance(models.Model):
#     LOAN_STATUS = (
#         (, )
#     )

#     book = models.ForeignKey(Book, on_delete = models.SET_NULL, null = True)
#     status = models.CharField(choices = LOAN_STATUS, max_length = 100)
#     borrower = models.ForeignKey(settings.AUTH_USER_MODEL)