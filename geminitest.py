import google.generativeai as genai

api_key = 'AIzaSyCkHD6jP6ahN4HaV2oIqG2Q1-aAsLNCuc0'

def gemini(prompt,parameters):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
                                model_name='gemini-1.5-flash',
                                generation_config= parameters)
    response = model.generate_content(prompt)
    return response.text
    
