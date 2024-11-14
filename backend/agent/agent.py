from services.gemini_service import GeminiService

def invoke_agent():
    gemini_service = GeminiService()
    print(gemini_service.invoke_service({"data":"What is the capital of India"}))