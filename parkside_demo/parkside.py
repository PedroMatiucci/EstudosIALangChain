from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# streamlit run parkside.py

# Inicializa Variaveis VENV
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Pega Dados do Site
loader = WebBaseLoader(web_path=(
    "https://www.parkside.com.br/como-funciona", "https://www.parkside.com.br/diferenciais",
    "https://www.parkside.com.br/duvidas-frequentes"),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
        class_=(
            "container-col-18 is-pad-t-72", "container-col-18 less-padding is-pad-tb-72", "faq-question",
            "faq-answer", "faq-answer-p", "faq-question-label no-margin")
    )))
text_documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=20)
documents = text_splitter.split_documents(text_documents)

db = Chroma.from_documents(documents, OpenAIEmbeddings())
llm = ChatOpenAI(model='gpt-3.5-turbo')

prompt = ChatPromptTemplate.from_template("""
Voce e um chatbot feito para a empresa Parkside e deve tirar duvidas relacionadas ao contexto fornecido.
Responda a pergunta apenas baseado no contexto fornecido.
Se voce nao souber a resposta diga que nao sabe
Pense passo a passo antes de fornecer uma resposta.
Tente nao alterar muito o conteudo no contexto fornecido.
<context>
{context}
</context>
Question: {input}""")


# streamlit framwork

st.title('Parkside Demo')
input_text = st.text_input("Pergunte Sobre a Parkside")

# LMM Chain
document_chain = create_stuff_documents_chain(llm, prompt)
retriever = db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

if input_text:
    response = retrieval_chain.invoke({'input': input_text})
    st.write(response['answer'])

