from django.db import models
from django.shortcuts import reverse, get_object_or_404


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='books/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    @property
    def show_url(self):
        pass
        url = reverse('book_show', args=[self.id])
        return url

    @property
    def delete_url(self):
        pass
        url = reverse('book_delete', args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @property
    def update_url(self):
        url = reverse('book_update', args=[self.id])
        return url

    @classmethod
    def get_book_by_id(cls, id):
        return  get_object_or_404(cls, pk=id)

    @property
    def update_forms_url(self):
        url = reverse('book_update_model_forms', args=[self.id])
        return url
