from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from src.chat.managers.conversational_chain_manager import embeddings_exist
from langchain_openai import OpenAIEmbeddings
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

class VectorStoreManager:
    def __init__(self):
        self.openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
        # self.google_embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.loader = DirectoryLoader('./texts')
        self.text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=256)

    def get_vectorstore_for_class(self, class_name):
        """Retrieves or creates a vector store for a specific class."""
        path = f"embeddings/{class_name}_faiss_index"
        if embeddings_exist(path):
            return FAISS.load_local(path, self.openai_embeddings, allow_dangerous_deserialization=True)
        # Load raw text
        self.loader = DirectoryLoader('./texts', glob="*" + class_name + "*/*.txt")
        raw_text = self.loader.load()

        # Split documents
        documents = self.text_splitter.split_documents(raw_text)

        # Create and save vector store
        vector_store = FAISS.from_documents(documents, embedding=self.openai_embeddings)
        vector_store.save_local(path)

        return vector_store

    def get_vectorstore_for_all(self):
        """Retrieves or creates a vector store for all classes."""
        path = f"faiss_index"
        if embeddings_exist(path):
            return FAISS.load_local(path, self.openai_embeddings, allow_dangerous_deserialization=True)

        # Load raw text for all classes
        self.loader = DirectoryLoader('./texts', glob="**/*.txt")
        raw_text = self.loader.load()

        # Split documents
        documents = self.text_splitter.split_documents(raw_text)

        # Create and save vector store
        vector_store = FAISS.from_documents(documents, embedding=self.openai_embeddings)
        vector_store.save_local(path)

        return vector_store
