from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Flash Model (convert_system_message_to_human handles SystemMessage if needed)
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key,
    convert_system_message_to_human=True
)

# Initialize chat history
chat_history = [
    HumanMessage(content='You are a helpful AI assistant.') 
]

# Chat Loop
while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        break
    # now human message is labelled
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    
    # now ai message is labelled
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)
