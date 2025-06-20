
import streamlit as st
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Set your API key
OPENAI_API_KEY = "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"

# Load the vector store (created earlier in Colab)
vector_store = FAISS.load_local(
    "faiss_index",
    OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY),
    allow_dangerous_deserialization=True
)

# Set up the LLM
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# Create the retrieval + generation chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
    chain_type="stuff"
)

# Streamlit UI
st.set_page_config(page_title="BTU Assistant", layout="centered")
st.title("BTU Knowledge Assistant")
st.markdown("Ask me anything about the Business Technology Unit or Product Management!")

question = st.text_input("Your Question", placeholder="e.g. What does BTU do?")


if question:
    greetings = ["hello", "hi", "hey", "how are you", "good morning", "good afternoon", "good evening"]
    cleaned_question = question.strip().lower()

    if cleaned_question in greetings:
        st.success("Answer:")
        st.write("👋 Hello! I’m your BTU Assistant. Feel free to ask me anything about our team's work or product management.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = qa_chain.run(question)
                if not answer.strip() or "I don't know" in answer.lower():
                    st.warning("🤖 Sorry, I could not find an answer to that based on what I know. Try rephrasing or ask something about BTU or product management.")
                else:
                    st.success("Answer:")
                    st.write(answer)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

