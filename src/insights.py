from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    job_type_set = set()
    for job in jobs_list:
        job_type_set.add(job["job_type"])
    return list(job_type_set)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_list_by_type = [job for job in jobs if job["job_type"] == job_type]

    return jobs_list_by_type


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    industries_set = set()

    for job in jobs_list:
        industries_set.add(job["industry"])

    industries_list = list(industries_set)
    return [industry for industry in industries_list if industry != ""]


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    jobs_list_by_industry = [
        job for job in jobs if job["industry"] == industry
    ]

    return jobs_list_by_industry


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salary_list = [
        int(job["max_salary"], 10)
        for job in jobs_list
        if job["max_salary"].isnumeric()
    ]

    return max(salary_list)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)

    salary_list = [
        int(job["min_salary"], 10)
        for job in jobs_list
        if job["min_salary"].isnumeric()
    ]
    return min(salary_list)


def is_invalid_matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        return True

    if not (type(job["min_salary"]) is int and type(job["max_salary"]) is int):
        return True

    if job["min_salary"] > job["max_salary"]:
        return True

    if not type(salary) is int:
        return True

    return False


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if is_invalid_matches_salary_range(job, salary):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def is_valid_filter_by_salary_range(job, salary):
    return (
        type(salary) is int and
        job["min_salary"] <= job["max_salary"] and
        matches_salary_range(job, salary)
    )


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filter_jobs = [
        job
        for job in jobs
        if type(job["min_salary"]) is int and type(job["max_salary"]) is int
    ]

    filter_jobs_by_salary = [
        job
        for job in filter_jobs
        if is_valid_filter_by_salary_range(job, salary)
    ]

    return filter_jobs_by_salary
