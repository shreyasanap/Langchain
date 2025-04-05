from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Flash model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

while True:
    user_input = input("You: ")  # Get user input
    if not user_input:  # Exit loop if input is empty
        break

    result = model.invoke(user_input)  # Invoke Gemini API
    print("Bot:", result.content)  # Print response
