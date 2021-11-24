from requests import get
from json import loads


class APIController:
    BASE_URL = 'http://challenge.dienekes.com.br/api/numbers?page={}'
    MIN_PAGE = 1
    MAX_PAGE = 10000

    def check_if_valid_page_type(self, page):
        type_validation = type(page) == int
        return type_validation

    def check_if_valid_page_number(self, page):
        page_validation = page >= self.MIN_PAGE and page <= self.MAX_PAGE
        return page_validation

    def get_page_from_challenge_api(self, page):
        page_type_validation = self.check_if_valid_page_type(page)
        if not page_type_validation:
            return None

        page_number_validation = self.check_if_valid_page_number(page)
        if not page_number_validation:
            return None

        html_content = get(self.BASE_URL.format(page)).content
        result = loads(html_content.decode('utf8'))

        return result

    def get_all_page_numbers_as_array(self):
        number_list = []

        for page in range(1, 5):
            result = self.get_page_from_challenge_api(page)
            page_numbers = result.get('numbers')

            if page_numbers:
                number_list.extend(page_numbers)

        return number_list
