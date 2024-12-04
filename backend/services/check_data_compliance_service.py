from fastapi import HTTPException
# from backend.workflows.text_workflow import check_text_compliance
from workflows.pdf_workflow import check_pdf_compliance
from utils.exceptions import WorkflowError
from workflows.workflows import initialize_text_workflow

def process_text(data: str):
    text_workflow = initialize_text_workflow()
    user_input = { "input_text":data }
    for event in text_workflow.stream(user_input):
        data = event.values()
        print("The data from the stream " ,data)
        for value in event.values():
            print(value['results'])
            results_list = value['results']
        

    results = results_list
    return results

def check_compliance(data: str, data_type: str, data_url: str):
    try:
        if data_type == "text":
            print("for text workflow")    # Remove it after adding text workflow
            return process_text(data)
            # return check_text_compliance(data)
        elif data_type == "pdf":
            return check_pdf_compliance(data_url)
        else:
            raise WorkflowError(f"Unsupported dataType: {data_type}")
    except WorkflowError as e:
        # Raise a structured HTTP error
        raise HTTPException(status_code=400, detail=str(e))
