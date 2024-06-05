import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.sql_database import SQLDatabase
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain_experimental.sql import SQLDatabaseChain
import streamlit as st
def main():
    username = "root"
    password = "devapraveen"
    host = "localhost"
    database = "bookdb"

    db=SQLDatabase.from_uri(f"mysql+pymysql://{username}:{password}@{host}/{database}")

    few_shots = [
        {'Question' : "what is the count of book name Software Architecture Patterns",
        'SQLQuery' : "SELECT book_count FROM books WHERE book_name = 'Software Architecture Patterns'",
        'SQLResult': "Result of the SQL query",
        'Answer' : '6'},
        {'Question': "what is the count of book name Python Crash Course",
        'SQLQuery':"SELECT book_count FROM books WHERE book_name = 'Python Crash Course'",
        'SQLResult': "Result of the SQL query",
        'Answer': '10'},
        {'Question': "what is the count of book name SQL for Beginners: Learn SQL using MySQL and Database Management" ,
        'SQLQuery' : """SELECT book_count FROM books WHERE book_name ='SQL for Beginners: Learn SQL using MySQL and Database Management'
    """,
        'SQLResult': "Result of the SQL query",
        'Answer': '12'} ,
        {'Question' : "what is the count of book name Computer Networking: A Top-Down Approach" ,
        'SQLQuery': "SELECT book_count FROM books WHERE book_name ='Computer Networking: A Top-Down Approach'",
        'SQLResult': "Result of the SQL query",
        'Answer' : '6'},
        {'Question': "what is the count of book name Artificial Intelligence: A Modern Approach",
        'SQLQuery' : "SELECT book_count FROM books WHERE book_name ='Artificial Intelligence: A Modern Approach'",
        'SQLResult': "Result of the SQL query",
        'Answer' : '5'
        }
    ]

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embeddings, metadatas=few_shots)



    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )

    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    No pre-amble.
    """
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )
    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"], #These variables are used in the prefix and suffix
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.2
    )

    new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

    st.title('Chat with LibDB')
    query=st.text_input("Enter")
    if query:
        res=new_chain(query)
        st.write('answer',res['result'])
main()