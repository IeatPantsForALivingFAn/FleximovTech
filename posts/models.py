from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=256)
    created_date = models.DateField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    image = models.ManyToManyField('Image',related_name='image')

    def __str__(self):
        """
        string representation of each model
        """
        return self.title

    def get_absolute_url(self):
        """
        canonical url for each model
        """
        return reverse('posts:post_detail',args=[self.id])

    class Meta:
        ordering = ['created_date']

class Image(models.Model):
    image_field = models.ImageField(upload_to='images/')
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return 'image '+str(self.id)
    def get_absolute_url(self):
        return reverse('posts:image_detail',args=[self.id])
