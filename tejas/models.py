from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)



class Publisher(models.Model):
    """Model representing a Language (e.g. Int journal of MM, Int Journal of Mfg, Int Journal of Materials, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the publication name (e.g. Int journal of MM, Int Journal of Mfg, Int Journal of Materials, etc.)")
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=500)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class ResearchPaper(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Author as a string rather than object because it hasn't been declared yet in the file

    abstract = models.TextField(max_length=1000, help_text='Enter a brief description of the Research Paper')

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    date_of_publication = models.DateField(null=True, blank=True)

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    author = models.ManyToManyField('Author', help_text='Select the Authors for this Research Paper')
    # Foreign Key used because ResearchPaper can only have one publisher, but publisher can have multiple ResearchPaper
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def display_author(self):
        """Creates a string for the author. This is required to display author in Admin."""
        return ', '.join([author.name for author in self.author.all()[:7]])

        display_author.short_description = 'author'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('researchpaper-detail', args=[str(self.id)])


from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to='project_image')
# Create your models here.
