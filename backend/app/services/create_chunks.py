def create_chunks(text: str, max_tokens: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []

    i = 0
    while i < len(words):
        chunk = words[i : i + max_tokens]
        chunks.append(" ".join(chunk))
        i += max_tokens - overlap

    return chunks
