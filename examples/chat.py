from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_chat_response("gemini", "Hello, what is your name?")
print(response.get('message', ''))