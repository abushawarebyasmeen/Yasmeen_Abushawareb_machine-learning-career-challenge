from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

def query_groq(query):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model="mixtral-8x7b-32768",  # Model adı güncel, istersen değiştirilebilir
            temperature=0.2  # Tutarlı ve kontrollü yanıt için düşük sıcaklık
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Groq API Error: {e}")
        return "Bir hata oluştu, lütfen tekrar deneyin."