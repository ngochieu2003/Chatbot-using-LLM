import os
import google.generativeai as genai

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
