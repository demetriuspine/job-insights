from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('src/jobs.csv', 'year') == 5431
    assert count_ocurrences('src/jobs.csv', 'Year') == 5431
    assert count_ocurrences('src/jobs.csv', 'demetrius') == 0


