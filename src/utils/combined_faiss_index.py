import os
from langchain_community.vectorstores import FAISS
from src.chat.managers.conversational_chain_manager import embeddings_exist
from langchain_openai import OpenAIEmbeddings

from src.chat.managers.vector_store_manager import VectorStoreManager

vectorStoreManager = VectorStoreManager()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def combine_and_save_all_vector_stores():
    path = f"combined_faiss_index"
    if embeddings_exist(path):
        return

    vectorstores = os.listdir('embeddings')
    v1 = FAISS.load_local("embeddings/" + vectorstores[0], embeddings, allow_dangerous_deserialization=True)
    for path in vectorstores[1:]:
        v2 = FAISS.load_local("embeddings/" + path, embeddings, allow_dangerous_deserialization=True)
        v1.merge_from(v2)

    v1.save_local(f'combined_faiss_index')
    print('Combine Vectorstore Done')


combine_and_save_all_vector_stores()
