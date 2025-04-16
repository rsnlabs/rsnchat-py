<h1 align="center"><b>RsnChat</b> <img src="https://i.ibb.co/0J89TrT/rsn-bot-1.png" width="30" style="border-radius: 50%; margin-bottom: -5px"></h1>
<p align="center"><i>The ultimate AI-powered RsnChat Phyton</i></p>

This package package for interacting with the Rsn Labs API. It supports generating chat responses, images, and interacting with female character models.

## Installation

You can install the package via Pypi

```bash
pip install rsnchat
```

---


# APIKEY

Discord : [https://api.rnilaweera.lk/discord](https://api.rnilaweera.lk/discord)

Join discord server and create account with **/register** slash command and get your apikey with **/generate-key** slash command for free!

---

## Generating Chat Responses

You can generate responses using the available chat models.

Valid models: `gemini`, `claude`, `deepseek-v3`, `gpt`, `deepseek-r1`, `llama`, `grok-3`, `grok-3-r1`, `gpt4`.

Example:

```python
from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_chat_response("gemini", "Hello, what is your name?")
print(response.get('message', 'Error: Could not generate the response'))
```

---

## Generating Images

You can generate images using different models for specific styles.

Valid models: `rsnlabs`, `flux`, `anime`, `disney`, `cartoon`, `photography`, `icon`, `ghibli`.

Example:

```python
from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_image("A futuristic city at night with neon lights", "flux")
print(response.get('image_url', 'Error: Could not generate the image'))
```

---

## Listing Available Models

The API allows you to list all available models, including chat, image, and female character models.

Example:

```python
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
```

---

## Generating Responses with Female Character Models

You can interact with female character models. Each character has a profile picture and responds based on the provided prompt.

Valid models: `amaya`, `ana`, `carla`, `delicia`, `ember`, `mariya`, `summer`, `naomi`.

Example:

```python
from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")
response = rsn_chat.generate_character_response('amaya', 'Hello, how are you doing today?')

print(f"Profile Pic: {response.get('profile_pic', 'Error: No profile picture available')}")
print(f"Response: {response.get('response', 'Error: Could not generate the message')}")
```

---

## Error Handling

If an invalid model is provided, the SDK will raise a `ValueError` with a detailed message listing the valid models.

Example:

```python
from rsnchat import RsnChat

rsn_chat = RsnChat("rsnlabs_××××××××××××××××××××××")

try:
    response = rsn_chat.generate_chat_response("invalid_model", "Test prompt")
except ValueError as e:
    print(f"Error: {e}")
```

---