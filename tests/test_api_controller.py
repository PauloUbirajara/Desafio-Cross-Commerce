from unittest import TestCase
from random import randint
from sys import path
path.append('./../src')
from api_controller import APIController


class APIControllerTestCase(TestCase):
    def check_if_valid_number_list(self, number_list):
        is_number_list_available = number_list is not None
        is_number_list_a_list = type(number_list) == list

        validation = all([is_number_list_available, is_number_list_a_list])

        return validation

    def check_if_valid_result(self, result):
        is_result_available = result is not None
        is_result_dict = type(result) == dict

        validation = all([is_result_available, is_result_dict])

        return validation

    def test_should_retrieve_random_page_content_as_dict(self):
        controller = APIController()

        MIN_RANGE = controller.MIN_PAGE
        MAX_RANGE = controller.MAX_PAGE

        page = randint(MIN_RANGE, MAX_RANGE)

        result = controller.get_page_from_challenge_api(page)
        result_validation = self.check_if_valid_result(result)

        self.assertTrue(result_validation)

    def test_should_not_retrieve_invalid_content_as_dict(self):
        controller = APIController()

        page = "invalid"
        result = controller.get_page_from_challenge_api(page)
        result_validation = self.check_if_valid_result(result)

        self.assertFalse(result_validation)

    def test_should_retrive_n_random_pages_content_as_dict(self):
        controller = APIController()

        MIN_RANGE = controller.MIN_PAGE
        MAX_RANGE = controller.MAX_PAGE

        n = 5
        result_list = []
        for _ in range(n):
            random_page = randint(MIN_RANGE, MAX_RANGE)
            result = controller.get_page_from_challenge_api(random_page)
            is_valid_result = self.check_if_valid_result(result)

            result_list.append(is_valid_result)

        results_validation = all(result_list)

        self.assertTrue(results_validation)

    def test_should_not_return_out_of_range_pages_as_dict(self):
        controller = APIController()

        MIN_RANGE = controller.MIN_PAGE
        MAX_RANGE = controller.MAX_PAGE

        lower_invalid_page = MIN_RANGE - randint(1, 10)
        higher_invalid_page = MAX_RANGE + randint(1, 10)

        invalid_results = [
            controller.get_page_from_challenge_api(lower_invalid_page),
            controller.get_page_from_challenge_api(higher_invalid_page)
        ]

        results_validation = all(map(
            self.check_if_valid_result,
            invalid_results
        ))

        self.assertFalse(results_validation)
