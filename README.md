# 🎶 Graph-RAG Based Lyrics Generator

An AI-powered interactive app combining a **graph database** and **LLM** to:
- 🔍 Chat with a music knowledge graph (artists, songs, lyrics)
- 🎼 Generate new lyrics based on a selected artist's style

Built with **Streamlit**, **Neo4j**, **LangChain**, and **Groq's Gemma2-9b-It** LLM.

---

## 🗂️ Project Structure

- ├── main.py # Streamlit app (UI)
- ├── graph_utils.py # Neo4j setup & data insertion
- ├── llm_utils.py # LLM loading & lyric generation
- ├── .env # Environment variables
- ├── requirements.txt
- ├── README.md
- └── data/
  - spotify_millsongdata.csv
  - songs_preprocessed_data.csv


---

## 🚀 Features

### 🔍 Chat with Music Knowledge Graph
Ask questions like:
- “Which songs did Westlife sing?”
- “Show me lyrics from the song ‘Forever’”
- “List all artists in the database”

### 🎵 Generate Lyrics in Artist's Style
- Select a favorite artist from the graph
- Retrieve real lyrics snippets
- Generate new lyrics using an LLM in their style

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/VaibhavMathur-2003/graphRAG-songs
cd graph-RAG-songs

pip install -r requirements.txt
```

### Create a .env file with the following content:
- GROQ_API_KEY=your_groq_api_key
- NEO4J_URI=bolt://localhost:7687
- NEO4J_USERNAME=neo4j
- NEO4J_PASSWORD=your_password

### Create graph using your csv
```bash
python graph_utils.py
```

## Run the App
```bash
streamlit run main.py

```
