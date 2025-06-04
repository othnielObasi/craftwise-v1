import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


# Load .env only locally (not in GitHub Actions)
if os.getenv("GITHUB_ACTIONS") != "true":
    from dotenv import load_dotenv
    load_dotenv()
  
# ---- Streamlit Page Configuration ----
st.set_page_config(
    page_title="CraftWise",
    layout="centered"
)

# ---- Initialize Session State for Rate Limiting ----
if "default_request_count" not in st.session_state:
    st.session_state.default_request_count = 0

# ---- Title and Description ----
st.title("CraftWise")
st.markdown(
    """
    **Get tailored writing suggestions** based on your audience, formality, domain, and intent.  
    You may either enter your own OpenAI API key (no request limit) or use our default API key (limited to 5 suggestions per session).
    """
)

# ---- Retrieve Default API Key from Environment ----
default_api_key = os.getenv("DEFAULT_OPENAI_API_KEY", "").strip()

# ---- API Key Selection ----
use_default = False
if default_api_key:
    use_default = st.checkbox(
        label="Use default API key (max 5 suggestions)",
        value=False
    )
    if use_default:
        st.info("You are using the default API key. Limited to 5 suggestions this session.")

if use_default:
    api_key = default_api_key
else:
    api_key = st.text_input(
        label="Enter your OpenAI API Key",
        placeholder="sk-...",
        type="password"
    )
    if api_key:
        st.success("Using your provided API key. No request limit.")

# ---- Validate API Key Presence ----
if use_default:
    # default key exists by definition
    pass
else:
    if not api_key:
        st.error("Please provide a valid OpenAI API key (either use default or enter your own).")
        st.stop()

# ---- Initialize OpenAI Client ----
try:
    client = OpenAI(api_key=api_key.strip())
except Exception as e:
    st.error(f"Failed to initialize OpenAI client: {e}")
    st.stop()

# ---- TailoredWritingAssistant Class ----
class TailoredWritingAssistant:
    def __init__(self, client: OpenAI):
        self.client = client
        self.options = {
            "audience": "knowledgeable",
            "formality": "formal",
            "domain": "business",
            "intent": "inform",
        }

    def set_options(self, audience: str, formality: str, domain: str, intent: str):
        self.options["audience"] = audience
        self.options["formality"] = formality
        self.options["domain"] = domain
        self.options["intent"] = intent

    def construct_prompt(self, text: str) -> str:
        prompt_intro = (
            f"Considering the audience is {self.options['audience']}, "
            f"the formality is {self.options['formality']}, "
            f"the domain is {self.options['domain']}, "
            f"and the intent is to {self.options['intent']}, rewrite the text:\n\n"
        )
        return prompt_intro + text

    def get_suggestions(self, text: str) -> str:
        full_prompt = self.construct_prompt(text)
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.7,
                max_tokens=1024,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            if response.choices and len(response.choices) > 0:
                return response.choices[0].message.content
            else:
                return "Error: No suggestions generated."
        except Exception as e:
            return f"An error occurred while generating suggestions: {e}"

# ---- Instantiate the Assistant ----
assistant = TailoredWritingAssistant(client)

# ---- Streamlit Input Widgets ----
user_text = st.text_area(
    label="Enter Text to Rewrite",
    placeholder="Type or paste your text here...",
    height=200
)

audience = st.radio(
    label="Audience",
    options=["general", "knowledgeable", "expert"],
    index=1  # default to "knowledgeable"
)

formality = st.radio(
    label="Formality",
    options=["informal", "neutral", "formal"],
    index=2  # default to "formal"
)

domain = st.selectbox(
    label="Domain",
    options=["academic", "business", "general", "email", "casual", "creative"],
    index=1  # default to "business"
)

intent = st.radio(
    label="Intent",
    options=["inform", "describe", "convince", "tell a story"],
    index=0  # default to "inform"
)

# ---- Rate-Limited Generate Button (only if using default key) ----
max_requests = 5
if use_default and st.session_state.default_request_count >= max_requests:
    st.error(f"Request limit reached ({max_requests} suggestions). To continue, enter your own API key.")
    generate_disabled = True
else:
    generate_disabled = False

if st.button("Generate Suggestions", disabled=generate_disabled):
    if not user_text.strip():
        st.error("Please enter some text to rewrite.")
    else:
        # If using default key, increment the counter
        if use_default:
            st.session_state.default_request_count += 1

        with st.spinner(
            "Generating tailored suggestions"
            + (f" (Request {st.session_state.default_request_count}/{max_requests})" if use_default else "")
            + "…"
        ):
            assistant.set_options(audience, formality, domain, intent)
            suggestions = assistant.get_suggestions(user_text)

        st.subheader("Tailored Suggestions")
        st.text_area(label="", value=suggestions, height=300)

        if use_default and st.session_state.default_request_count >= max_requests:
            st.warning("You have reached the 5-suggestion limit using the default API key. Refresh or enter your own key to continue.")
