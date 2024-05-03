import os
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from src.chat.index import model


class ConversationalChainManager:
    def __init__(self):
        self.prompt_template = """
        You are an expert in Egypt landmarks, monuments, and history.
        Answer the question as full detailed as possible from the provided context \n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """
        self.prompt = PromptTemplate(template=self.prompt_template, input_variables=["context", "question"])

    def get_conversational_chain(self):
        """Loads and returns a conversational chain."""
        chain = load_qa_chain(model, chain_type="stuff", prompt=self.prompt)
        return chain


def embeddings_exist(path):
    return os.path.exists(f"{path}")
