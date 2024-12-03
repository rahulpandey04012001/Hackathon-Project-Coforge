import streamlit as st
from utils.nlp_parser import parse_user_story
from utils.test_generator import generate_test_cases
from gpt_integration import generate_test_cases_with_gpt3
from flow_chart import create_flow_chart_with_python
from io import BytesIO
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Requirement Rebels - Test Case Generator",
    page_icon="🐍",  # Python emoji
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a header mentioning Python
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Requirement Rebels</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Built with Python 🐍</h3>", unsafe_allow_html=True)

# Subtitle
st.markdown("<h4 style='text-align: center;'>Automated Test Case Generator</h4>", unsafe_allow_html=True)

# Initialize session state
if "test_cases" not in st.session_state:
    st.session_state["test_cases"] = None

# Input for user story
user_story = st.text_area(
    "Enter a User Story:",
    placeholder="E.g., As a user, I want to reset my password so that I can access my account."
)

# Input for max test cases
max_cases = st.number_input("Max Test Cases (for GPT-3.5-turbo)", min_value=1, max_value=10, value=3)

# Buttons and their functionality
if st.button("Generate Test Cases (Basic)"):
    if user_story.strip():
        parsed_data = parse_user_story(user_story)
        st.session_state["test_cases"] = generate_test_cases(parsed_data)
        st.subheader("Generated Test Cases (Basic):")
        for case in st.session_state["test_cases"]:
            st.write(f"**Test Case {case['ID']}**")
            st.write(f"- **Step:** {case['Step']}")
            st.write(f"- **Expected:** {case['Expected']}")
    else:
        st.error("Please enter a valid user story.")

if st.button("Generate Test Cases with GPT-3.5-turbo"):
    if user_story.strip():
        st.session_state["test_cases"] = generate_test_cases_with_gpt3(user_story, max_cases)
        st.subheader("Generated Test Cases (GPT-3.5-turbo):")
        st.write(st.session_state["test_cases"])
    else:
        st.error("Please enter a valid user story.")

if st.button("Export Test Cases"):
    if st.session_state["test_cases"]:
        with open("test_cases/test_cases.txt", "w") as file:
            file.write(str(st.session_state["test_cases"]))
        st.success("Test cases exported to 'test_cases/test_cases.txt'.")
    else:
        st.error("No test cases to export!")

# Button to display flow chart
if st.button("Show Project Flow Chart"):
    st.subheader("Project Flow Chart")
    # Generate the flow chart
    fig = create_flow_chart_with_python()  # Get the figure from flow_chart.py
    st.pyplot(fig)  # Display the figure in Streamlit

#Add Positive Scenarios

