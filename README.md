### **Project Title: Cheeku - The Conversational Chatbot**

#### **Overview**:
Cheeku is an interactive chatbot designed to assist users in finding word definitions, synonyms, and translating phrases between languages. It's built to help with quick language-related queries and supports multilingual translation capabilities.

#### **Setup & Installation**:
To integrate Google Translate API into the project, follow these steps:

1. Install the **Google Cloud SDK** to interact with Google's cloud services.
2. Enable the **Google Translate API** through the Google Cloud Console.
3. Set up authentication. This project uses **service accounts** by default, but you can modify the code in `actions.py` if you're using another authentication method.
4. Configure your system’s environment variables to include the necessary API credentials.
5. Install the `google-cloud-translate` package using pip.

**Optional but Recommended:**
- Set up a virtual environment for your project to manage dependencies effectively.

#### **How to Use**:
Before using the chatbot, it's a good idea to familiarize yourself with the Rasa framework by reviewing the [Rasa documentation](https://rasa.com/docs/). Once ready, follow these steps to run the chatbot:

1. Open two terminal windows.
2. In one terminal, run:
   ```bash
   rasa run --cors "*"
   ```
3. In the second terminal, execute:
   ```bash
   rasa run actions
   ```
4. Finally, open the accompanying HTML file in your web browser. Your chatbot will now be accessible, ready to assist with your language queries!

#### **Future Improvements & Contributions**:
Contributions to this project are welcome! Some areas that can be enhanced include:
- Expanding the training data in the `nlu.yml` file for better user interaction.
- Integrating the Google **Text-to-Speech API** for voice-based responses, enabling users to hear pronunciations.
- Improving the design and functionality of the frontend to create a better user experience.

