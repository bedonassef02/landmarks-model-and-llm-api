import os
import logging
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from src.chat.index import model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ConversationalChainManager:
    def __init__(self, prompt_template=None):
        """
        Initialize the ConversationalChainManager with a prompt template.

        :param prompt_template: Optional custom prompt template. Defaults to a template about Egypt landmarks.
        """
        default_prompt_template = """
        You are an expert in Egypt landmarks, monuments, and history.
        Answer the question as fully detailed as possible from the provided context. \n\n
        Context:\n {context}\n
        Question: \n{question}\n

        Answer:
        """
        self.prompt_template = prompt_template or default_prompt_template
        self.prompt = PromptTemplate(template=self.prompt_template, input_variables=["context", "question"])
        logger.info("ConversationalChainManager initialized with prompt template")

    def get_conversational_chain(self):
        """
        Load and return a conversational chain.

        :return: The conversational chain object.
        """
        try:
            chain = load_qa_chain(model, chain_type="stuff", prompt=self.prompt)
            logger.info("Conversational chain loaded successfully")
            return chain
        except Exception as e:
            logger.error(f"Error loading conversational chain: {e}")
            raise

def embeddings_exist(path):
    """
    Check if embeddings exist at the specified path.

    :param path: The path to check.
    :return: True if the path exists, False otherwise.
    """
    exists = os.path.exists(path)
    logger.info(f"Embeddings exist at '{path}': {exists}")
    return exists
