
from utils.gemini import model


def explain_paper(paper):

    prompt = f""" You are an expert Computer Science teacher.
    Explain the following research paper to a beginner.
    
    Title: {paper['title']}
    Abstract: {paper['abstract']}
    
    Explain using:
    1. What problem does this paper solve?
    2. How does the proposed method work?
    3. Why is it important?
    4. Real-world applications.
    5. Explain in simple English without complex research terms. """

    try:
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    from research_expert.paper_search import search_papers
    papers = search_papers(input("Search Paper: "))

    if papers:
        explanation = explain_paper(papers[0])
        print("\nExplanation\n")
        print(explanation)

    else:
        print("Paper not found.")
