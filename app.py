print("test")

from dotenv import load_dotenv
import os,random

load_dotenv()

a = os.getenv("USERDOMAIN_ROAMINGPROFILE")
print(a)

