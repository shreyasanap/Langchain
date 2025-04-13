from langchain_community.document_loaders import TextLoader
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

prompt=PromptTemplate(
    template="Summarize this poem:\n{poem}",
    input_variables=['poem']
)

parser=StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()
print(len(docs))
chain=prompt | model | parser
print(chain.invoke({'poem':docs[0].page_content}))