<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BTU Knowledge Assistant</title>
</head>
<body style="font-family: Arial, sans-serif; color: #333; background-color: #f5f5f5; padding: 20px;">

    <h1 style="color: #b30000;">BTU Knowledge Assistant</h1>

    <p><strong>BTU Knowledge Assistant</strong> is a custom-built Retrieval-Augmented Generation (RAG) chatbot designed to answer questions about the Business Technology Unit (BTU) and product management using internal documents, PDFs, Word files, and even YouTube video transcripts.</p>

    <h2 style="color: #b30000;">🔧 Features</h2>
    <ul>
        <li>RAG-powered chatbot using OpenAI and LangChain</li>
        <li>Supports PDF, Word documents, and YouTube videos</li>
        <li>Built with Streamlit for easy interaction</li>
        <li>Deployed via Streamlit Cloud (or intranet)</li>
        <li>Branded with red and grey color scheme for BTU identity</li>
    </ul>

    <h2 style="color: #b30000;">📁 Folder Structure</h2>
    <pre style="background-color: #eee; padding: 10px; border: 1px solid #ccc;">
BTU_Chatbot/
├── app.py                # Streamlit frontend
├── faiss_index/          # Folder for FAISS vector store
├── requirements.txt      # Python dependencies
├── logo.jpeg             # BTU logo file
└── README.md             # Project documentation
    </pre>

    <h2 style="color: #b30000;">🚀 How to Run Locally</h2>
    <ol>
        <li>Clone the repo</li>
        <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Run the app: <code>streamlit run app.py</code></li>
    </ol>

    <h2 style="color: #b30000;">🔐 API Key</h2>
    <p>Make sure to set your <code>OPENAI_API_KEY</code> environment variable before launching.</p>

    <h2 style="color: #b30000;">🌐 Deployment</h2>
    <ul>
        <li><strong>Streamlit Cloud:</strong> Upload your repo and deploy directly.</li>
        <li><strong>Intranet Server:</strong> Use <code>streamlit run app.py</code> on your internal server for access via IP.</li>
    </ul>

    <h2 style="color: #b30000;">🧠 Powered By</h2>
    <ul>
        <li>LangChain</li>
        <li>FAISS</li>
        <li>OpenAI (GPT-3.5/4)</li>
        <li>Streamlit</li>
    </ul>

    <p style="margin-top: 40px;"><em>Developed by Chinwe Vivian Aliyu for the Business Technology Unit (BTU).</em></p>

</body>
</html>

