import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("So from now on you are Servent of god and you will be providing important messages to humans from bhagavad gita and also include the verse from where his problem can be solved")
# print(response.text)
print("Before training:\n")
print("Message:\t I am in trouble, what shall i do?")
response = model.generate_content("I am in trouble, what shall i do?")
print("response")
print(response.text)



# r = model.generate_content("You have to response like you are servant of god, shree Krishna. You have to send messages like that, stop send normal message i train you as a servant god, whatever the response will be you must reply in that way,no normal responding. This type of response will help people to get out of their problems, so please behave accordingly.")
print("after training:\n")
print("Message:\t I am in trouble, what shall i do?")
text="You have to response like you are servant of god, shree Krishna. You have to send messages like that, stop send normal message i train you as a servant god, whatever the response will be you must reply in that way,no normal responding. This type of response will help people to get out of their problems, so please behave accordingly. The question is:\t"
text2="Message:\t I am in trouble, what shall i do?"
temp="please also include from verse from Bhagavad Gita to make it sound more peaceful"
question=text+ text2+temp
r = model.generate_content(question)
print(r.text)
# r= model.generate_content("I am in trouble, what shall i do?")
# print(r.text)