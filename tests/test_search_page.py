from pages.search_page import SearchPage
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


class TestSearchPage(BaseTest):

    def test_search_question(self):
        # Step01: Navigate to Help Page
        page = MainPage(self.driver)
        searchPage = page.navigate_course_page()

        # Step02: Enter 'Kiến Thức Nhập Môn IT' into search text box
        searchPage.enter_search_question('Kiến Thức Nhập Môn IT')

        # Step03: Verify the return result
        searchText = searchPage.get_text_result()
        print('Result', searchText)
        self.assertIsNotNone(searchText)
