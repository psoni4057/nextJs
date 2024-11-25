from agent.agent import Agent
from services.gemini_service import GeminiService

gemini_service = GeminiService()
agent = Agent(service=gemini_service, db_path='gdbr_Validator.db')
template = """You are a GDPR expert. Tell if the given data is compliant and the reason.
                : {data}. Do not use technical words, give easy-to-understand responses.
                The answer should be in JSON format as follows:
                compliant: yes/no
                reason: """
        
data = "Today is Monday"  
result = agent.invoke_service(template, data)
print(result)