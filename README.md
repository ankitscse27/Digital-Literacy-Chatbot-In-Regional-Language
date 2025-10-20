# 🤖 Multilingual Digital Literacy Chatbot

A user-friendly, multilingual desktop chatbot built with **Python** and **Tkinter** to promote digital literacy, online safety, and awareness of government schemes in regional Indian languages. Developed by **Group 7**.

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## ✨ Why This Project Matters

This chatbot is designed to **bridge the digital divide** by making critical information accessible in multiple Indian regional languages. It provides essential, self-contained educational resources on online safety, digital tools, and beneficial government initiatives through a clean, intuitive Graphical User Interface (GUI).

---

## 🚀 Key Features

* **🌐 8-Language Support**: Fully translated content for:
    * English (`en`)
    * Hindi (`hi`)
    * Hinglish (`hing`)
    * Awadhi (`awa`)
    * Gujarati (`guj`)
    * **Bengali** (`bn`)
    * **Tamil** (`ta`)
    * **Marathi** (`mr`)
* **📚 Core Educational Modules**: Access information on:
    * **Digital Literacy** (`info`)
    * **Online Security** (`security`): Tips on OTPs, Phishing, strong passwords, and public Wi-Fi.
    * **Government Schemes**: Details for Agriculture (`agri`), Health (`health`), Education (`skills`), and Sanitation (`sanitation`).
    * **National Initiatives**: `digital_india` and `make_in_india`.
* **📝 Interactive Learning**: Includes a **5-question quiz** (`quiz`) to test online safety knowledge.
* **🚨 Emergency Helplines**: Quick access to vital emergency numbers (`emergency`).
* **💬 Enhanced UI/UX**: Features color-coded chat, **clickable hyperlinks**, a robust help command, and conversation logging to `chat_log.json`.
* **🧠 Basic Sentiment Analysis**: Uses `TextBlob` to provide friendly, sentiment-aware responses to general conversation.

---

## 🛠️ Technology Stack

* **[Python](https://www.python.org/)**: Core programming language.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: For the desktop Graphical User Interface (GUI).
* **[TextBlob](https://textblob.readthedocs.io/)**: For basic Natural Language Processing (NLP) and sentiment analysis.

---

## ⚙️ Getting Started

Follow these steps to set up and run the chatbot on your local machine.

### Prerequisites

Ensure you have **Python 3.x** installed.

### Installation

1.  **Clone the repository:**
  
    git clone [https://github.com/ankitscse27/Digital-Literacy-Chatbot-In-Regional-Language.git]
    cd Digital-Literacy-Chatbot-In-Regional-Language

    2.  **Install dependencies:** The only external dependency is `TextBlob`.
    ```sh
    pip install textblob
    ```
3.  **Download NLTK corpora:** This is a one-time step for sentiment analysis models.
    ```sh
    python -m textblob.download_corpora
    ```
4.  **Run the application:**
    ```sh
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with your main script file name.)*

---

## 💻 How to Use

1.  Launch the application and select your preferred language from the initial screen.
2.  In the main chat window, type `help` to view a complete list of commands.
3.  Interact by typing commands such as `quiz`, `security`, or `agri`.
4.  Use the "Options" menu to change the language or clear the chat history at any time.

---

## 🤝 Contributing

We welcome contributions! Please refer to the `CONTRIBUTING.md` file for detailed guidelines.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add a new command'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See the `LICENSE` file for more information.

---

## 🙏 Acknowledgments

* This project was developed by **Group 7**.
* Special thanks to the contributors: @ankitscse27, @Anuragtiwari018, @anupyadav14, @arpitpatelcell.
* Hat tip to the creators of the `TextBlob` library.
