import streamlit as st

st.title("Textbook QA System")

query = st.text_input("Enter your query:")
if query:
    hits = searcher.search(query, k=10)
    documents = [hit.raw for hit in hits]
    scores = re_rank(query, documents)
    ranked_docs = sorted(zip(scores, documents), reverse=True)
    context = " ".join([doc for score, doc in ranked_docs[:5]])
    answer = get_answer_from_llm(context, query)
    
    st.write(f"Answer: {answer}")
    st.write(f"Source: {ranked_docs[0][1]}")  # Display the source of the top-ranked document
