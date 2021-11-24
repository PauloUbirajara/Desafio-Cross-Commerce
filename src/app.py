from flask import Flask
from api_controller import APIController
from merge_sort import sort_array_by_merge_sort

app = Flask(__name__)
controller = APIController()


@app.route("/api")
def show_sorted_data():
    number_list = controller.get_all_page_numbers_as_array()
    sorted_number_list = sort_array_by_merge_sort(number_list)

    result = {
        'numbers': sorted_number_list
    }

    return result
