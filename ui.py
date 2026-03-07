import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
from audio import generate_audio_from_text

load_dotenv()

st.set_page_config(page_title="NCERT Hinglish Doubt Bot", page_icon="🤖")

st.title("🤖 NCERT Hinglish Doubt Bot")
st.write("Ask your Science / Maths doubts in Hinglish or Tanglish")

# Initialize memory
if "response" not in st.session_state:
    st.session_state.response = None

if "question" not in st.session_state:
    st.session_state.question = None

with open("syllabus.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Initialize LLM
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

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

answer only if question falls under this syllabus 
{text}
else respond that question is out of syllabus
"""
)

parser = StrOutputParser()
chain = prompt | llm | parser


# Chat input
question = st.chat_input("Ask your doubt...")

if question:
    st.session_state.question = question

    response = chain.invoke({
        "question": question,"text":text
    })

    st.session_state.response = response


# Show messages
if st.session_state.question:
    with st.chat_message("user"):
        st.write(st.session_state.question)

if st.session_state.response:
    with st.chat_message("assistant"):

        col1, col2 = st.columns([9,1])

        with col1:
            st.write(st.session_state.response)

        with col2:
            if st.button("🔊"):
                audio_file = generate_audio_from_text(st.session_state.response)
                st.audio(audio_file)