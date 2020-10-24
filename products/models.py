from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural= 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=5000)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    salePrice = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    download = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    description = models.CharField(max_length=5000)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

# class FilesAdmin(models.Model):
#     adminupload = models.FileField(upload_to='media')
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title