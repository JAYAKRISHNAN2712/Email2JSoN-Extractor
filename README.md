# Email2JSON-Extractor

Email2JSON-Extractor is a project designed to convert emails in PDF or PNG format into a structured JSON format. The application uses OCR (Optical Character Recognition) to extract text from email images and then processes this text to extract key-value pairs using LLM, representing the email content. The final JSoN Structured output contains keys, "From", "To", "Cc", "BCc", "Date", "Time", "Subject", "Body", and "Summary".

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)


## Features

- Upload PDF or PNG email files.
- Extract text from images using PaddleOCR.
- Parse email contents into key-value pairs using LLM.
- Convert parsed content into JSON format using Langchain Custom Tools.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Email2JSON-Extractor.git
    cd Email2JSON-Extractor
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Upload a PDF or PNG email file through the web interface.

3. The application will process the file and display the extracted contents and the resulting JSON.

## Project Structure

```plaintext
Email2JSON-Extractor/Source/
│
├── app.py          # Streamlit app for file upload and displaying results
├── ocr.py          # OCR processing using PaddleOCR
├── llm.py          # Extract email contents in key-value format
├── tool.py         # Convert key-value content into JSON format
├── requirements.txt# List of required dependencies

Email2JSON-Extractor/
│
├── README.md       # Project documentation
