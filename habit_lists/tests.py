from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.template.loader import render_to_string

from habit_lists.models import Habit, HabitList
from habit_lists.views import home_page

class HomePageTest(TestCase):
	
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class HabitAndHabitListModelTest(TestCase):

	def test_saving_and_retrieving_habits(self):
		habit_list_ = HabitList()
		habit_list_.save()

		first_habit = Habit()
		first_habit.text = 'The first habit'
		first_habit.habit_list = habit_list_
		first_habit.save()

		second_habit = Habit()
		second_habit.text = 'The second habit'
		second_habit.habit_list = habit_list_
		second_habit.save()

		saved_habit_list = HabitList.objects.first()
		self.assertEqual(saved_habit_list, habit_list_)

		saved_habits = Habit.objects.all()
		self.assertEqual(saved_habits.count(), 2)

		first_saved_habit = saved_habits[0]
		second_saved_habit = saved_habits[1]
		self.assertEqual(first_saved_habit.text, 'The first habit')
		self.assertEqual(first_saved_habit.habit_list, habit_list_)
		self.assertEqual(second_saved_habit.text, 'The second habit')
		self.assertEqual(second_saved_habit.habit_list, habit_list_)

class HabitListViewTest(TestCase):

	def test_uses_habit_list_template(self):
		new_habit_list = HabitList.objects.create()
		response = self.client.get('/habit_lists/%d/' % (new_habit_list.id,))
		self.assertTemplateUsed(response, 'habit_list.html')	

class ListViewTest(TestCase):
	
	def test_uses_list_template(self):
		habit_list_ = HabitList.objects.create()
		response = self.client.get('/habit_lists/%d/' % (habit_list_.id,))
		self.assertTemplateUsed(response, 'habit_list.html')
	
	def test_displays_only_habits_for_that_habit_list(self):
		correct_habit_list = HabitList.objects.create()
		Habit.objects.create(text='habit 1', habit_list=correct_habit_list)
		Habit.objects.create(text='habit 2', habit_list=correct_habit_list)
		other_habit_list = HabitList.objects.create()
		Habit.objects.create(text='other habit 1', habit_list=other_habit_list)
		Habit.objects.create(text='other habit 2', habit_list=other_habit_list)

		response = self.client.get('/habit_lists/%d/' % (correct_habit_list.id,))
		
		self.assertContains(response, 'habit 1')
		self.assertContains(response, 'habit 2')
		self.assertNotContains(response, 'other habit 1')
		self.assertNotContains(response, 'other habit 2')
	
	def test_passes_correct_habit_list_to_template(self):
		other_habit_list = HabitList.objects.create()
		correct_habit_list = HabitList.objects.create()
		response = self.client.get('/habit_lists/%d/' % (correct_habit_list.id,))
		self.assertEqual(response.context['habit_list'], correct_habit_list)

class NewListTest(TestCase):

	def test_can_save_a_POST_request_to_an_existing_habit_list(self):
		other_habit_list = HabitList.objects.create()
		correct_habit_list = HabitList.objects.create()

		self.client.post(
			'/habit_lists/%d/add_habit' % (correct_habit_list.id,),
			data={'habit_text': 'A new habit'}
		) 		

		self.assertEqual(Habit.objects.count(), 1)
		new_habit = Habit.objects.first()
		self.assertEqual(new_habit.text, 'A new habit')
		self.assertEqual(new_habit.habit_list, correct_habit_list)

	def test_redirects_to_habit_list_view(self):
		other_habit_list = HabitList.objects.create()
		correct_habit_list = HabitList.objects.create()

		response = self.client.post(
			'/habit_lists/%d/add_habit' % (correct_habit_list.id,),
			data={'habit_text': 'A new habit'}
		) 		

		self.assertRedirects(response, '/habit_lists/%d/' % (correct_habit_list.id,))


