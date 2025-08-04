import streamlit as st
from prompts import get_question_prompt
from utils import ask_gemini
import re
import time

st.set_page_config(page_title="TalentScout AI", page_icon="🤖")


if st.sidebar.button("❌ End Conversation"):
    st.session_state.clear()
    st.success("👋 Conversation ended. Thank you!")
    st.stop()


if 'step' not in st.session_state:
    st.session_state.step = "greeting"
if 'candidate_data' not in st.session_state:
    st.session_state.candidate_data = {}
if 'tech_stack' not in st.session_state:
    st.session_state.tech_stack = ""
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = []

# Step 1: Greet the user
if st.session_state.step == "greeting":
    st.title("🤖 TalentScout Hiring Assistant")
    st.success("Hi there! I'm TalentScoutBot, here to help screen your skills.")
    if st.button("Start Application"):
        st.session_state.step = "collect_info"

# Step 2: Collect Candidate Info
if st.session_state.step == "collect_info":
    st.header("📝 Candidate Information")
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.slider("Years of Experience", 0, 30)
        position = st.text_input("Desired Position")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (comma-separated)")
        submitted = st.form_submit_button("Next")

    if submitted:
        if not all([name, email, phone, position, location, tech_stack]):
            st.warning("Please fill in all fields.")
        else:
            st.session_state.candidate_data = {
                "name": name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack
            }
            st.session_state.tech_stack = tech_stack
            st.session_state.step = "generate_questions"

# Step 3: Generate Questions via Gemini
if st.session_state.step == "generate_questions":
    st.info("Generating technical questions for your tech stack...")
    prompt = get_question_prompt(st.session_state.tech_stack)

    questions = []
    retries = 3

    while len(questions) < 5 and retries > 0:
        response = ask_gemini(prompt)
        lines = response.text.strip().split("\n") if response and hasattr(response, "text") else []

        questions = []
        for line in lines:
            clean = line.strip()
            if clean.endswith("?"):
                questions.append(clean)
            elif re.match(r"^\d+\.", clean) and clean.endswith("?"):
                questions.append(clean[2:].strip())

        retries -= 1
        time.sleep(1)

    questions = questions[:5]
    st.session_state.questions = questions
    st.session_state.answers = [""] * len(questions)
    st.session_state.step = "answer_questions"
    st.rerun()

# Step 4: Show Questions
if st.session_state.step == "answer_questions":
    st.header("🧠 Technical Questions")
    with st.form("qa_form"):
        for i, q in enumerate(st.session_state.questions):
            st.markdown(f"**Q{i+1}: {q}**")
            st.session_state.answers[i] = st.text_area(
                f"Your answer to Q{i+1}",
                value=st.session_state.answers[i],
                key=f"answer_{i}"
            )
        submitted = st.form_submit_button("Submit Answers")

    if submitted:
        st.session_state.step = "summary"
        st.rerun()

# Step 5: Show Summary
if st.session_state.step == "summary":
    st.header("📋 Submission Summary")
    st.success("✅ Thank you! Your application has been recorded.")

    st.subheader("👤 Candidate Info")
    for key, value in st.session_state.candidate_data.items():
        st.markdown(f"**{key.title()}:** {value}")

    st.subheader("🧠 Your Answers")
    for i, (q, a) in enumerate(zip(st.session_state.questions, st.session_state.answers)):
        st.markdown(f"**Q{i+1}: {q}**")
        st.markdown(f"✍️ **Answer:** {a}")
