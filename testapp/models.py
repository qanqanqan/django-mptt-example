from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
	name = models.CharField(max_length=150, unique=True)
	parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('node', kwargs={'pk': self.pk})


class Node(models.Model):
	name = models.CharField(max_length=150)
	parent = TreeForeignKey(Category, on_delete=models.PROTECT)

	def __str__(self):
		return self.name
