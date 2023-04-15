import gradio as gr
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


def authentication(username, password):
    users = {"user1": "password1", "user2": "password2", "user3": "password3"}
    if username in users and password == users[username]:
        return True
    else:
        return False

def read_pdf(pdf_file):
    pdf_text = ''
    for i, page in enumerate(pdf_file.pages):
        text = page.extract_text()
        if text:
            pdf_text += text

    return pdf_text

def split_text(pdf_text):
    
    text_splitter = CharacterTextSplitter(        
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )

    return text_splitter.split_text(pdf_text)


def aimodel(file, text):
    query = text
    os.environ["OPENAI_API_KEY"] = "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"
    pdf_file = PdfReader(file)

    pdf_text = read_pdf(pdf_file)
    texts = split_text(pdf_text)

    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    docs = docsearch.similarity_search(query)
    return chain.run(input_documents=docs, question=query)

def main(file, text):
    try:
        with open(file.name, 'rb') as f:
            result = aimodel(f, text)
        return result
    except Exception:
        return "Invalid PDF file. Please upload a valid PDF file."

gr.Interface(
    fn=main,
    inputs=[
        gr.inputs.File(label="Upload PDF file ", type="file"),
        gr.inputs.Textbox(label="What is your question?")
    ],
    outputs="text",
    title="PDFGPT",
    description="Upload a file and enter text to prompt PDFGPT",
    auth=authentication

).launch()
