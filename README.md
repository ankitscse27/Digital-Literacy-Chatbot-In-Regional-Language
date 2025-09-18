# Digital-Literacy-Chatbot-In-Regional-Language
This is a Python Tkinter chatbot by Group 7 for digital literacy. Now in 8 languages (adds Bengali, Tamil, Marathi), it features an enhanced UI with a menu, color-coded chat, clickable links, and a help command. It offers crucial info on online safety, government schemes, an interactive quiz, and more.

# 🤖 Multilingual Digital Literacy Chatbot

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A user-friendly, multilingual desktop chatbot built with Python and Tkinter to promote digital literacy and provide essential information on government schemes and online safety.




---

## ✨ About The Project

This chatbot is designed to bridge the digital divide by offering critical information in multiple Indian languages. Its primary goal is to educate users, particularly those with limited digital exposure, about online safety, digital tools, and beneficial government initiatives. The application features a clean graphical user interface (GUI) and is entirely self-contained, making it easy to run on any desktop.

This project was developed with care by **Group 7**.

---

## 🚀 Key Features

* **🌐 Multi-Language Support**: Fully translated conversations available in:
    * English (`en`)
    * Hindi (`hi`)
    * Hinglish (`hing`)
    * Awadhi (`awa`)
    * Gujarati (`guj`)
    * Bengali (`bn`)
    * Tamil (`ta`)
    * Marathi (`mr`)
* **📚 Core Educational Modules**: Covers essential topics through simple commands:
    * **Digital Literacy (`info`)**: What it is and why it's important.
    * **Online Security (`security`)**: Crucial tips on OTPs, Phishing, strong passwords, and public Wi-Fi.
    * **Government Schemes**: Information and official links for initiatives in **Agriculture (`agri`)**, **Health (`health`)**, **Education (`skills`)**, and **Sanitation (`sanitation`)**.
    * **National Initiatives**: Details on `digital_india` and `make_in_india`.
* **📝 Interactive Quiz**: A 5-question quiz (`quiz`) to test and reinforce the user's knowledge of online safety.
* **🚨 Emergency Helplines**: A quick command (`emergency`) to list all-in-one emergency numbers, police, ambulance, and more.
* **😄 Fun & Utility Features**:
    * Get a random, language-appropriate **joke** (`joke`).
    * Generate a placeholder **image** from a text prompt (`image`).
    * Check the current **time**, **date**, and simulated **weather**.
* **💬 Basic NLP Sentiment Analysis**: Uses `TextBlob` to provide friendly, sentiment-aware responses to non-command inputs.
* **🔗 Clickable Hyperlinks**: Automatically detects and renders URLs as clickable links within the chat window.
* **📝 Conversation Logging**: All interactions are automatically saved to `chat_log.json` for review.

---

## 🛠️ Technology Stack

* **[Python](https://www.python.org/)**: Core programming language.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: For the graphical user interface (GUI).
* **[TextBlob](https://textblob.readthedocs.io/)**: For basic Natural Language Processing (NLP) and sentiment analysis.

---

## ⚙️ Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

Make sure you have Python 3 installed on your system.
```sh
python --version
```

### Installation

1.  **Clone the repository:**
    
    git clone [https://github.com/your-username/your-repository-name.git]
    
2.  **Navigate to the project directory:**
    
    cd your-repository-name
    
3.  **Install the required Python packages:**
    The only external dependency is `TextBlob`.
    ```sh
    pip install textblob
    ```
4.  **Download necessary NLTK corpora for TextBlob:**
    Run this command in your terminal. This is a one-time setup that downloads the models needed for sentiment analysis.
    ```sh
    python -m textblob.download_corpora
    ```
5.  **Run the application:**
    ```sh
    python your_script_name.py
    ```
    *(Replace `your_script_name.py` with the actual name of your Python file).*

---

##  kullanım

1.  Launch the application by running the Python script.
2.  You will be greeted with a language selection screen. Choose your preferred language.
3.  The main chat window will open. Type `help` to see a full list of available commands.
4.  Interact with the bot by typing commands like `quiz`, `security`, `agri`, etc.
5.  Use the "Options" menu to change the language or clear the chat history at any time.

---

## 📂 Project Structure

```
your-repository-name/
│
├── your_script_name.py     # Main application script
├── chat_log.json           # Stores conversation logs (created on first run)
├── .gitignore              # Specifies files for Git to ignore
└── README.md               # You are here!
```

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 🙏 Acknowledgments

* This project was created by **Group 7**.
* @ankitscse27
* @Anuragtiwari018
* @anupyadav14
* @arpitpatelcell
* Hat tip to the creators of the `TextBlob` library.
