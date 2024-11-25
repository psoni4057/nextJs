
class WorkflowError(Exception):
    """
    Custom exception for errors in workflows.
    
    Attributes:
        message (str): The error message to display.
        code (int): Optional error code to categorize the error.
    """
    def __init__(self, message: str, code: int = 400):
        super().__init__(message)
        self.message = message
        self.code = code

    def __str__(self):
        return f"[WorkflowError] {self.message} (Code: {self.code})"
