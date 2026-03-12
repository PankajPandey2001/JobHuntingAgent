import pandas as pd
from jobspy import scrape_jobs


def fetch_jobs(search_term: str, location: str = "India", results: int = 50):

    jobs = scrape_jobs(
        site_name=["indeed", "glassdoor"],
        search_term=search_term,
        location=location,
        results_wanted=results,
        hours_old=72,
        country_indeed="India"
    )

    df = pd.DataFrame(jobs)

    return df