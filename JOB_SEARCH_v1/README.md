# Job Finder Agent (Semantic Job Search)

A lightweight **Python-based Job Finder Agent** that automatically finds jobs matching your resume.

The system:

1. Reads your **resume (PDF/DOCX)**
2. Uses an **LLM to extract job search keywords**
3. Fetches jobs from multiple platforms using **python-jobspy**
4. Performs **semantic similarity ranking using embeddings**
5. Exports ranked job results into a **CSV file**

This project is designed to be **simple, modular, and extensible**, making it easy to evolve into a full job-search automation agent.

---

# Features

* Resume parsing (PDF / DOCX)
* LLM-based keyword extraction
* Multi-site job scraping
* Semantic search using sentence embeddings
* CSV export of ranked job matches
* Clean modular architecture
* Works **without GPU**

---

# Project Structure

```
job_finder/

main.py
resume_reader.py
keyword_extractor_llm.py
job_fetcher.py
job_ranker.py

requirements.txt
.env
README.md
```

---

# How It Works

Pipeline:

```
Resume File
   ↓
LLM Keyword Extraction
   ↓
JobSpy Job Scraper
   ↓
Semantic Embedding Search
   ↓
Similarity Ranking
   ↓
CSV Output
```

---

# Installation

## 1. Clone the repository

```
git clone https://github.com/yourusername/job-finder-agent.git
cd job-finder-agent
```

---

## 2. Create Virtual Environment

```
python -m venv .venv
```

Activate it.

### Windows (PowerShell)

```
.venv\Scripts\activate
```

### Mac / Linux

```
source .venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_api_key_here
```

This API key is used for **LLM-based keyword extraction**.

---

# Usage

Place your resume in the project directory.

Example:

```
resume.pdf
```

Edit the path in `main.py` if needed:

```python
resume_path = "resume.pdf"
```

Run the pipeline:

```
python main.py
```

---

# Output

The script generates:

```
ranked_jobs.csv
```

Example output:

```
title,company,location,score,job_url
Machine Learning Engineer,Amazon,Bangalore,0.83,https://...
AI Engineer,Microsoft,Hyderabad,0.80,https://...
Data Scientist,Uber,Bangalore,0.78,https://...
```

Jobs are ranked using **semantic similarity to the resume**.

---

# Technologies Used

* Python
* sentence-transformers
* python-jobspy
* Groq LLM API
* pandas
* scikit-learn

---

# Future Improvements

Possible upgrades for this system:

* LLM-generated multi-query job searches
* Job deduplication across platforms
* Automated job application agent
* Resume-job skill gap analysis
* Web dashboard for browsing results
* Scheduled daily job search

---

# License

MIT License
