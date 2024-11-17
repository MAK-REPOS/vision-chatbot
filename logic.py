import os
import google.generativeai as genai 
from main import streamlit_app
from PIL import Image

def vision_chat() :
    genai.configure(api_key='AIzaSyDysRriCh_xnloDODlfwpKn5ABORNWuzC8')

    #media = input('enter the image path') #'cricket.jpeg'
    file = genai.upload_file(media)
    #query = input('enter the query') # 'describe the image'
    model = genai.GenerativeModel('gemini-1.5-flash')
    result = model.generate_content(
        [file,'\n\n',query]
    )
    #print(f'{result.text}')
    result = result.text
    return result
    