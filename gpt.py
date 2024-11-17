# import streamlit as st
# from PIL import Image
# import io
# import google.generativeai as genai
# import tempfile

# def vision_chat(media, query):
#     genai.configure(api_key='AIzaSyDysRriCh_xnloDODlfwpKn5ABORNWuzC8')

#     # Save the uploaded image to a temporary file
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
#         temp_file.write(media.read())  # Save the media content to the temp file
#         temp_path = temp_file.name  # Get the path to the saved file
    
#     # Upload the temporary file to genai
#     file = genai.upload_file(temp_path)

#     model = genai.GenerativeModel('gemini-1.5-flash')
#     result = model.generate_content([file, '\n\n', query])
#     result = result.text
#     return result


# def streamlit_app():
#     st.title('Vision Analysis')

#     # File uploader for images
#     media = st.file_uploader('Choose an image...', type=['jpg', 'png', 'jpeg', 'JPEG'])
#     if media is not None:
#         mime_type = media.type
#         print(f'Mime type is {mime_type}')
#         if mime_type.startswith('image/'):
#             image = Image.open(io.BytesIO(media.read()))
#             st.image(image, caption='Uploaded image', use_column_width=True)
#             print(f'Mime type is {mime_type}')
#     else:
#         st.error('Please upload a valid image file')

#     # Text input for the query
#     query = st.text_input('Enter the query')
#     submit = st.button('Submit')

#     if submit:
#         try:
#             # Run the vision chat function
#             result = vision_chat(media, query)
#             st.code(result, language='markdown')
#         except Exception as e:
#             st.error(f'An error occurred: {e}')


# if __name__ == '__main__':
#     streamlit_app()


import streamlit as st
from PIL import Image
import io
import google.generativeai as genai

def vision_chat(media, query):
    genai.configure(api_key='AIzaSyDysRriCh_xnloDODlfwpKn5ABORNWuzC8')

    # Upload the image file directly (instead of saving to a temporary file)
    file = genai.upload_file(media)

    model = genai.GenerativeModel('gemini-1.5-flash')
    result = model.generate_content([file, '\n\n', query])
    result = result.text
    return result

def streamlit_app():
    st.title('Vision Analysis')

    # File uploader for images
    media = st.file_uploader('Choose an image...', type=['jpg', 'png', 'jpeg', 'JPEG'])
    if media is not None:
        mime_type = media.type
        print(f'Mime type is {mime_type}')
        if mime_type.startswith('image/'):
            image = Image.open(io.BytesIO(media.read()))
            st.image(image, caption='Uploaded image', use_column_width=True)
            print(f'Mime type is {mime_type}')
    else:
        st.error('Please upload a valid image file')

    # Text input for the query
    query = st.text_input('Enter the query')
    submit = st.button('Submit')

    if submit:
        try:
            # Run the vision chat function
            result = vision_chat(media, query)
            st.code(result, language='markdown')
        except Exception as e:
            st.error(f'An error occurred: {e}')


if __name__ == '__main__':
    streamlit_app()
