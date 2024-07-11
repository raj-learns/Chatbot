import nltk
nltk.download('wordnet')
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from nltk.corpus import wordnet
from google.cloud import translate_v2 as translate

assert 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ, "GOOGLE_APPLICATION_CREDENTIALS environment variable not set."
#Stops the program if authentication is not done.
LANGUAGE_CODES = {
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Italian': 'it',
    'Hindi': 'hi',
    'Kannada':'kn',
    'Malayalam': 'ml',
    'Tamil':'ta',
    'Telugu':'te'
}


class ActionDefineWord(Action):
    def name(self) -> Text:
        return "action_define_word"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        def_word = tracker.get_slot("def_word")
       # print(f"Debug: def_word slot value is {def_word}")  # Debugging statement

        if not def_word:
            response = "I need a word to define."
            dispatcher.utter_message(text=response)
            return []

        synsets = wordnet.synsets(def_word)
        if synsets:
            definition = synsets[0].definition()

            examples = synsets[0].examples()
            if examples:
                ex = '; '.join(examples)
                response = f"The definition of '{def_word}' is '{definition}'. Examples: {ex}."
            else:
                response = f"The definition of '{def_word}' is '{definition}'."

        else:
            response = "Sorry, I couldn't find the definition and synonyms for that word."

        dispatcher.utter_message(text=response)
        return []

class ActionSynonymWord(Action):
    def name(self) -> Text:
        return "action_synonym_word"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        syn_word = tracker.get_slot("syn_word")
       # print(f"Debug: syn_word slot value is {syn_word}")  # Debugging statement

        if not syn_word:
            response = "I need a word to find synonyms for."
            dispatcher.utter_message(text=response)
            return []

        synsets = wordnet.synsets(syn_word)
        if synsets:
            synonyms = set()
            for synset in synsets:
                for lemma in synset.lemmas():
                    synonyms.add(lemma.name())
            synonyms_list = ', '.join(synonyms)
            response = f"Synonyms of '{syn_word}' include: {synonyms_list}."

        else:
            response = f"Sorry, I couldn't find synonyms for '{syn_word}'."

        dispatcher.utter_message(text=response)
        return []


class ActionTranslateWord(Action):
    def name(self) -> Text:
        return "action_translate_word"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        tra_word = tracker.get_slot('tra_word')
        lang = tracker.get_slot('lang')
       # print(f"Debug: tra_word slot value is {tra_word}, lang slot value is {lang}")  

        if not tra_word or not lang:
            response = "I need both a word and a language to translate."
            dispatcher.utter_message(text=response)
            return []
            
        lang_code = LANGUAGE_CODES.get(lang.capitalize())
        if not lang_code:
            response = f"Sorry, I don't support the language '{lang}'."
            dispatcher.utter_message(text=response)
            return []

        translate_client = translate.Client()

        try:
            result = translate_client.translate(tra_word, target_language=lang_code)
            translation = result['translatedText']
            response = f"The translation of '{tra_word}' in {lang} is: '{translation}'."
            dispatcher.utter_message(text=response)
        except Exception as e:
            response = f"Sorry, there was an error with the translation service: {str(e)}"
            dispatcher.utter_message(text=response)

        return []
