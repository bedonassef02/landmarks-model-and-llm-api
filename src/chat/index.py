import os
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from src.chat.model import model

def get_conversational_chain():
    prompt_template = """
    Answer the question as full detailed as possible from the provided context \n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def embeddings_exist(path):
    return os.path.exists(f"{path}")