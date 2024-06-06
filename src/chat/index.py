# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


# model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=1)
model = ChatOpenAI(model="gpt-4o", temperature=1)