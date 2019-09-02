from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Brand(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return u'%s' % self.name

class Category(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	related_categories = models.ManyToManyField('self', blank=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

	def __unicode__(self):
		return u'%s' % self.name

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL) # sets value to null when foreign key is deleted
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)  # doesn't delete when foreign key is deleted
	related_products = models.ManyToManyField('self', blank=True)

	def __str__(self):
		return '%s: %s' % (self.brand, self.name)

	def __unicode__(self):
		return u'%s: %s' % (self.brand, self.name)

class Rating(models.Model):
	id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
	author = models.ForeignKey(User, default='anon', on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add='true')
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

	def __str__(self):
		return '%s: %s' % (self.product, self.rating)

	def __unicode__(self):
		return u'%s: %s' % (self.product, self.rating)

class Review(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	review = models.CharField(max_length=1000)
	pub_date = models.DateTimeField(auto_now_add='true')

	def __str__(self):
		return '%s: %s...' % (self.author, self.review[:15])

	def __unicode__(self):
		return u'%s: %s...' % (self.author, self.review[:15]) 



