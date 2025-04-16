from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_character_response('amaya', 'Hello, how are you doing today?')
print(response.get('profile_pic', 'Error: No profile picture available'))
print(response.get('message', 'Error: Could not generate the message'))