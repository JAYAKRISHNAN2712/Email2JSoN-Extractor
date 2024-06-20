import json
import streamlit as st
from ocr import OCR
from llm import LLM
from tool import Tool

st.header("Email2JSoN Extractor")

# Can upload only .pdf or .png
uploaded_file = st.file_uploader("Upload an Email file", type=['pdf','png'])

if st.button("Submit"):
    if uploaded_file is not None:
        if uploaded_file.type == "image/png":
            with open("uploaded_file.png","wb") as f:
                f.write(uploaded_file.getbuffer())

        if uploaded_file.type == "application/pdf":
            with open("uploaded_file.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
        # adding a spinner
        with st.spinner("Processing"):
            # checking the file type and extracting contents using Paddle OCR.
            if uploaded_file.type == "image/png":
                ocr_instance = OCR(filename="uploaded_file.png")
            else:
                ocr_instance = OCR(filename="uploaded_file.pdf")
            # processing using Meta/Llama3 LLM.
            lang_model = LLM(ocr_instance.mail_extraction())
            str_format = lang_model.ChatTemplate()
            # Converting string output from LLM to JSoN format
            json_obj = Tool(str_format)
            json_format = json_obj.json_converter()
            st.json(json_format)

            #Convert the JSON object to a JSON string and then to bytes
            json_str = json.dumps(json_format, indent=4)
            json_bytes = json_str.encode('utf-8')
            
            # Add a download button
            st.download_button(
                label="Download JSON",
                data=json_bytes,
                file_name=f"{json_format['Subject']}.json",
                mime="application/json"
            )
