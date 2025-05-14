import os
from langchain_groq import ChatGroq
from langchain.chains import GraphCypherQAChain

def load_llm():
    return ChatGroq(groq_api_key=os.environ["GROQ_API_KEY"], model_name="Gemma2-9b-It")

def get_cypher_qa_chain(llm, graph):
    return GraphCypherQAChain.from_llm(llm=llm, graph=graph, verbose=True, allow_dangerous_requests=True)

def generate_lyrics(llm, artist, snippets):
    combined_snippets = "\n".join(snippets[:10])
    prompt = f"""Here are some lyrics from songs by {artist}:\n\n{combined_snippets}\n\nBased on these, generate new song lyrics in a similar style."""
    response = llm.invoke(prompt)
    return response.content
