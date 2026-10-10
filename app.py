import streamlit as st
from groq import Groq, AuthenticationError, RateLimitError, APIConnectionError, APIStatusError

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")
st.title("📚 AI Study Buddy")
st.write("Paste your notes below, then ask a question about them.")

# Prefer a key configured securely in Streamlit Cloud > App settings > Secrets.
# If no secret is configured, allow the user to enter a key in the app.
try:
    saved_api_key = st.secrets.get("GROQ_API_KEY", "")
except Exception:
    saved_api_key = ""

if saved_api_key:
    api_key = saved_api_key
    st.caption("Using the Groq API key configured in app secrets.")
else:
    api_key = st.text_input("Enter your Groq API key", type="password")

notes = st.text_area("Paste your notes here", height=200)
question = st.text_input("Ask a question about your notes")

if st.button("Ask"):
    if not api_key or not notes.strip() or not question.strip():
        st.warning("Please provide an API key, your notes, and a question.")
        st.stop()

    try:
        client = Groq(api_key=api_key)

        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
               model="openai/gpt-oss-120b",

                messages=[
                    {
                        "role": "user",
                        "content": (
                            "Using ONLY the notes below, answer the question. "
                            "If the answer isn't in the notes, say "
                            "'I could not find this in your notes'.\n\n"
                            f"Notes:\n{notes}\n\nQuestion: {question}"
                        ),
                    }
                ],
            )

        answer = response.choices[0].message.content
        st.success("Answer:")
        st.write(answer or "The model returned an empty answer.")

    except AuthenticationError:
        st.error(
            "Groq authentication failed. Check that your API key is correct, "
            "active, and configured as GROQ_API_KEY in Streamlit Secrets. "
            "Do not share your API key publicly."
        )
    except RateLimitError:
        st.error("Groq rate limit or quota reached. Please wait and try again, or check your Groq account limits.")
    except APIConnectionError:
        st.error("Could not connect to Groq. Check your internet connection and try again.")
    except APIStatusError as exc:
        st.error(f"Groq API returned an error (HTTP {exc.status_code}). Please check your model access and API settings.")
    except Exception as exc:
        st.error(f"Something went wrong: {type(exc).__name__}. Check the app logs for details.")
