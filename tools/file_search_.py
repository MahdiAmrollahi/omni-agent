from langchain_community.document_loaders import PyPDFLoader, TextLoader, ToMarkdownLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.tools import tool
import os

text_splitter = CharacterTextSplitter(chunk_size=20, chunk_overlap=2, separator="\n")


@tool
def file_search(query: str, folder_path: str = "docs"):
    """Search for a text query inside .txt and .md and .pdf files in a folder.
    
    Args:
        query: The text query to search for.
        folder_path: The path to the folder to search in.
    Returns:
        A list of chunks that contain the query.
    Example:
        file_search("mahdi","docs")
        Returns:
        A list of chunks that contain the query "mahdi".
    """
    
    results = []

    if not os.path.exists(folder_path):
        return {"error": f"Folder '{folder_path}' does not exist"}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt") or filename.endswith(".md") or filename.endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)

            try:
                if filename.endswith(".pdf"):
                    loader = PyPDFLoader(full_path)
                elif filename.endswith(".md") or filename.endswith(".txt"):
                    loader = TextLoader(full_path,encoding="utf-8")
                document = loader.load()
                chunks = text_splitter.split_documents(document,)    
                # print(chunks)
                for chunk in chunks:
                    if query.lower().strip() in chunk.page_content.lower().strip():
                        results.append({"file": filename, "chunk": chunk.page_content,"page": chunk.metadata["page"] if "page" in chunk.metadata else None})
            except Exception as e:
                print(f"Error loading file {filename}: {e}")
    return results
