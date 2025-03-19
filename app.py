print("test")

from dotenv import load_dotenv
import os

load_dotenv()

a = os.getenv("USERDOMAIN_ROAMINGPROFILE")
print(a)

