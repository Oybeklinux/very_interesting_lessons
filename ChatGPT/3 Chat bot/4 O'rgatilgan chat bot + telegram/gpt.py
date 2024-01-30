# !pip install langchain
# !pip install openai
# !pip install faiss-cpu
# !pip install tiktoken
# !pip install -U langchain-openai
# pip install python-docx

import os
from docx import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# API kalit
os.environ["OPENAI_API_KEY"] = "Sizning kalitingiz"

# docs file yo'li
docx_files = ['fayllar/flutter.docx', 'fayllar/js.docx', 'fayllar/python.docx', "fayllar/savol_javob.docx"]

# DOCX ma'lumotlarini raw_text o'zgaruvchisiga o'qib olish
raw_text = ""
for docx_file in docx_files:
    doc = Document(docx_file)

    for paragraph in doc.paragraphs:
        raw_text += paragraph.text + "\n"

# matnni tokenlarga bo'lib olamiz. Bi ChatGPT talabidan chetga chiqib ketmaslik uchun
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
)
texts = text_splitter.split_text(raw_text)

# embeddingni yuklab olish - bu machine learning modellari va algoritmlari osongina foydalanishi mumkin bo'lgan ma'lumotlarni maxsus formatidir.
# Embedding - bu matn bo'lagi semantik ma'nosining zichlashtirilgan ifodasidir
embeddings = OpenAIEmbeddings()

# FAISS (Facebook AI oʻxshashlik qidiruvi) bu kutubxona boʻlib, ishlab chiquvchilarga bir-biriga oʻxshash multimedia hujjatlarini tezda izlash imkonini beradi.
docsearch = FAISS.from_texts(texts, embeddings)

# LangChain - bu til modellari asosida ishlaydigan ilovalarni ishlab chiqish uchun framework.
from langchain.chains.question_answering import load_qa_chain
from langchain_openai.llms import OpenAI

# OpenAI-llm
# Hujjatlar to'plami bo'yicha Savol Javob qilish uchun foydalanishingiz mumkin bo'lgan zanjirni yuklaydi
chain = load_qa_chain(OpenAI(), chain_type="stuff")


def get_answer(query):
    # https://www.pinecone.io/learn/what-is-similarity-search/
    # vektor ko'rishdagi raqamlarni solishtirish

    docs = docsearch.similarity_search(query)
    result = chain.invoke({"input_documents": docs, "question": query}, return_only_outputs=True)
    return result['output_text']
