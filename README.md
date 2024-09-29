**Project title** - **"Cheeku the chatbot"** <br>
Description: It is a chatbot designed to provide the user meanings, synonyms of words and translations of phrases.

**Installation** <br>
To integrate google translate api, you have to follow the steps given below: <br>
1.Install google cloud sdk <br>
2.Enable google translate api <br>
3.Set up authentication(I used service accounts, you have to change the code a little bit in actions.py if you are going to use another method) <br>
4.Configure environmental variables <br>
5.Install google-cloud-translate. <br>
Optional <br>
Set up a virtual environment(recommended). <br>

**Usage** <br>
I recommend once going through rasa documentation. It will provide you with an understanding of how the project works.For using the chatbot you can go through the following steps: <br>
Run the following commands in two separate terminal windows: <br>
-rasa run --cors "*" <br>
-rasa run actions <br>
Then open the html file linked to the project. Chatbot will be up and running in the default web browser. <br>


**Contributions** <br>
If you are open to contributions, I would suggest the following: <br>
-Train more data in nlu.yml <br>
-Integrate text to speech google api so that pronunciation of words can be done <br>
-There is a scope of improvement in the frontend development of website <br>

