import hashlib
import time
import random
import streamlit as st

# Streamlit setup
st.title("🔒 Cyber Defense Quest: CIA Triad Adventure")
st.write("Welcome, Cyber Agent! Your mission is to secure sensitive data using the CIA Triad principles: Confidentiality, Integrity, and Availability.")

# Initialize session state for tracking progress
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# Stage 1: Confidentiality
if st.session_state.stage == 1:
    st.header("Stage 1: Confidentiality")
    st.write("Imagine you're guarding a treasure chest. The key to this chest is your password. If the key is too simple, a thief can easily copy it and steal the treasure!")

    # Generate a random strong password once
    if 'strong_password' not in st.session_state:
        st.session_state.strong_password = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()", k=10))
        weak_passwords = ["123456", "password", "AgentX!#42", "X!Z9$7@k8"]
        st.session_state.password_options = weak_passwords + [st.session_state.strong_password]
        random.shuffle(st.session_state.password_options)

    st.write("A hacker is trying to steal your password. Choose the strongest one:")
    password_choice = st.radio("Select your password:", st.session_state.password_options)

    if st.button("Submit Password"):
        if password_choice == st.session_state.strong_password:
            st.success("✅ Great choice! You protected the data from being stolen.")
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("❌ The hacker broke in! Try again.")

# Stage 2: Integrity
if st.session_state.stage == 2:
    st.header("Stage 2: Integrity")
    st.write("You’ve stored a top-secret blueprint, but a hacker wants to tamper with it. Imagine a wax seal on a letter — if the seal is broken, you know someone has meddled with it. Here, hashes are your digital seals!")

    original_data = "TopSecretFileContents"
    original_hash = hashlib.sha256(original_data.encode()).hexdigest()
    st.write(f"Original file hash: `{original_hash}`")

    # Generate file options once
    if 'files' not in st.session_state:
        fake_data1 = "TopSecretFileCont3nts"
        fake_data2 = "T0pSecretF1leContents"
        st.session_state.files = [("File A", original_data), ("File B", fake_data1), ("File C", fake_data2)]
        random.shuffle(st.session_state.files)
        st.session_state.file_choices = [f"{name} - {hashlib.sha256(data.encode()).hexdigest()}" for name, data in st.session_state.files]

    selected_file = st.radio("Select the file that is unmodified:", st.session_state.file_choices)

    if st.button("Verify File"):
        selected_index = st.session_state.file_choices.index(selected_file)
        if st.session_state.files[selected_index][1] == original_data:
            st.success("✅ Perfect! You identified the original file.")
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("❌ Data tampered! Hackers misled you. Try again.")

# Stage 3: Availability
if st.session_state.stage == 3:
    st.header("Stage 3: Availability")
    st.write("The server is under DDoS attack! Imagine a store with a huge crowd blocking the entrance — no one can get in to buy anything. Solve this puzzle to clear the crowd and keep the store (server) open!")

    if 'math_puzzle' not in st.session_state:
        math_puzzles = [
            ("(12 * 3) + (18 / 2) - 4", "41"),
            ("(8 * 4) - (10 / 2) + 6", "30"),
            ("(15 / 3) + (7 * 2) - 5", "14")
        ]
        st.session_state.math_puzzle = random.choice(math_puzzles)

    puzzle_question, puzzle_answer = st.session_state.math_puzzle
    answer = st.text_input(f"What is {puzzle_question}? (Quick!):")

    if st.button("Submit Answer"):
        if answer == puzzle_answer:
            st.success("🎉 Mission Complete! You successfully defended the data using the CIA Triad.")
            st.balloons()
            st.write("🏅 Congratulations, Elite Cyber Agent!")
            st.session_state.stage = 1  # Reset for replay
        else:
            st.error("❌ Wrong answer! The server crashed. Hackers won this round. Try again.")

# Final message
    st.write("\n✅ You've completed the advanced CIA Triad practical. Great job!")
