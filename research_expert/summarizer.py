
from utils.gemini import model


def summarize_paper(paper):

    prompt = f""" You are a research assistant.
    Summarize the following research paper.
        
    Title: {paper['title']}
    Abstract: {paper['abstract']}
        
    Write the summary in:
    - 5 to 7 bullet points
    - Simple English
    - Mention the main contribution
    - Mention possible applications """

    try:
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    from research_expert.paper_search import search_papers
    papers = search_papers(input("Search Paper: "))

    if papers:
        summary = summarize_paper(papers[0])
        print("\nSummary\n")
        print(summary)

    else:
        print("Paper not found.")
