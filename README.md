
# TalentScout AI - Hiring Assistant Chatbot

TalentScout AI is an intelligent Streamlit-based chatbot designed to assist tech recruitment agencies in the **initial screening** of candidates. It gathers essential applicant information, dynamically generates technical questions based on the candidate’s tech stack, and allows candidates to submit their answers — all in a seamless conversational interface.

---

## Project Overview

This chatbot simulates a smart hiring assistant that:
- Collects personal and professional details from candidates
- Asks 3–5 relevant technical questions based on their declared tech stack
- Allows candidates to answer the questions in the same session
- Provides a summary of the answers for review

---

## 🛠 Installation Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Vo1denz/talentscout-chatbot.git
cd talentscout-chatbot
```

2. **Set up a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your Gemini API key**

Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

---

## 🧑‍💻 Usage Guide

1. Click "Start Application" to begin.
2. Fill in your personal and technical details.
3. The chatbot will generate 3–5 relevant technical questions.
4. Answer the questions directly in the interface.
5. Submit your answers and view a full summary of your submission.
6. You can end the conversation at any time using the "❌ End Conversation" button.

---

## ⚙️ Technical Details
- `streamlit` for UI and form handling

- `google-generativeai` to call            Gemini                                                                                                                                        

- `python-dotenv` for managing API keys securely

- `re` for regular expressions to filter and clean up Gemini's output

- `time` to introduce delays during retry logic (ensuring full question generation)

### 🧰 Libraries Used
- `streamlit` – UI framework
- `google-generativeai` – Gemini API SDK
- `python-dotenv` – for loading API keys securely
- `re` – regular expressions for filtering response content

### 🧠 LLM Used
- **Model:** `gemini-2.5-flash`
- **Provider:** Google AI Studio
- **Why Flash?** Fast response time, lower latency, cost-effective

### 🧱 Architecture
- Frontend: Streamlit interface
- Backend: Python with session-state handling
- Model interaction: Prompt sent to Gemini via API → cleaned → displayed

---

## ✨ Prompt Design

The chatbot uses a **custom-crafted prompt** to request Gemini to:
- Generate *exactly* 5 technical questions
- Format each question clearly, one per line
- Avoid any introductory or explanatory content
- Maintain context across the conversation for future expansion (e.g., follow-up questions)

We also included a robust filter to **detect only actual questions** from the output using `?` and regex patterns.

---

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| Gemini Flash sometimes returned only 2–3 questions | Added strict prompt instructions and retry logic to enforce 5 |
| Extra junk like titles in output | Used regex filtering to extract only proper questions |
| Session crashes on missing data | Initialized all session state variables safely |
| Quota errors from Gemini | Switched from `gemini-pro` to `gemini-2.5-flash`, added fallbacks |
| Needed graceful end | Added "End Conversation" button with `st.session_state.clear()` |

---

## 📹 Demo

Watch the full walkthrough of the chatbot in action:  
👉 [Loom Video Link](https://loom.com/) *(replace with actual link)*

---

## 📦 Optional Enhancements (Bonus Implemented)

- ✅ Session-based interaction flow
- ✅ Custom UI flow with question filtering
- ✅ Performance-optimized using Gemini Flash model




