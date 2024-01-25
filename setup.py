from setuptools import setup, find_packages

VERSION = '3.0.0' 
DESCRIPTION = 'A package for interacting with GPT4-based chat services, OpenChat, Bard, Gemini, LlaMa, Mixtral, Prodia, Kandinsky, Absolutebeauty, Sdxl, Dalle and AI Icon'
LONG_DESCRIPTION = open("README.md").read()

# Setting up
setup(
  name="rsnchat", 
  version=VERSION,
  author="rnilaweera",
  author_email="stacxdev@gmail.com",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=["requests"],
        
  keywords=['python', 'first package'],
)