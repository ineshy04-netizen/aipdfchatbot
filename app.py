import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI PDF Chatbot")
st.write("Gemini AI से अपने PDF के बारे में सवाल पूछें।")

uploaded_file = st.file_uploader(
    "अपनी PDF upload करें",
    type=["pdf"]
)

question = st.text_input("अपना सवाल लिखें:")

if st.button("Ask Gemini"):
    if uploaded_file is None:
        st.warning("पहले PDF upload करें।")
    elif not question:
        st.warning("पहले अपना सवाल लिखें।")
    else:
        with st.spinner("Gemini सोच रहा है..."):
            pdf_data = uploaded_file.read()

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=[
                    {
                        "inline_data": {
                            "mime_type": "application/pdf",
                            "data": pdf_data
                        }
                    },
                    question
                ]
            )

            st.subheader("🤖 Gemini का Answer")
            st.write(response.text)