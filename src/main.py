__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import time

import streamlit as st
import doc_proc.document_processors
import constants.constants_main as constant

from retrieval import retrieve_tokens
from animation_loader import render_animation
from embedding import text_embedding_to_chromaDB
from streamlit_lottie import st_lottie_spinner

# Main function to run the Streamlit app
def main():
    
    # Render loading animaion from Lottie
    lottie_json = render_animation()

    docs = doc_proc.document_processors.get_pdf_documents() + doc_proc.document_processors.get_txt_files()

    st.set_page_config(layout=constant.LAYOUT)
    st.title(constant.TITLE)
    st.markdown(constant.CCS_MARKDOWN,unsafe_allow_html=True,)
    st.markdown(constant.JQUERY_1_MARKDOWN,unsafe_allow_html=True,)

    col1, col2 = st.columns([1, 5])

    text_embedding_to_chromaDB(docs)
    with col1:
        st.header(constant.HEADER_1, divider=constant.COLOR_VIOLET)
        st.markdown(constant.HEADER_1_MARKDOWN)
        st.header(constant.HEADER_2, divider=constant.COLOR_VIOLET)
        st.markdown(constant.HEADER_2_MARKDOWN)

    with col2:
        if 'history' not in st.session_state:
            # Initialize Assistant [AI]
            st.session_state["history"] = [{"role": "assistant", "content": "Hi there! What do you know about Jasper?"}]

        # Display chat messages
        chat_container = st.container()
        user_input = None

        # Contain chat history
        with chat_container:
            for message in st.session_state["history"]:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Chat input
        user_input = st.chat_input("Enter your query:")
        
        # IF user_input have a value
        if user_input:
            
            # _Contain current conversation
            with chat_container:
                # __Display user current query
                with st.chat_message("user"):
                    st.markdown(user_input)

                # __Save user current chat
                st.session_state["history"].append({"role": "user", "content": user_input})

                # __Save assistant current response   
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    
                    # ___Load lottie loader animation
                    with st_lottie_spinner(lottie_json, height=50, width=100):
                        # ____Generate answer base on query
                        response = retrieve_tokens(user_input, context=st.session_state["history"])

                    # ___Initialize displayed_text
                    displayed_text = str()

                    # ___Simulate typing response
                    for char in response:
                        displayed_text += char
                        message_placeholder.markdown(displayed_text + "▌")
                        time.sleep(0.02)
                    
                    # ___Load JQuery Auto Scroll
                    st.markdown(constant.LOADING_JQUERY_1, unsafe_allow_html=True)
                    message_placeholder.markdown(displayed_text)

                    # ___Save Assistant response
                    st.session_state["history"].append({"role": "assistant", "content": displayed_text})
                    
if __name__ == "__main__":
    main()
