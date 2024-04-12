import os

API_ID = API_ID = 25624473

API_HASH = os.environ.get("API_HASH", "f9064b91dc1331fe9cd614a34eb37de0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6826605668:AAER_9fJYl5lfSDQCkR5gjT9LYWp2408PUI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7064711434)

LOG = -1002122751557

try:
  GROUPS =[]
  for x in (os.environ.get('GROUPS', '-1002025716464 -1002116445692').split()):
    GROUPS.append(int(x))
except ValueError:
    raise Exception("Your AUTH GROUPS list does not contain valid integers.")    

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7064711434 ").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


