import os 

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage
)

# from dotenv import load_dotenv



# def csv_to_vs(path_to_corpus, oaikey):
#     load_dotenv()
#     os.environ["OPENAI_API_KEY"] = oaikey
#     my_value_a = environ.get('OPENAI_API_KEY')
#     loader = CSVLoader(file_path = path_to_corpus, source_column="filename", encoding='utf-8')
#     data = loader.load()
#     embeddings = OpenAIEmbeddings()
#     docsearch = FAISS.from_documents(data, embeddings)
#     docsearch.save_local("circolari_1")
#     return None


# def get_top_4(myquery, tag = [], destinatari = [] , creazione = []):
#     embeddings = OpenAIEmbeddings()
#     db = FAISS.load_local("circolari_1" , embeddings, allow_dangerous_deserialization=True)
#     # retriever = docsearch.as_retriever(search_kwargs={"k": k})
#     # docs = retriever.get_relevant_documents(query)

#     import pandas as pd
#     df = pd.read_csv("sept1.csv")
        
#     results_with_scores = db.similarity_search_with_score(myquery, k=int(len(df)), fetch_k=int(len(df)) )
#     search_results = []


#     for doc, score in results_with_scores:
#         res = {'Content': doc.page_content, 'Metadata': doc.metadata, 'Score': score}
#         # if doc.metadata['row'] in ok_indeces:
#         #     search_results.append(res)
#         search_results.append(res)


#     return search_results[:4]



def gen_reply(query, context = "", chat_history = ""):
    if len(context) > 0:
        context = f"Contesto:{context}"
    if len(chat_history) > 0:
        chat_history = f"Conversazione:{chat_history}"

    model_name = "gpt-3.5-turbo"
    chat = ChatOpenAI(model_name=model_name, temperature=0, api_key = os.environ.get('OPENAI_API_KEY') )
    question = f"""Sei un chatbot che sta avendo una conversazione con un essere umano.

                    Dati i seguenti estratti e una domanda, crea una risposta finale.

                    {context}

                    {chat_history}

                    Umano: {query}
                    AI:
"""

    response = chat([HumanMessage(content=question)]).content

    chat_history += f'''\nHuman: {query}\nAI:{response}'''
        

    return response, chat_history


# def llm_call(context):
#     from langchain.chat_models import ChatOpenAI
#     from langchain.schema import (
#         HumanMessage
#     )
#     model_name = "gpt-3.5-turbo"
#     chat = ChatOpenAI(model_name=model_name, temperature=0)
#     question = f"""Riassumi in 30 parole il seguente testo.

#                     Testo:{context}"""

#     response = chat([HumanMessage(content=question)]).content

#     return response
