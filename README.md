# rsnchat

This package package for interacting with GPT4-based chat services, OpenChat, Bard, Gemini and LlaMa without restrictions or limits

## Installation

You can install the package via Pypi

```bash
pip install rsnchat
```

## Usage GPT4

```python

from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

gpt_response = rsn_chat.gpt("hello what is your name?")
print(gpt_response.get('message', ''))
```

## Usage OpenChat

```python

from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

openchat_response = rsn_chat.openchat("hello what is your name?")
print(openchat_response.get('message', ''))
```

## Usage Bard

```python

from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

bard_response = rsn_chat.bard("hello what is your name?")
print(bard_response.get('message', ''))
```

## Usage Gemini

```python

from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

gemini_response = rsn_chat.gemini("hello what is your name?")
print(gemini_response.get('message', ''))
```

## Usage LlaMa

```python

from rsnchat import RsnChat

rsn_chat = RsnChat("chatgpt_××××××××××××××××××××××")

llama_response = rsn_chat.llama("hello what is your name?")
print(llama_response.get('message', ''))
```

# APIKEY

Discord : [https://discord.gg/r5QWdKfQxr](https://discord.gg/r5QWdKfQxr)

Join discord server and create account with **/new** slash command and get your apikey with **/key** slash command for free!
