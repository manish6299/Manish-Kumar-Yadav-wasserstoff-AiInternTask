from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
import os  # You may need to install `langchain-openai`


os.environ["OPENAI_API_KEY"] = (
    "sk-schoolaiassistant-IJAus8rOlO5f3hnrBcyuT3BlbkFJ60gsZPoeRzVR0bwKuABN"
)


def create_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_text(text)


def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(chunks, embedding=embeddings)
    db.save_local("vector_db")


def query_rag(question):
    embeddings = OpenAIEmbeddings()
    
    #  Allow loading FAISS pickle 
    db = FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=db.as_retriever())
    return qa.run(question)
