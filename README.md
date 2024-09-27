
# Lessstudy: An AI-based Tool for Analyzing Repeated Questions

**Lessstudy** is an AI-powered tool that helps students identify the most repeated and important questions across multiple exam question papers. The tool uses Google's Gemini API to analyze the content of five PDF files and categorize questions as **Most Repeated**, **Repeated**, or **Unique**.

---

## Features

- **Upload up to 5 PDFs**: Users can upload five different question papers in PDF format.
- **AI-powered analysis**: The tool utilizes the Google Gemini API to analyze the content.
- **Question Categorization**:
  - **Most Repeated**: Appears 3 or more times across the PDFs.
  - **Repeated**: Appears 2 times.
  - **Unique**: Appears only once.
- **Simple Web Interface**: The user-friendly interface is built using **Streamlit**.

---

## Project Structure

```
Lessstudy/
├── app.py                 # The main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files
└── .env                   # Environment variables (API keys)
```

---

## Installation

To run this project locally, follow the steps below:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Lessstudy.git
cd Lessstudy
```

### 2. Set up a virtual environment (optional but recommended)

```bash
# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
# On macOS/Linux
source env/bin/activate
# On Windows
env\Scriptsctivate
```

### 3. Install the dependencies

Install all the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory of the project and add your Google Gemini API key:

```bash
GOOGLE_API_KEY=your_actual_gemini_api_key
```

Replace `your_actual_gemini_api_key` with your real API key from [Google Gemini](https://developers.generativeai.google/api).

### 5. Run the Streamlit app

Use the following command to run the Streamlit web app:

```bash
streamlit run app.py
```

Once the app starts, open your browser and navigate to `http://localhost:8501` to access the tool.

---

## Usage

1. **Upload PDFs**: Upload five PDF files, each containing exam questions.
2. **Analyze Content**: The tool will extract and analyze the content of the PDFs using the Google Gemini API.
3. **Categorized Results**: The tool will display the categorized questions:
   - **Most Repeated**: Questions that appear 3 or more times across the PDFs.
   - **Repeated**: Questions that appear 2 times.
   - **Unique**: Questions that appear only once.

---

## Environment Variables

Make sure to configure the following environment variable in the `.env` file:

| Variable Name     | Description                |
|-------------------|----------------------------|
| `GOOGLE_API_KEY`  | Your API key for Google Gemini |

---

## Dependencies

This project relies on the following Python packages:

- **streamlit**: For building the web interface.
- **pypdf**: For extracting text from PDF files.
- **google-generativeai**: To integrate with Google's Gemini API.

You can find these dependencies listed in the `requirements.txt` file.

---

## .gitignore

The `.gitignore` file is used to prevent unnecessary files from being tracked by Git. Here's the content:

```plaintext
# Ignore environment variable files
.env

# Ignore Python cache and other unnecessary files
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore system files
.DS_Store
*.swp
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---



