from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from audio import generate_audio_from_text

load_dotenv()

# Initialize LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Prompt template
prompt = ChatPromptTemplate.from_template(
"""
You are a friendly NCERT teacher for Class 9–10 students.

Step 1: Detect the language style used by the student.

Language rules:
- Tamil words in English letters → Tanglish

Step 2: Reply in the SAME language style.

Use simple explanations with examples.

Question:
{question}

Explain clearly.
"""
)

# Output parser
parser = StrOutputParser()

# Pipeline
chain = prompt | llm | parser

# Ask question
response = chain.invoke({
    "question": "muje capacitor vyaakhya karana"
})

# Convert response to audio
audio_file = generate_audio_from_text(response)

print(response)
print("Audio saved at:", audio_file)