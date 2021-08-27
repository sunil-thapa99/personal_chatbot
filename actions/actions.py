# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class Name(Action):
    def name(self):
        return "action_name"
        
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name= tracker.get_slot("name")
        messages = f"Hi {name}, do you have a treat for me? I really like treats, master doesn't give me many treats because he thinks I'm chubby."

        buttons = [
            {"title":"Give Treat","payload":"i will give treat"},
            {"title":"Don't Give Treat","payload":"sorry no treat for you"}
        ]

        # reply = random.choice(messages)
        dispatcher.utter_message(text=messages,buttons=buttons)
        return []

class Treat(Action):
    def name(self):
        return "action_treat"
        
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = "Woof! That was yummy! What was that? \nNow that you're not a stranger, what would you like to talk about? I know a lot about masters. What do you want to know?"
        
        buttons = [
            {"title":"About","payload":"tell me about master"},
            {"title":"Work","payload":"work about master"}
        ]

        # reply = random.choice(messages)
        dispatcher.utter_message(text=messages,buttons=buttons)
        return []

class NoTreat(Action):
    def name(self):
        return "action_no_treat"
        
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = "That's okay. I'll break into the treat jar later. \nNow that you're not a stranger, what would you like to talk about? I know a lot about master. What do you want to know?"
        
        buttons = [
            {"title":"Who is Master?","payload":"master name"},
            {"title":"Work","payload":"work about master"}
        ]

        dispatcher.utter_message(text=messages,buttons=buttons)
        return []

class WhoMaster(Action):
    def name(self):
        return "action_who_master"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = "Oh boy oh boy! I love talking about Master. \nYou can call him Master too, but everyone else calls him Sunil. \n🤗"
        
        buttons = [
            {"title":"About","payload":"tell me about master"},
            {"title":"Contact","payload":"tell me about master"},
            {"title":"Education","payload":"tell me about master"},
            {"title":"Work","payload":"work about master"}
        ]

        dispatcher.utter_message(text=messages, buttons=buttons)
        return []

class AboutMaster(Action):
    def name(self):
        return "action_about"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = '''Master was born in Melamchi-02, Sindhupalchowk, Nepal in 17th March 1999. 
                        The family moved to the capital, Kathmandu when master was only 2 years old. 
                        His dad bought him his first personal computer ..an i3 Dell Inspiron. 
                        From then on, he was hooked. \n \n
                        In middle school, he learned programming in QBASIC, then shifted into HTML and CSS in order to learn more about programming. After getting enrolled for his Bachelors, he was then introduced into various programming language such as Java, C++, Python, Matlab, JS and so on. 
                        He spent initial phase designing websites till he decided it wasn't his thing, so he dabbling in programming instead. He wanted to become an AI Developer. \n \n
                        Master is an aspiring computer vision engineer who enjoys connecting the dots: be it ideas from different disciplines, people from different teams, or applications from different industries. He has strong technical skills and an academic background in software engineering, statistics, and machine learning.
                    '''
        
        buttons = [
            {"title":"Contact","payload":"tell me about master"},
            {"title":"Education","payload":"tell me about master"},
            {"title":"Work","payload":"work about master"}
        ]

        dispatcher.utter_message(text=messages)
        return []

class WorkMaster(Action):
    def name(self):
        return "action_work"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = '''Master's career started with performing CRUD operation for digitizing governmental forms using Laravel. He worked for Malika Incorporate Pvt. Ltd. as an junior web developer. \n \n
                        After graduating, he did internship at InfoDevelopers Pvt. Ltd as a software engineer within the field of AI. There, he got full-time as a junior software engineer. 
                        Then he was promoted to Software Engineer.  \n \n
                        Master had the opportunity to lead the projects to take the Machine Learning projects right from Research to Implementation and Deployment.  \n \n
                        Currently, Master is preparing for further studies, and refining his technical skills, brain-storming, participating in Hackathons, pitching ideas in Fuse AI Expo, being in the Omdena community as a Junior ML Engineer.  \n \n
                        He states, "Being a part of the Omdena community, we worked on Using AI to Analyze Domestic Violence and Online Harassment During Covid-19 collaborating with Red Dot Foundation."
                    '''
        
        buttons = [
            {"title":"About","payload":"tell me about master"},
            {"title":"Contact","payload":"tell me about master"},
            {"title":"Education","payload":"tell me about master"},
        ]

        dispatcher.utter_message(text=messages)
        return []

class EducationMaster(Action):
    def name(self):
        return "action_education"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        messages = '''Master completed his primary and secondary schooling from Gorakhshya Nikhil Jyoti Divya Vidhyashram and the National School of Sciences (NIST) respectively. \n \n
                        He completed a BSc (Hons) Computing (Software Engineering) from Naaya Aayam Multi-Disciplinary Institute (NAMI), partnered with the University of Northampton, the UK, graduating with a First Class Honors degree. 
                        According to the WES evaluation, he obtained a 3.87 GPA out of 4.
                    '''
        
        data = [
            {"title": "Primary and Middle School", "description": "Master went to Gorakhshya Nikhil Jyoti Divya Vidhyashram. "}
        ]

        buttons = [
            {"title":"About","payload":"tell me about master"},
            {"title":"Contact","payload":"tell me about master"},
            {"title":"Education","payload":"tell me about master"},
        ]

        dispatcher.utter_message(text=messages)
        return []


class DownloadPdf(Action):
    def name(self):
        return "download_pdf"
        
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        messages = ["Here's the link to the resume!!!",]
        data = {
            'payload': "pdf_attachment",
            'title': 'CV',
            'url': 'https://juventudedesporto.cplp.org/files/sample-pdf_9359.pdf'
        }

        reply = random.choice(messages)
        dispatcher.utter_message(text=reply, json_message=data)
        return []

class AboutBot(Action):
    def name(self):
        return "action_about_bot"
    
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        messages = ["I am a bot to help you ease your shopping experience",
                    "I am your virtual assistant to give you a smooth shopping experience 😁"]
        
        reply = random.choice(messages)
        dispatcher.utter_message(text=reply)
        return []

class Goodbye(Action):
    def name(self):
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        question = tracker.latest_message['text']
        messages = ['Thank you, 😁 I am happy to help you. 👋',
                    'I hope I was helpful for you. 👋😁']

        reply = random.choice(messages)
        dispatcher.utter_message(text=reply)
        return []
