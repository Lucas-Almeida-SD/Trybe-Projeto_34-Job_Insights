from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 1000, "min_salary": 200, "date_posted": "2020-05-10"},
        {"max_salary": 800, "min_salary": 150, "date_posted": "2022-05-10"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "2021-05-10"},
        {"max_salary": None, "min_salary": None, "date_posted": None},
        {"min_salary": 300, "date_posted": None},
    ]

    expected_by_max_salary = [
        {"max_salary": 1000, "min_salary": 200, "date_posted": "2020-05-10"},
        {"max_salary": 800, "min_salary": 150, "date_posted": "2022-05-10"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "2021-05-10"},
        {"max_salary": None, "min_salary": None, "date_posted": None},
        {"min_salary": 300, "date_posted": None},
    ]

    expected_by_min_salary = [
        {"max_salary": 500, "min_salary": 100, "date_posted": "2021-05-10"},
        {"max_salary": 800, "min_salary": 150, "date_posted": "2022-05-10"},
        {"max_salary": 1000, "min_salary": 200, "date_posted": "2020-05-10"},
        {"min_salary": 300, "date_posted": None},
        {"max_salary": None, "min_salary": None, "date_posted": None},
    ]

    expected_by_date_posted = [
        {"max_salary": 800, "min_salary": 150, "date_posted": "2022-05-10"},
        {"max_salary": 500, "min_salary": 100, "date_posted": "2021-05-10"},
        {"max_salary": 1000, "min_salary": 200, "date_posted": "2020-05-10"},
        {"min_salary": 300, "date_posted": None},
        {"max_salary": None, "min_salary": None, "date_posted": None},
    ]

    expectations = [
        ("max_salary", expected_by_max_salary),
        ("min_salary", expected_by_min_salary),
        ("date_posted", expected_by_date_posted),
    ]

    for expectation in expectations:
        sort_by(jobs, expectation[0])
        assert jobs == expectation[1]
