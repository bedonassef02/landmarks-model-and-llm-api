from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from src.chat.index import embeddings_exist
from langchain_openai import OpenAIEmbeddings

# embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
def get_vectorstore(class_name):
    path = f"embeddings/{class_name}_faiss_index"
    if embeddings_exist(path):
        return FAISS.load_local(path, embeddings)

    loader = DirectoryLoader('./texts', glob="*" + class_name + "*/*.txt")
    raw_text = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=256)
    documents = text_splitter.split_documents(raw_text)

    vector_store = FAISS.from_documents(documents, embedding=embeddings)
    vector_store.save_local(path)

    return vector_store