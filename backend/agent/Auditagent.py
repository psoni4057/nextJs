import datetime
from state.datastate import DataState
from core.Audit import Audit

audit = Audit.create_audit()

def invoke_audit_agent(state: DataState):
        appName = state["appName"]
        model = state["model"]
        status = state["status"]
        comments = state["comments"]
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d-%m-%Y")
        audit.insert_values(formatted_date, appName, model, status, comments)
        print("Values inserted")
        return state
       