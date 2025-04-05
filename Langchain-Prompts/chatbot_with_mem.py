from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Flash model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Chat history to maintain context
chat_history = []

while True:
    user_input = input("You: ")  # Get user input
    if not user_input:  # Exit if input is empty
        break

    # Add user input to chat history
    chat_history.append(f"{user_input}")

    # Create a conversation context by joining all messages
    context = "\n".join(chat_history)

    # Invoke Gemini API with the full conversation
    result = model.invoke(context)

    # Store and display model response
    bot_response = result.content
    chat_history.append(f"{bot_response}")
    
    print(bot_response)
print(chat_history)
# Issue: We cannot get who is talking what??
# we need dict for tracking 
#  langchain has this inbuilt mechanism of tracking