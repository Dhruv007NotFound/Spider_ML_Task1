import streamlit as st
from RetrievalPipeline import Question_Answer
import time
st.title(":blue[QueryAI]")

if "messages" not in st.session_state:
    st.session_state.messages=[]



if not st.session_state.messages:
    st.markdown(
    """
        <div style='text-align:center; padding-top:150px;'>
            <h1>Hello User 👋</h1>
            <p>Welcome to QueryAI !!</p>
        </div>
        """,
        unsafe_allow_html=True
    )    
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])


if query:= st.chat_input("Type query"):
    with st.chat_message('User'):
        st.write(f"Querry : {query}")
    st.session_state.messages.append({'role':'User','content':query})

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            Ans, source= Question_Answer(query)
            st.subheader("Answer :")
            st.write(Ans)
            if Ans!="I do not have sufficient information to provide an answer":
                st.subheader("Sources :")
                for s in source.keys():
                    st.write(f"{s} : Pages - {source[s]}")
    st.session_state.messages.append({'role':'assistant','content':Ans})

    
    



