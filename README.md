AI Study Buddy

A simple AI-powered study assistant that answers questions based on your own notes — built with Python, Streamlit, and Groq's LLaMA API.

Live app: https://study-buddy-xbyux2zpz8dvahxm8xghfb.streamlit.app/

What it does

Paste your notes, ask a question, and the app answers strictly based on what's in your notes — not general knowledge. If the answer isn't in your notes, it says so instead of guessing, which helps prevent AI hallucination.

How it works
Enter your Groq API key.
Paste your notes into the text box.
Ask a question about them.
The app sends your notes and question to Groq's llama-3.3-70b-versatile model via a carefully constrained prompt, and displays the answer.
Tech Stack
Python
Streamlit — web app framework and UI
Groq API (via the official groq Python SDK) — LLM inference
Prompt engineering — the prompt explicitly restricts the model to answering only from the provided notes, reducing hallucination
Key design choice: hallucination prevention

The core prompt is written to constrain the model's behavior:

"Using ONLY the notes below, answer the question. If the answer isn't in the notes, say 'I could not find this in your notes'."

This is a small but deliberate example of prompt engineering — forcing the model to stay grounded in the provided context rather than drawing on its general training data.

Run it locally
bash
pip install streamlit groq
streamlit run app.py

You'll need a free Groq API key from console.groq.com.

Possible future improvements
Store the API key securely (e.g., Streamlit secrets) instead of a plain input field
Support PDF/document upload instead of pasted text
Add conversation history for follow-up questions

Author
Vaidehi Raut
