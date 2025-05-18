import google.generativeai as genai
import base64

# Configure the API
genai.configure(api_key="AIzaSyD3HhN5hAns_2Z_aK1tPHeb0UWGREP2HQo")

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash')

def ask_abhi_ai(question):
    try:
        # Path to the resume PDF
        pdf_path = "Abhishek Yadav (Resume)1.pdf"
        
        # Read the PDF file
        with open(pdf_path, 'rb') as f:
            pdf_content = f.read()
        
        # Encode the PDF content
        pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
        
        # Create the prompt
        prompt = "You are Abhishek's personal AI which gives user answers based on his resume. Please reply politely to the question based on the resume. Question: " + question
        
        # Generate response
        response = model.generate_content(
            [
                prompt,
                {
                    "mime_type": "application/pdf",
                    "data": pdf_base64
                }
            ]
        )
        
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Test the function
result = ask_abhi_ai("Who are you?")
print(result)
