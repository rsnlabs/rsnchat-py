from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_image("A futuristic city at night with neon lights", "flux")
print(response.get('image_url', 'Error: Could not generate the image'))