from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings, DEFAULT_TENANT, DEFAULT_DATABASE

# Initialize Chroma client with on-disk persistence
chroma_client = chromadb.PersistentClient(
    path="/app/data/chroma",
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE,
)

# Create or get the “chunks” collection
collection = chroma_client.get_or_create_collection("chunks")

# Load the embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(file_id: str, chunks: list[str], metadata: dict):
    # 1) Compute embeddings (list of lists)
    embeddings = embedder.encode(chunks, show_progress_bar=True).tolist()

    # 2) Prepare IDs and per-chunk metadata
    ids = [f"{file_id}_{i}" for i in range(len(chunks))]
    metadatas = []
    for idx in range(len(chunks)):
        m = {"file_id": file_id, "chunk_index": idx}
        m.update(metadata)
        metadatas.append(m)

    # 3) Add to Chroma
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )
