from unittest import TestCase
from merge_sort import sort_array_by_merge_sort

class MergeSortTestCase(TestCase):
    def test_should_sort_array_correctly(self):
        arr = [25, 40, 50, 90, 10]
        sorted_arr = sort_array_by_merge_sort(arr)

        self.assertEqual(sorted_arr, sorted(arr))
    
    def test_should_not_sort_incorrectly(self):
        arr = [25, 40, 50, 90, 10]
        sorted_arr = sort_array_by_merge_sort(arr)

        self.assertFalse(sorted_arr != sorted(arr))

    def test_should_throw_error_if_invalid_array(self):
        arr = [25, 40, 50, 90, 10, "string"]

        with self.assertRaises(Exception):
            _ = sort_array_by_merge_sort(arr)
        
