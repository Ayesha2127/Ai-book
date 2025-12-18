from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Chunk:
    page_content: str
    metadata: Dict[str, str]


def get_docs_path() -> Path:
    """
    Resolve the absolute path to `my-ai-book/docs` from the repo root.
    Assumes this script lives in `/backend/indexing_script.py`.
    """
    backend_dir = Path(__file__).resolve().parent
    repo_root = backend_dir.parent
    docs_dir = repo_root / "my-ai-book" / "docs"
    return docs_dir


def split_text_into_chunks(text: str, source_path: Path, chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Chunk]:
    """
    Simple character-based chunking with overlap.
    """
    chunks: List[Chunk] = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk_text = text[start:end]
        metadata = {
            "source": str(source_path),
            "start_index": str(start),
        }
        chunks.append(Chunk(page_content=chunk_text, metadata=metadata))

        if end == text_length:
            break

        start = end - chunk_overlap

    return chunks


def load_and_chunk_documents(docs_path: Path | None = None) -> List[Chunk]:
    """
    Loads markdown documents from the specified path and chunks them.
    """
    if docs_path is None:
        docs_path = get_docs_path()

    print(f"Loading markdown files from: {docs_path}")
    all_chunks: List[Chunk] = []

    if not docs_path.exists():
        print(f"Docs path does not exist: {docs_path}")
        return all_chunks

    for md_path in docs_path.rglob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = md_path.read_text(encoding="utf-8", errors="ignore")

        file_chunks = split_text_into_chunks(text, md_path)
        all_chunks.extend(file_chunks)

    return all_chunks


if __name__ == "__main__":
    print("Loading and chunking documents...")
    chunks = load_and_chunk_documents()
    print(f"Created {len(chunks)} chunks.")
    if chunks:
        print("First chunk example:")
        print(chunks[0].page_content)
        print(f"Source: {chunks[0].metadata['source']}")
        print(f"Start Index: {chunks[0].metadata['start_index']}")
