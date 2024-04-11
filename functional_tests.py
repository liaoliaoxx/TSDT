from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome('D:/develop/chromedriver.exe')
	
	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element(By.ID,'id_list_table')
		rows = table.find_elements(By.TAG_NAME,'tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# 张三听说有一个在线待办事项的应用
		# 他去看了这个应用的首页
		self.browser.get('http://localhost:8000')

		# 他注意到网页里包含"To-Do"这个词
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element(By.TAG_NAME,'h1').text
		self.assertIn('To-Do',header_text)

		# inputbox = self.browser.find_element(By.ID,'id_new_item')
		# inputbox.send_keys('Buy flowers')
		# inputbox.send_keys(Keys.ENTER)
		# time.sleep(1)
		# self.check_for_row_in_list_table('1: Buy flowers')

		inputbox = self.browser.find_element(By.ID,'id_new_item')
		inputbox.send_keys('Give a gift to Lisi')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_for_row_in_list_table('1: Buy flowers')
		self.check_for_row_in_list_table('2: Give a gift to Lisi')

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()
