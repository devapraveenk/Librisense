from langchain_community.document_loaders import CSVLoader
import tempfile
import streamlit as st
from Base import creation_FAQ_chain,creation_of_vectorDB_in_local,rechatbot

def app():
    def main():
        # st.set_page_config(page_title="SaiScholar",page_icon="😈",layout="wide")
        st.title("SaiScholar: AI-Assisted Library Discovery📚")
        with st.sidebar:
            st.title('Library Assistant')
            st.info('Welcome to the Library Assistant App. Choose your options below')
            st.markdown('---')
            
            option = st.sidebar.selectbox('Make a choice', ['WayFinder','Know about the book'])

        if option=='WayFinder':
            chatbot()
        if option=='Know about the book':
            research()
            
    def research():
        with st.sidebar:
            st.info("Give The name of the book and the author name to know about you books and enjoy")
        
        if "messages" not in st.session_state:
            st.session_state.messages = [{'role':'assistant', 'content':'Hi! How may I assist you today?'}]
        for message in st.session_state.messages:
            with st. chat_message(message["role"]):
                st. write (message["content"])
            
        
        topic = st.chat_input("Enter the book name: ")
        
        if topic:
            st. session_state. messages.append({"role": "user","content": topic})
            with st.chat_message ("user"):
                st.write(topic)
            
            
        if st.session_state.messages[-1]['role']!= 'assistant':
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking🤔..."):
                            repo=rechatbot(topic)
                            
                        st. write(repo)
                        st. session_state.messages. append(
                            {"role": "assistant",
                            "content": repo})
            

    def chatbot():
            main_()

    def csv_loader(tmp_file_path):
                loader=CSVLoader(file_path=tmp_file_path)

                return loader


    def main_():
                # st.set_page_config(page_title="SaiScholar",page_icon="😈",layout="wide")
                # st.title("SaiScholar: AI-Assisted Library Discovery📚")

                with st.sidebar:
                    st.title("Settings")
                    st.markdown('---')
                    st.subheader('Upload Your CSV File')
                    doc=st.file_uploader("Upload your CSV file and Click Process",'csv')

                    if st.button("Process"):
                        with st.spinner("Processing"):
                            if doc is not None:
                                with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                                    tmp_file.write(doc.getvalue())
                                    tmp_file_path = tmp_file.name
                        
                                    st.success(f'File {doc.name} is successfully saved!')
                                
                                load=csv_loader(tmp_file_path)
                                creation_of_vectorDB_in_local(load)
                                st.success("Process Done")
                            else:
                                st.error("❗️Please Upload Your File❗️")
                    
                if "messages" not in st.session_state:
                    st.session_state.messages = [{'role':'assistant', 'content':'Hi! How may I assist you today?'}]
                for message in st.session_state.messages:
                    with st. chat_message(message["role"]):
                        st. write (message["content"])

                query=st.chat_input("Ask the Question")
                if query:
                    st. session_state. messages.append({"role": "user","content": query})
                    with st.chat_message ("user"):
                        st.write(query)
                    
                    
                    

                if st.session_state.messages[-1]['role']!= 'assistant':
                    with st.chat_message("assistant"):
                        with st.spinner("Thinking🤔..."):
                            ans=creation_FAQ_chain()
                            result=ans(query)
                            a=result["result"]
                        st. write(a)
                        st. session_state.messages. append(
                            {"role": "assistant",
                            "content": a})
                


    # if __name__=='__main__':
    main()                