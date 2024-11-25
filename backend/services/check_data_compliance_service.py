from fastapi import HTTPException
# from backend.workflows.text_workflow import check_text_compliance
from backend.workflows.pdf_workflow import check_pdf_compliance
from backend.utils.exceptions import WorkflowError

def check_compliance(data: str, data_type: str, data_url: str):
    try:
        if data_type == "text":
            print("for text workflow")    # Remove it after adding text workflow
            # return check_text_compliance(data)
        elif data_type == "pdf":
            return check_pdf_compliance(data_url)
        else:
            raise WorkflowError(f"Unsupported dataType: {data_type}")
    except WorkflowError as e:
        # Raise a structured HTTP error
        raise HTTPException(status_code=400, detail=str(e))
