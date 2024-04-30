# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


# model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)