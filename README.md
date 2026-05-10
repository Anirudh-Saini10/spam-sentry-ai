# 🛡️ SpamSentry

SpamSentry is an AI-powered phishing and SMS spam detection system built using a fine-tuned DistilBERT transformer model with explainable threat analysis and real-time cloud deployment.

---

# 🚀 Live Demo

https://spam-sentry-ai-ohzyu8xplysuo9jfnzl5tj.streamlit.app/

---

# 🔥 Features

- Fine-tuned DistilBERT spam classifier
- Real-time phishing and spam detection
- Explainable threat analysis engine
- Confidence score visualization
- Dynamic random spam/safe example generation
- Interactive Streamlit frontend
- Hugging Face-hosted transformer model
- Cloud-deployed NLP inference pipeline

---

# 🧠 System Architecture

```text
User Input
    ↓
DistilBERT Tokenizer
    ↓
DistilBERT Transformer Model
    ↓
Spam / Safe Classification
    ↓
Threat Analysis Engine
    ↓
Frontend Visualization
```

---

# 🤖 Model Details

## Base Model

- DistilBERT (`distilbert-base-uncased`)
- Transformer-based NLP architecture from Hugging Face

## Dataset

SMS Spam Collection Dataset from Hugging Face:

- Total messages: 5,574
- Ham (safe): 4,827
- Spam: 747

Additional manually curated phishing examples were added to improve modern phishing detection performance.

## Training Configuration

| Parameter | Value |
|---|---|
| Epochs | 3 |
| Batch Size | 16 |
| Max Token Length | 128 |
| Training Device | CPU |
| Loss Function | CrossEntropyLoss |
| Optimizer | AdamW |

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Transformers | NLP pipeline |
| DistilBERT | Transformer model |
| PyTorch | Deep learning framework |
| Streamlit | Frontend + deployment |
| Hugging Face Hub | Model hosting |
| GitHub | Version control |

---

# ☁️ Deployment Architecture

```text
GitHub → Source Code Hosting
Hugging Face Hub → Model Hosting
Streamlit Cloud → Frontend Deployment
```

The trained transformer weights are hosted separately on Hugging Face because the model exceeded GitHub's file size limits.

---

# 📸 Application Preview
<img width="1349" height="624" alt="image" src="https://github.com/user-attachments/assets/66b9a410-7013-46be-a8a3-7ff2242e9723" />

## Features Demonstrated

- Real-time message analysis
- Spam probability scoring
- Threat indicator explanations
- Interactive testing interface
- Randomized spam/safe examples

---

# 🛠️ Local Installation

Clone repository:

```bash
git clone https://github.com/Anirudh-Saini10/spam-sentry-ai.git
cd spam-sentry-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

# 🤗 Hugging Face Model

https://huggingface.co/anirudhsaini/spamsentry-model

---

# 📌 Future Improvements

- Multi-class scam categorization
- Email phishing detection
- URL risk analysis
- Explainable attention visualization
- REST API deployment
- Mobile application integration

---

# 👨‍💻 Author

Anirudh Saini

Built as a transformer-based NLP security project focused on practical AI deployment, phishing detection, and real-time inference systems.
