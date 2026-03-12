from resume_reader import read_resume
from keyword_extractor_llm import extract_keywords_llm
from job_fetcher import fetch_jobs
from job_ranker import rank_jobs


OUTPUT_FILE = "ranked_jobs.csv"


def main():

    resume_path = "himanshu_resume.pdf"

    print("Reading resume...")
    resume_text = read_resume(resume_path)

    print("Extracting keywords using LLM...")
    keywords = extract_keywords_llm(resume_text)

    if not keywords:
        print("No keywords extracted.")
        return

    print("\nExtracted Keywords:")
    print(keywords)

    search_term = " ".join(keywords[:4])

    print("\nSearching jobs for:", search_term)

    jobs = fetch_jobs(search_term)

    if jobs.empty:
        print("No jobs found.")
        return

    print("Ranking jobs using semantic similarity...")

    ranked_jobs = rank_jobs(resume_text, jobs)

    columns = [
        "title",
        "company",
        "location",
        "date_posted",
        "score",
        "job_url"
    ]

    available_cols = [c for c in columns if c in ranked_jobs.columns]

    ranked_jobs[available_cols].to_csv(OUTPUT_FILE, index=False)

    print("\nTop Job Matches:\n")

    print(ranked_jobs[available_cols].head(10))

    print(f"\nCSV saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()