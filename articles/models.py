from django.db import models

# to add new field to the model use the following command:
# python3 manage.py makemigrations
# then type:
# python3 manage.py migrate


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    # add thumbnail
    # add author

    def __str__(self):
        return self.title
