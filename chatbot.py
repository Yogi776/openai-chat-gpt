# Import the required libraries
import openai
# import os
import streamlit as st

# Set the GPT-3 API key
openai.api_key = st.text_input("Enter you API Key ")

st.markdown("<h1 style='text-align: center; color: black;'>Chat GPT Demo Demo</h1>", unsafe_allow_html=True)

article_text = st.text_area("Enter your Question")
output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text)>= 0:
    if st.button("Generate Summary",type='primary'):

    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Please summarize this scientific article for me in a few sentences: " + article_text,
            temperature=0.9,
            max_tokens=out_token,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")