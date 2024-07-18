import os
import google.generativeai as genai

def gemini_init():
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
