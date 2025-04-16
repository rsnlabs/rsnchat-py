from setuptools import setup, find_packages

VERSION = "5.0.0-beta.1"
DESCRIPTION = "A library for interaction with multiple AI models, such as GPT-4, Claude, Gemini, Llama, and others."
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="rsnchat",
    version=VERSION,
    author="rnilaweera",
    author_email="stacxdev@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["python", "first package"],
)