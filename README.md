# Lessstudy

Lessstudy is a web-based tool designed to help students analyze previous year question papers by identifying the most repeated questions. The application takes five input PDFs (question papers) and categorizes the questions using the **Gemini API** to determine which ones are repeated most frequently across the PDFs.

## Features

- Upload up to 5 PDFs of question papers.
- Extract text from the uploaded PDFs.
- Analyze questions to identify:
  - **Most Repeated**: Appears 3 or more times.
  - **Repeated**: Appears 2 times.
  - **Unique**: Appears only once.
- Categorize the questions based on modules across the PDFs.

## Tech Stack

- **Streamlit**: Web framework used to build the user interface.
- **Gemini API**: For content generation and categorizing the questions based on repetition.
- **PyPDF**: For extracting text from the uploaded PDFs.
- **Localtunnel**: For exposing the app to the internet temporarily during development.

## Project Structure

```plaintext
Lessstudy/
├── app.py                 # The main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files
└── .env                   # API key (not included in the repository)

