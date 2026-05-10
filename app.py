import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="SpamSentry",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #050816;
    color: white;
}

.main-title {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #9CA3AF;
    margin-bottom: 30px;
}

.tech-stack {
    text-align: center;
    color: #9CA3AF;
    margin-bottom: 20px;
}

.spam-box {
    background: rgba(255, 0, 0, 0.15);
    border: 1px solid rgba(255,0,0,0.4);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #ff4b4b;
    margin-top: 20px;
}

.ham-box {
    background: rgba(0, 255, 100, 0.12);
    border: 1px solid rgba(0,255,100,0.35);
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #00ff99;
    margin-top: 20px;
}

.threat-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 16px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SAMPLE MESSAGES ----------------

spam_examples = [
    "CONGRATULATIONS! You won a FREE iPhone!!! Click now to claim reward.",
    "URGENT: Your bank account has been suspended. Verify immediately.",
    "WIN CASH NOW!!! Limited time offer!!!",
    "You have been selected for a FREE vacation package.",
    "Claim your FREE Netflix subscription today!",
    "Earn ₹50,000 per week from home. Click now!",
    "Your Paytm account is blocked. Verify your identity immediately.",
    "Get rich fast with this secret crypto trick!",
    "Exclusive reward waiting for you. Act now!",
    "FINAL WARNING!!! Your account will be deleted today."
]

safe_examples = [
    "Hey bro are we still meeting tomorrow evening?",
    "Can you send me the assignment PDF?",
    "Mom said dinner will be ready by 8.",
    "Let's play football this weekend.",
    "I'm outside your house, come down.",
    "Did you complete the lab record?",
    "The meeting has been shifted to Monday.",
    "Happy birthday! Hope you have a great day.",
    "Can you call me when you're free?",
    "Your Amazon package has been delivered."
]

# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    tokenizer = DistilBertTokenizer.from_pretrained(
    "anirudhsaini/spamsentry-model"
    )

    model = DistilBertForSequenceClassification.from_pretrained(
    "anirudhsaini/spamsentry-model"
    )
    model.eval()
    return tokenizer, model

with st.spinner("🛡️ Initializing SpamSentry AI Engine..."):

    try:
        tokenizer, model = load_model()

    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

# ---------------- PREDICT FUNCTION ----------------

def predict(text):

    inputs = tokenizer(
        text,
        return_tensors='pt',
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probs = torch.softmax(outputs.logits, dim=1)

    confidence = probs.max().item()
    prediction = probs.argmax().item()

    return prediction, confidence

# ---------------- THREAT ANALYSIS ----------------

def analyze_threats(text):

    threats = []

    text_upper = text.upper()

    spam_keywords = [
        "FREE",
        "WIN",
        "PRIZE",
        "URGENT",
        "CLICK",
        "LIMITED",
        "OFFER",
        "MONEY",
        "REWARD",
        "CONGRATULATIONS"
    ]

    found_keywords = []

    for word in spam_keywords:
        if word in text_upper:
            found_keywords.append(word)

    if found_keywords:
        threats.append(
            f"Suspicious promotional keywords detected: {', '.join(found_keywords)}"
        )

    if text.count("!") >= 3:
        threats.append(
            "Excessive exclamation marks indicate aggressive messaging"
        )

    if any(word.isupper() and len(word) > 3 for word in text.split()):
        threats.append(
            "Heavy capitalization detected"
        )

    if "http://" in text or "https://" in text or "www." in text:
        threats.append(
            "Possible suspicious link detected"
        )

    if len(text) > 200:
        threats.append(
            "Unusually long message structure"
        )

    return threats

# ---------------- SIDEBAR ----------------

st.sidebar.title("🛡️ SpamSentry")

st.sidebar.markdown("### AI Threat Detection")

st.sidebar.markdown("---")

st.sidebar.markdown("### ⚙️ Tech Stack")

st.sidebar.markdown("- DistilBERT")
st.sidebar.markdown("- HuggingFace")
st.sidebar.markdown("- PyTorch")
st.sidebar.markdown("- Streamlit")

st.sidebar.markdown("---")

st.sidebar.metric("Model Accuracy", "98%+")

st.sidebar.markdown("---")

st.sidebar.caption("Transformer-based NLP spam detection system")

# ---------------- MAIN TITLE ----------------

st.markdown(
    '<div class="main-title">🛡️ SpamSentry</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered SMS Spam Detection System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="tech-stack">Real-time threat classification using fine-tuned DistilBERT</div>',
    unsafe_allow_html=True
)

# ---------------- EXAMPLE BUTTONS ----------------

col1, col2 = st.columns(2)

with col1:
    if st.button("🎁 Random Spam Example"):
        st.session_state.example_text = random.choice(spam_examples)

with col2:
    if st.button("💬 Random Safe Example"):
        st.session_state.example_text = random.choice(safe_examples)

# ---------------- TEXT INPUT ----------------

user_input = st.text_area(
    "Enter message to analyze:",
    value=st.session_state.get("example_text", ""),
    height=180,
    placeholder="Type or paste SMS message here..."
)

# ---------------- ANALYZE BUTTON ----------------

if st.button("🔍 Analyze Message"):

    if user_input.strip():

        prediction, confidence = predict(user_input)

        if prediction == 1:

            st.markdown(
                '<div class="spam-box">🚨 SPAM DETECTED</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="ham-box">✅ SAFE MESSAGE</div>',
                unsafe_allow_html=True
            )

        st.markdown("### Confidence Score")

        st.progress(confidence)

        st.write(f"### {confidence:.2%}")

        # Threat Analysis
        threats = analyze_threats(user_input)

        if threats:

            st.markdown(
                '<div class="threat-box">',
                unsafe_allow_html=True
            )

            st.markdown("## 🚨 Threat Analysis")

            for threat in threats:
                st.markdown(f"- {threat}")

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.success("No obvious spam indicators detected.")

    else:

        st.warning("Please enter a message.")