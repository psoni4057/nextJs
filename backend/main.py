from backend.services.gemini_service import GeminiService, ValidationService

# Example usage
if __name__ == "__main__":
    gemini_service = GeminiService(api_key="api-key", model_url=" ")
    content = " "
    validation_response = gemini_service.generate_response(content)
    
    # Print the validation response
    print(validation_response)