import os
import google.generativeai as genai 
#from main import streamlit_app

#from logic import vision_chat
import streamlit as st
from PIL import Image
import io


def vision_chat(media,query) :
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


def streamlit_app() :
    st.title('Vision Analysis')
    
    media = st.file_uploader('choose an image...',type=['jpg','png','jpeg','JPEG'])
    if media is not None :
        mime_type = media.type
        print(f'mimie type is {mime_type}')
        if mime_type.startswith('image/') :
            image = Image.open(io.BytesIO(media.read()))
            st.image(image,caption='uploaded image',use_column_width=True)
            print(f'mimie type is {mime_type}')
    else :
        st.error('please upload the valid image file')
    
    img = st.text_input('Enter the image path')
    query = st.text_input('enter the query')
    submit = st.button('Submit')
    if submit :
        try :
            result = vision_chat(img,query)
            st.code(result,language = 'markdown')
        except Exception as e:
            st.error(f'An error occured {e}')
        

if __name__ == '__main__' :
    streamlit_app()