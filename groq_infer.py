import os
from groq import Groq
from dotenv import load_dotenv

#loading api key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


#prompt to enter for making coverletter
response = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that writes tailored professional cover letters."},
        {"role": "user", "content": "Write a cover letter for a software engineer applying to Google. Make it confident, clear, and short."}
    ]
)

print("\nGenerated Cover Letter:\n")
print(response.choices[0].message.content)
