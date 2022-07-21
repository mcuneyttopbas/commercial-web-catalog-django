from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField
from datetime import datetime

class CareInstruction(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default=None)
    icon = models.ImageField(upload_to="settings/care_instructions")

    def __str__(self) -> str:
        return f"{self.name}"

class DesignDirection(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="settings/design_directions")
    
    def __str__(self) -> str:
        return f"{self.name}"

class Composition(models.Model):
    TYPES_CHOICES = (
    ('natural','NATURAL'),
    ('not-natural', 'NOT-NATURAL'))

    type = models.CharField(max_length=20, choices=TYPES_CHOICES, default='vowen')
    name = models.CharField(max_length=150, default=None)
    icon = models.FileField(upload_to="feature_icons" ,blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Usage(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f"{self.name}"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name) 
        super().save(*args, **kwargs)

class Feature(models.Model):
    name = models.CharField(max_length=15)
    icon = models.FileField(upload_to="feature_icons")

    def __str__(self) -> str:
        return f"{self.name}"

class Collection(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    subtitle = models.CharField(max_length=50)
    description = RichTextField()

    def generate_main_filename(self, filename):
        name = "collections/%s/main/%s" % (self.title , filename)
        return name

    main_image =  models.ImageField(upload_to=generate_main_filename, default=None)

    # Status Details
    is_active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    is_exclusive = models.BooleanField(default=False)
    is_contract = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.title}"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CollectionImages(models.Model):
    collection = models.ForeignKey(Collection, default=None, on_delete=models.CASCADE)

    def generate_filename(self, filename):
        name = "collections/%s/%s" % (self.collection.name , filename)
        return name

    image = models.ImageField(upload_to=generate_filename)
    

class Product(models.Model):
    # Product ID
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    code = models.CharField(max_length=20, blank=False)
    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.SET_NULL)
    create_date = models.DateField(default=timezone.now())

    # Product Details
    description = RichTextField()
    width = models.PositiveIntegerField(blank=False)
    weight = models.PositiveIntegerField(blank=False)
    horizontal_repeat = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=1 )
    vertical_repeat = models.DecimalField(max_digits=2, decimal_places=1,blank=True, default=1 )

    TYPES_CHOICES = (
    ('vowen','VOWEN'),
    ('knitting', 'KNITTING'))

    type = models.CharField(max_length=10, choices=TYPES_CHOICES, default='vowen')

    # Status Details
    is_active = models.BooleanField(default=True)
    is_new = models.BooleanField(default=False)
    is_exclusive = models.BooleanField(default=False)
    is_contract = models.BooleanField(default=False)

    # Special Features
    # is_natural = models.BooleanField(default=False)
    # is_fr = models.BooleanField(default=False)
    # is_easyclean = models.BooleanField(default=False)
    # is_recycled = models.BooleanField(default=False)

    # Many To Many Fields
    usages = models.ManyToManyField(Usage, blank=False)
    compositions = models.ManyToManyField(Composition, blank=False)
    features = models.ManyToManyField(Feature, blank=True)
    design_direction = models.ManyToManyField(DesignDirection, blank=True)

    # Physical Tests
    martindale = models.CharField(max_length=50)
    pilling_abrasion = models.CharField(max_length=50)
    seam_slippage = models.CharField(max_length=50)
    tear_strenght = models.CharField(max_length=50)
    tensile_strenght = models.CharField(max_length=50)
    color_fastness = models.CharField(max_length=50)
    light_fastness = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name.capitalize()}"

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        self.name = self.name.lower()
        super().save(*args, **kwargs)
    
    def generate_main_filename(self, filename):
            name = "products/%s/main/%s" % (self.name, filename)
            return name
    
    def generate_style_filename(self, filename):
            name = "products/%s/style/%s" % (self.name, filename)
            return name
    
    def generate_zoom_filename(self, filename):
            name = "products/%s/zoom/%s" % (self.name, filename)
            return name
    
    def generate_filename(self, filename):
        print(f"filename is {filename}")
        name = "products/%s/images/%s" % (self.product.name , filename)
        return name

    # Product Details Images
    main_image = models.ImageField(upload_to=generate_main_filename)
    style_image = models.ImageField(upload_to=generate_style_filename, blank=True, null=True)
    zoom_image = models.ImageField(upload_to=generate_zoom_filename, blank=True, null=True)


class ProductVariantImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    
    def generate_filename(self, filename):
        name = "products/%s/variants/%s" % (self.product.name , filename)
        return name

    image = models.ImageField(upload_to=generate_filename)