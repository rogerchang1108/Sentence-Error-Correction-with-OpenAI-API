import json
import openai
import requests 

import streamlit as st
from streamlit_lottie import st_lottie 

# openai.api_key = ''

def correct_error(prompt, input_content, model_selected):

    content_statement = prompt
    
    content_input = f"""{input_content}"""
    
    try:
        response = openai.ChatCompletion.create(
            model = model_selected,
            messages = [
                {'role': 'user', 'content': content_statement},
                {'role': 'user', 'content': content_input}
            ],
            temperature = 0.7
        )

        response_content = response['choices'][0]['message']['content']
        
        st.write(f"""{model_selected}'s response:""")
        st.write(response_content)
    
    except Exception as e:
        st.info('❗Something went wrong! Check your OpenAI API Key!!!')
        st.error(f'An error occurred: {e}')

tab1, tab2 = st.tabs(["Sentence Error Correction", "Surprise!!!"])

with tab1:
    st.title("Sentence Error Correction")
    
    if 'disabled' not in st.session_state:
        st.session_state.disabled = True
    
    input_api_key = st.text_input('OpenAI API Key:')
    openai.api_key = input_api_key
    
    if input_api_key:
        st.success('Unlocked!', icon = '🔓')
        st.session_state.disabled = False
    else:
        st.info('Locked: Please Input Your OpenAI API Key First.', icon = '🔐')
        st.session_state.disabled = True
      
    with st.form(key='my_form'):
        prompt = st.text_area(
            'Prompt for ChatGPT (You Can Adjust it if you want)',
            f"""Act as an English teacher.
            
Correct the input sentences. There may be article, vocabulary choosing, spelling or phase choosing error, which make the meaning of sentence incorrect and ambiguous. 

Correct the sentence step by step.
Output only the corrected sentence.

For examples: 
Input: I hope you all have a enjoyable stay.
Output: I hope you all have an enjoyable stay.

Input: One of the girls I share with is a British.
Output: One of the girls I share with is British.
    
Input:  It is difficult to reach abandoned places such as small country villages.
Output: It is difficult to reach remote places such as small country villages.

Input:  I want to improve my ability of English.
Output: I want to improve my ability in English.

Input:  We weren't able to stop laughing.
Output: We couldn't stop laughing.
    
Input:  He likes reading, above all novels.
Output: He likes reading, especially novels.
    
Input:  It's a pity that you were absent from the training session.
Output: It's a pity that you weren't at the training session.
    
Here is the input:""",
            height = 600,
            disabled = st.session_state.disabled
        )   
    
        input = st.text_input(
            'Input Incorrect Sentence and Press "Submit" to Get Result',
            'I hope you all have a enjoyable stay.',
            disabled = st.session_state.disabled
        )
    
        model_selected = st.selectbox(
            'Model',
            ['gpt-3.5-turbo-0125', 'gpt-3.5-turbo-1106', 'gpt-4-0125-preview', 'gpt-4-1106-preview'],
            disabled = st.session_state.disabled
        )
    
        submit_button = st.form_submit_button(
            label='Submit', 
            disabled=st.session_state.disabled
        )

    if submit_button:
        correct_error(prompt, input, model_selected)

with tab2:
    url = requests.get( 
    "https://lottie.host/4ce71fb9-e943-45ae-a81d-04435c1e4323/wMTe8jOfPu.json") 

    url_json = dict() 
  
    if url.status_code == 200: 
        url_json = url.json() 
    else: 
        print("Error in the URL") 
  
    st.title("Please Give Me a Star If You Like It")
    
    st_lottie(url_json, 
        # change the direction of our animation 
        reverse = True, 
        # height and width of animation 
        height = 400,   
        width = 400, 
        # speed of animation 
        speed = 0.8,   
        # means the animation will run forever like a gif, and not as a still image 
        loop = True,   
        # quality of elements used in the animation, other values are "low" and "medium" 
        quality = 'high', 
        # This is just to uniquely identify the animation 
        key = 'Cat' 
    ) 
