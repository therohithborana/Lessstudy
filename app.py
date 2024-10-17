import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import os

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to extract text from a PDF file
def extract_pdf_text(pdf_file_path):
    pdf_reader = PdfReader(pdf_file_path)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() + "\n"
    return pdf_text

# Function to save the uploaded PDF to the local file system
def save_uploaded_file(uploaded_file, file_path):
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Streamlit app interface
st.title('Lessstudy: Upload Question Papers')

# Placeholder to store the paths of saved PDFs
pdf_file_paths = []

# Create 5 upload areas for the PDFs
for i in range(1, 6):
    pdf_file = st.file_uploader(f"Upload PDF {i}", type="pdf", key=f"pdf{i}")
    if pdf_file is not None:
        st.success(f'PDF {i} uploaded successfully.')
        # Save the uploaded file
        file_path = f"./QuesPap{i}.pdf"
        save_uploaded_file(pdf_file, file_path)
        pdf_file_paths.append(file_path)

# Ensure all 5 PDFs are uploaded before proceeding
if len(pdf_file_paths) == 5:
    st.write("All 5 PDFs uploaded successfully! Extracting text...")

    # Extract text from the uploaded PDFs
    extracted_texts = []
    for idx, pdf_path in enumerate(pdf_file_paths, 1):
        pdf_content = extract_pdf_text(pdf_path)
        extracted_texts.append(f"PDF {idx} Content:\n{pdf_content}")

    # Combine the content from all PDFs
    combined_content = "\n\n".join(extracted_texts)

    # Create the query for Gemini API
    query = f"""
    Please analyze the following content extracted from five PDFs and categorize the questions module-wise.

    Instructions:
    - Identify and mark the questions based on the number of repetitions across the five PDFs.
    - Categorize questions as 'Most repeated' (appears 3 or more times), 'Repeated' (appears 2 times), and 'Unique' (appears only once).
    - Organize the questions by modules.
    - Consider that the questions may not have the exact same wording but might be similar in meaning.

    Content:
    {combined_content}
    """

    # Call the Gemini API to generate the content
    response = genai.generate(messages=[{"content": query}])
    
    # Check if the response contains any content
    if response and "content" in response[0]:
        st.write(response[0]["content"])
    else:
        st.error("Failed to generate a valid response from the Gemini API.")

else:
    st.warning("Please upload all 5 PDFs.")


# Add credits at the bottom of the page
st.markdown("""
    <p style='text-align: center;'>
    Made by <a href="https://www.linkedin.com/in/rohith-borana-b10778266" target="_blank">Rohith Borana</a>
    </p>
    """, unsafe_allow_html=True)
