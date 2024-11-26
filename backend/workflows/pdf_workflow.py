import requests
from io import BytesIO
from PyPDF2 import PdfReader
from backend.utils.exceptions import WorkflowError


def check_pdf_compliance(data_url: str):
    #if not data_url.startswith("http"):
        #raise WorkflowError("Invalid URL provided for PDF data.")
    
    # Example logic: Fetch the PDF, process it, and check compliance
    pdf_content = fetch_pdf(data_url)
    if not pdf_content:
        raise WorkflowError("Failed to fetch PDF content.")
    
    # Need to call text workflow --------------

    return {"is_compliant": True, "details": "PDF is GDPR compliant"}



def fetch_pdf(url: str):

    pdf_text = ""
    try:
        # Add headers to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        
        # Fetch the PDF from the link
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful
        
        # Load the PDF content
        pdf_bytes = BytesIO(response.content)
        pdf_reader = PdfReader(pdf_bytes)
        
        # Extract text from all pages
        
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        
    except requests.exceptions.RequestException as e:    # Link is not accessible
        print(f"Error fetching the PDF: {e}")     
    except Exception as e:                               # Not able to process PDF
        print(f"Error processing the PDF: {e}")

    return pdf_text



# pdf_url = "https://www.orimi.com/pdf-test.pdf"
# text = check_pdf_compliance(pdf_url)


# print(text)  
