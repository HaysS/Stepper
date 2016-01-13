from django.db import models

class HabitList(models.Model):
	pass


class Habit(models.Model):
	text = models.TextField(default='')
	habit_list = models.ForeignKey(HabitList, default=None)
