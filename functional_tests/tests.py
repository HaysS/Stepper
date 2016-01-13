from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_habit_list_table(self, row_text):
		habit_list_table = self.browser.find_element_by_id('habit_list_table')
		habit_list_rows = habit_list_table.find_elements_by_tag_name('tr')
		self.assertIn(
			row_text, 
			[row.text for row in habit_list_rows]
		)
		
	def test_allows_user_to_enter_multiple_habits(self):
		self.browser.get(self.live_server_url)
		
		self.assertIn('Stepper', self.browser.title)
		
		#User enters "Brush teeth" as a new habit.
		new_habit_elem = self.browser.find_element_by_id('new_habit')
		new_habit_elem.send_keys('Brush teeth')
		new_habit_elem.send_keys(Keys.ENTER)
		
		first_habit_list_url = self.browser.current_url
		self.assertRegex(first_habit_list_url, '/habit_lists/.+')
		self.check_for_row_in_list_table('Brush teeth')

		#User enters "Go to bed early" as a new habit.
		new_habit_elem = self.browser.find_element_by_id('new_habit')
		new_habit_elem.send_keys('Go to bed early')
		new_habit_elem.send_keys(Keys.ENTER)

		#Check to see if the user entries are in table.
		self.check_for_row_in_habit_list_table('Brush teeth')
		self.check_for_row_in_habit_list_table('Go to bed early')

		#The first user quits, and then the second user opens
		#the site.
		self.browser.quit()
		self.browser = webdriver.Firefox()
		self.browser.get(self.live_server_url)
		
		#Check to make sure the first users data is not presented
		#to the second user.
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Brush teeth', page_text)
		self.assertNotIn('Go to bed early', page_text)

		#Second user enters "Read for 20 minutes" as a new habit.
		new_habit_elem = self.browser.find_element_by_id('new_habit')
		new_habit_elem.send_keys('Read for 20 minutes')
		new_habit_elem.send_keys(Keys.ENTER)

		#Make sure second user gets a unique url.
		second_habit_list_url = self.browser.current_url
		self.assertRegex(second_habit_list_url, '/habit_lists/.+')
		self.assertNotEqual(second_habit_list_url, first_habit_list_url)



