import streamlit as st
from groq import Groq

st.title("📚 AI Study Buddy")
st.write("Paste your notes below, then ask a question about them.")

api_key = st.text_input("Enter your Groq API key", type="password")
notes = st.text_area("Paste your notes here", height=200)
question = st.text_input("Ask a question about your notes")

if st.button("Ask"):
    if not api_key or not notes or not question:
        st.warning("Please fill in all three fields!")
    else:
        client = Groq(api_key=api_key)
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{
                    "role": "user",
                    "content": f"Using ONLY the notes below, answer the question. If the answer isn't in the notes, say 'I could not find this in your notes'.\n\nNotes:\n{notes}\n\nQuestion: {question}"
                }]
            )
        st.success("Answer:")
        st.write(response.choices[0].message.content)