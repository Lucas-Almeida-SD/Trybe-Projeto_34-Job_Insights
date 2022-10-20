from src.counter import count_ocurrences


def test_counter():
    path = 'src/jobs.csv'
    word = 'Marketing'
    counter = count_ocurrences(path, word)
    assert counter == 1259
