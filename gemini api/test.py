import os
from dotenv import load_dotenv
load_dotenv() 
temp=os.environ['API_KEY']
print(temp)