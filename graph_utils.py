import os
import pandas as pd
from langchain_community.graphs import Neo4jGraph

def get_graph():
    return Neo4jGraph(
        url=os.environ["NEO4J_URI"],
        username=os.environ["NEO4J_USERNAME"],
        password=os.environ["NEO4J_PASSWORD"],
    )

def insert_song_data(graph, csv_path: str, limit: int = 10000):
    df = pd.read_csv(csv_path).head(limit)
    for _, row in df.iterrows():
        artist = str(row['artist']).strip().replace("'", "\\'")
        song = str(row['song']).strip().replace("'", "\\'")
        link = str(row['link']).strip().replace("'", "\\'")
        lyrics_snippet = str(row['text'])[:50].strip().replace("'", "\\'") if pd.notnull(row['text']) else ""

        query = f"""
        MERGE (a:Artist {{name: '{artist}'}})
        MERGE (s:Song {{
            title: '{song}',
            link: '{link}',
            lyrics_snippet: '{lyrics_snippet}'
        }})
        MERGE (a)-[:SANG]->(s)
        """
        graph.query(query)
    graph.refresh_schema()
    
# graph=get_graph()
# csv = "songs_processed_data.csv"

# insert_song_data(graph, csv)
