🧠 BTU Knowledge Assistant Chatbot
BTU Knowledge Assistant is a custom RAG-based (Retrieval-Augmented Generation) chatbot designed to answer questions about the Business Technology Unit (BTU) and its work — including how it relates to product management.

Built using:

🔗 LangChain

🧠 OpenAI API

📦 FAISS Vector Store

🎨 Streamlit (for the user interface)

☁️ Streamlit Cloud / Intranet deployment

📌 Features
✅ RAG-powered conversational assistant

✅ Answers grounded in internal docs (PDFs, Word files)

✅ Integrated product management references

✅ Styled in official BTU brand colors (grey and red)

✅ Embeds company logo and supports friendly interactions

✅ Can be deployed on the intranet or online via Streamlit Cloud

📂 Folder Structure

BTU_Chatbot/
│
├── app.py                  # Streamlit web app
├── faiss_index/            # Vector store of embedded documents
├── requirements.txt        # Dependencies for Streamlit Cloud
├── btu_logo.jpeg           # BTU Logo
└── README.md               # You're here!

🚀 How to Run (Locally)
1. Clone the repo
git clone https://github.com/your-username/BTU_Chatbot.git
cd BTU_Chatbot
2. Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
pip install -r requirements.txt
4. Set your OpenAI API key
export OPENAI_API_KEY='your-api-key-here'  # on Linux/Mac
# set OPENAI_API_KEY=your-api-key-here     # on Windows
5. Run the app
streamlit run app.py


🌐 Deploy via Streamlit Cloud
Push your repository to GitHub

Go to Streamlit Cloud

Connect your repo and set:

Main file: app.py

Secrets: Add OPENAI_API_KEY under app settings

Launch your app and share the link!

🛡 Security Notes
Make sure your OPENAI_API_KEY is stored as an environment variable or inside Streamlit Cloud secrets.

If deploying internally, remove any public-facing APIs and restrict access via your company’s intranet firewall.


💡 Future Improvements
Support for multiple knowledge bases

Admin panel for uploading new documents

Integration with internal staff directory or ticketing system

👩🏽‍💻 Project Maintainer
Chinwe Vivian Aliyu
Head of Business Technology Unit (BTU)
Federal Inland Revenue Service, Nigeria
WiDS Ambassador • Data Scientist • Mentor 
