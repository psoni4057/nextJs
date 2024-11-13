from services.gemini_service import GeminiService
from models.gemini import llm 

gemini_service = GeminiService()
print(gemini_service.invoke_service({"data":"What is the capital of India"}))