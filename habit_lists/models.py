from django.db import models

class Habit(models.Model):
	text = models.TextField(default='')
