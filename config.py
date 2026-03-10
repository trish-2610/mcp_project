## This file loads the LLM 
import os
from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
load_dotenv()

def get_model():
    """This function returns the LLM"""
    try : 
        model = ChatGroq(
            model = "llama-3.1-8b-instant",
            api_key = os.getenv("GROQ_API_KEY"),
            temperature = 0
        )
        return model
    except Exception as e :
        print(f"Error loading model : {str(e)}")