
import json
import re
from utils.config import ARXIV_DIR

DATASET_PATH = ARXIV_DIR / "cs_papers.json"

PAPERS = None

STOP_WORDS = {
    "a", "an", "the", "is", "are", "of",
    "to", "in", "for", "and", "on",
    "with", "what", "how"
}

def load_papers():
    papers = []

    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        for line in file:
            papers.append(json.loads(line))

    return papers

def get_papers():
    global PAPERS
    
    if PAPERS is None:
        PAPERS = load_papers()
        
    return PAPERS


def search_papers(query, top_k=5):
    
    query = query.strip()

    if not query:
        return []
    
    query_words = re.findall(r"\w+", query.lower())
    results = []

    for paper in get_papers():

        original_title = paper.get("title", "")
        title = original_title.lower()
        abstract = paper.get("abstract", "").lower()
        categories = paper.get("categories", "").lower()

        title_words = set(re.findall(r"\w+", title))
        abstract_words = set(re.findall(r"\w+", abstract))
        category_words = set(re.findall(r"\w+", categories))
        
        score = 0
        
        query_text = " ".join(query_words)

        if query_text in title:
            score += 8
        
        if query_text in abstract:
            score += 5
        
        for word in query_words:
        
            if word in STOP_WORDS or len(word) <= 2:
                continue
        
            if word in title_words:
                score += 5
            elif word in title:
                score += 2
        
            if word in abstract_words:
                score += 3
            elif word in abstract:
                score += 1
        
            if word in category_words:
                score += 2

        if score > 0:
            results.append((score, paper))

    results.sort(key=lambda x: x[0], reverse=True)

    searched_papers = []
    seen_titles = set()

    for _, paper in results:
        
        title = paper.get("title", "").strip().lower()
        
        if title not in seen_titles:
            searched_papers.append(paper)
            seen_titles.add(title)

        if len(searched_papers) == top_k:
            break

    return searched_papers


if __name__ == "__main__":
    query = input("Search Papers: ")
    papers = search_papers(query)

    if not papers:
        print("No papers found.")

    else:
        for i, paper in enumerate(papers, 1):
            print(f"\nPaper {i}")
            print(f"Title      : {paper['title']}")
            print(f"Category   : {paper['categories']}")
            print(f"Abstract   : {paper['abstract'][:300]}...")

