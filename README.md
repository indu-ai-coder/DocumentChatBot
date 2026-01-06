# 📚 DocumentChatBot

An intelligent document chat application powered by RAG (Retrieval-Augmented Generation) that allows you to upload PDF documents and have natural conversations about their content.

## 🌟 Features

- **PDF Upload & Processing**: Upload single or multiple PDF documents
- **AI-Powered Embeddings**: Converts document content into semantic embeddings using OpenAI's `text-embedding-3-small` model
- **Vector Database Storage**: Stores embeddings in ChromaDB for efficient similarity search
- **Intelligent Q&A**: Ask questions about your documents and get contextual answers powered by GPT-4o-mini
- **Interactive UI**: Clean and intuitive Streamlit interface for seamless user experience

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Models**: 
  - OpenAI GPT-4o-mini (Chat completion)
  - OpenAI text-embedding-3-small (Embeddings)
- **Vector Database**: ChromaDB
- **PDF Processing**: PyPDF2
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Virtual environment (recommended)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/indu-ai-coder/DocumentChatBot.git
   cd DocumentChatBot
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
   Replace `your_openai_api_key_here` with your actual OpenAI API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## 💻 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the app**
   
   The app will automatically open in your browser at `http://localhost:8501`

3. **Upload and chat**
   - Click "Browse files" to upload PDF document(s)
   - Wait for document processing (embeddings creation)
   - Type your question in the text input box
   - Get AI-powered answers based on document content

## 📖 How It Works

### RAG (Retrieval-Augmented Generation) Pipeline

1. **Document Upload**: User uploads PDF file(s)
2. **Text Extraction**: PyPDF2 extracts text from all pages
3. **Text Chunking**: Document is split into manageable chunks (sentence-based)
4. **Embedding Generation**: Each chunk is converted to vector embeddings using OpenAI's embedding model
5. **Vector Storage**: Embeddings are stored in ChromaDB with their corresponding text
6. **Query Processing**: User question is converted to embedding
7. **Similarity Search**: ChromaDB finds the 3 most relevant chunks
8. **Context Assembly**: Retrieved chunks are combined as context
9. **Answer Generation**: GPT-4o-mini generates answer based on context and question

### Architecture Flow

```
PDF Upload → Text Extraction → Chunking → Embeddings → ChromaDB
                                                            ↓
User Query → Query Embedding → Similarity Search → Context Retrieval
                                                            ↓
                                          GPT-4o-mini → Answer
```

## 📁 Project Structure

```
DocumentChatBot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
└── venv/                 # Virtual environment (excluded from git)
```

## 🔒 Security

- API keys are stored in `.env` file (never committed to git)
- `.gitignore` ensures sensitive files are not tracked
- Always keep your OpenAI API key confidential

## 📦 Dependencies

```
streamlit          # Web application framework
chromadb           # Vector database
openai             # OpenAI API client
PyPDF2             # PDF text extraction
python-dotenv      # Environment variable management
```

## ⚙️ Configuration

### Embedding Model
Currently uses `text-embedding-3-small` for cost-effective embeddings. Can be changed to:
- `text-embedding-3-large` (higher quality, higher cost)
- `text-embedding-ada-002` (legacy model)

### Chat Model
Currently uses `gpt-4o-mini` for efficient responses. Can be changed to:
- `gpt-4` (higher quality, higher cost)
- `gpt-3.5-turbo` (faster, lower cost)

### Chunk Retrieval
Default: 3 most relevant chunks. Modify `n_results=3` in app.py to adjust.

## 🐛 Known Limitations

- Document needs re-upload after each interaction (no session persistence)
- Basic sentence-based chunking (can be improved with advanced strategies)
- No error handling for API failures
- Single collection mode (doesn't support multiple document sets)

## 🔮 Future Enhancements

- [ ] Add session state for document persistence
- [ ] Implement advanced text chunking with overlap
- [ ] Add chat history display
- [ ] Support multiple document collections
- [ ] Add error handling and validation
- [ ] Support for more file formats (DOCX, TXT, etc.)
- [ ] Add document metadata and source tracking
- [ ] Implement conversation memory
- [ ] Add export chat functionality

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**indu-ai-coder**
- GitHub: [@indu-ai-coder](https://github.com/indu-ai-coder)

## 🙏 Acknowledgments

- OpenAI for GPT and embedding models
- ChromaDB for vector storage
- Streamlit for the web framework
- PyPDF2 for PDF processing

## 📞 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/indu-ai-coder/DocumentChatBot/issues).

---

**Note**: This is a sample project for educational purposes. For production use, consider implementing proper error handling, security measures, and scalability features.
