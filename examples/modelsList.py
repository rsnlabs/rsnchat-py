from rsnchat import RsnChat

rsn_chat = RsnChat()

response = rsn_chat.list_models()

if response:
    print("Chat Models:")
    for chat_model in response.get('chat_models', []):
        print(f" - {chat_model['name']} (Status: {chat_model['status']})")

    print("\nImage Models:")
    for image_model in response.get('image_models', []):
        print(f" - {image_model['name']} (Status: {image_model['status']})")

    print("\nGirls Character Models:")
    for girl_model in response.get('girls_character_models', []):
        print(f" - {girl_model['name']} (Status: {girl_model['status']})")
        print(f"   Profile Pic: {girl_model['profile_pic']}")

    print(f"\nPowered By: {response.get('powered_by', 'Unknown')}")
else:
    print("Failed to fetch the models.")