import streamlit as st
from chatgptapp import structured_generator  # Assuming this is a predefined function in the helpers module


# Streamlit code to create the UI
def main():
    # Set up the title and description of the web app
    st.title("Fitness")
    st.write("Generate Health and Fitness based information on a given topic using Custom GPT AI")

    # Input section: User inputs the topic for the blog titles
    user_input = st.text_input("Enter the topic", "...")

    # Button to trigger the title generation
    if st.button("Generate"):
        # Call the structured_generator function with the user input
        prompt = f" you are a Fitness Person , so just respond if the question is related to Health and Fitness, just say the question is out of scope if the question is not related to Health and Fitness {user_input}"

        result = structured_generator(prompt)
        st.write(result.choices[0].message.content)


# run with: "streamlit run web_interface.py"
if __name__ == "__main__":
    main()
