import src.chat.keys
from src.chat.index import get_conversational_chain
from src.chat.cache import get_from_cache, add_to_cache
from src.chat.vectorstore import get_vectorstore


def user_input(class_name, user_question):

    cached_response = get_from_cache(class_name, user_question)
    if cached_response:
        return cached_response

    vector_store = get_vectorstore(class_name)

    docs = vector_store.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question}
        , return_only_outputs=True)

    add_to_cache(class_name, user_question, response)

    return response
