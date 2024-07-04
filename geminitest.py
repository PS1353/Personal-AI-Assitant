import google.generativeai as genai

api_key = 'your api key'

def gemini(prompt,parameters):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
                                model_name='gemini-1.5-flash',
                                generation_config= parameters)
    response = model.generate_content(prompt)
    return response.text
    
