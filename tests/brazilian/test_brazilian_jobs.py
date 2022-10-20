from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for element in brazilian_jobs:
        assert ('title' in element) is True
        assert ('salary' in element) is True
        assert ('type' in element) is True
