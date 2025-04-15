from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model=ChatGoogleGenerativeAI(
     model="gemini-1.5-flash",
     google_api_key=api_key
)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.apple.com/in-edu/shop/buy-mac/macbook-air/15-inch'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(len(docs))
print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))