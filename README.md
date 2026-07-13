
# 🤖 GenAI Multi-Domain Chatbot

A Streamlit chatbot that routes each user message to the right specialist module based on
intent: medical Q&A, a custom knowledge base, research paper search, multimodal file
analysis, sentiment detection, and multilingual replies — all backed by Google's Gemini model.

The chatbot automatically classifies each user query and routes it to the most appropriate 
AI module without requiring the user to manually select a mode.

## Features

- **Medical Q&A** — answers health questions using the MedQuAD dataset (FAISS + sentence
  embeddings) combined with the knowledge base for extra context.
- **Knowledge Base** — build your own searchable knowledge base from uploaded files
  (PDF, DOCX, TXT, CSV, XLSX, images), websites, or YouTube videos.
- **Research Expert** — searches a local arXiv CS-papers dataset and can summarize or
  explain a paper in plain English.
- **Multimodal Chat** — upload a document, spreadsheet, or image and ask questions about it.
- **Sentiment Detection** — detects positive / negative / neutral tone in a message.
- **Multilingual Support** — auto-detects the message language and replies in the same
  language (English, Hindi, Tamil, Telugu, Kannada, Malayalam, French, German, Spanish,
  Italian, Japanese, Korean, Chinese).

Intent is decided automatically by `router/query_classifier.py` — no need to pick a mode
manually.

## Project Structure

genAi_chatbot/
├── app.py                   # Streamlit UI and entry point
├── router/                  # Classifies intent and routes to the right module
├── medical_chatbot/         # Medical Q&A (MedQuAD + FAISS)
├── knowledge_base/          # Custom knowledge base (files / websites / YouTube)
├── research_expert/         # arXiv paper search, summaries, explanations
├── multimodal/              # Document / spreadsheet / image understanding
├── multilingual/            # Language detection + translated replies
├── sentiment/               # Sentiment analysis
├── utils/                   # Shared config, logger, chat memory, Gemini client
├── data/                    # Datasets, uploads, chat history (see below)
├── vector_db/               # Generated FAISS indexes (not committed)
└── requirements.txt

## Setup

### 1. Clone and create a virtual environment

```bash
git clone https://github.com/Ashish5407/GenAI-MultiDomain-Chatbot.git
cd GenAI-MultiDomain-Chatbot
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Gemini API key

Copy `.env.example` to `.env` and add your key (get a free one at
[aistudio.google.com/apikey](https://aistudio.google.com/apikey)):

GOOGLE_API_KEY=your-google-api-key-here

> **Never commit your real `.env` file** — it's already excluded via `.gitignore`.

### 4. Add the datasets

These are not committed to the repo (too large for git) — download them once and place
them here:

- **Medical Q&A** — the [MedQuAD dataset](https://github.com/abachaa/MedQuAD) →
  extract into `data/MedQuAD/` (keeping the original sub-folder structure of `.xml` files).
- **Research papers** — a JSON-Lines file of arXiv CS paper metadata (`title`, `abstract`,
  `categories` per line) → save as `data/arxiv/cs_papers.json`.

### 5. Build the medical vector database (one-time)

```bash
python -m medical_chatbot.embeddings
```

This reads `data/MedQuAD/`, creates embeddings, and saves the FAISS index to
`vector_db/medical_db/`. The knowledge base index (`vector_db/knowledge_db/`) is created
automatically the first time you upload a file or URL from the app's sidebar.

### 6. Run the app

```bash
streamlit run app.py
```

## Logs

Application logs are written to `data/logs/chatbot.log` (created automatically, ignored
by git).

## License

Distributed under the MIT License — see [`LICENSE`](LICENSE) for details.