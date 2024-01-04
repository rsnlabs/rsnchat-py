from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

gpt_response = rsn_chat.gpt("hello what is your name?")
print(gpt_response.get('message', ''))