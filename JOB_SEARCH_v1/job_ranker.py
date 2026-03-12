import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def rank_jobs(resume_text: str, jobs_df: pd.DataFrame):

    if jobs_df.empty:
        return jobs_df

    jobs_df = jobs_df.copy()

    jobs_df["description"] = jobs_df["description"].fillna("")

    job_descriptions = jobs_df["description"].tolist()

    # Create embeddings
    resume_embedding = model.encode([resume_text])
    job_embeddings = model.encode(job_descriptions)

    # Compute similarity
    similarities = cosine_similarity(resume_embedding, job_embeddings)[0]

    jobs_df["score"] = similarities

    ranked_jobs = jobs_df.sort_values(by="score", ascending=False)

    return ranked_jobs