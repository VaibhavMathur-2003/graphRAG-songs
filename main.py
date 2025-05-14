import streamlit as st
from dotenv import load_dotenv

from graph_utils import get_graph
from llm_utils import load_llm, get_cypher_qa_chain, generate_lyrics

load_dotenv()
graph = get_graph()
llm = load_llm()
qa_chain = get_cypher_qa_chain(llm, graph)

st.set_page_config(page_title="Lyrics & Music Knowledge", layout="wide")
tab1, tab2 = st.tabs(["Chat with Database", "Lyrics Generator"])

with tab1:
    st.title("🎤 Chat with Music Database")
    user_query = st.text_input("Ask about artists, songs, lyrics...", "")
    if user_query:
        response = qa_chain.invoke({"query": user_query})
        st.markdown("**Answer:**")
        st.write(response["result"])

with tab2:
    st.title("🎼 Generate Song Lyrics in Artist's Style")

    
    artist_result = qa_chain.invoke({"query": "List all artists in the database."})
    artists = [a.strip() for a in artist_result["result"].split(",") if a.strip()]
    selected_artist = st.selectbox("Select your favorite artist:", options=artists)

    if selected_artist:
        query = f"""
        MATCH (a:Artist {{name: '{selected_artist}'}})-[:SANG]->(s:Song)
        RETURN s.lyrics_snippet AS snippet
        """
        results = graph.query(query)
        snippets = [record['snippet'] for record in results if record['snippet']]

        if st.button("Generate New Song Lyrics"):
            if snippets:
                lyrics = generate_lyrics(llm, selected_artist, snippets)
                st.subheader("🎶 Generated Lyrics:")
                st.write(lyrics)
            else:
                st.warning("No lyrics found for this artist.")
