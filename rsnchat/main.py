import requests

class RsnChat:
    api_key: str

    def __init__(self, api_key: str = None):
        if api_key:
            self.api_key = api_key
        self._chat_base_url = "https://rsnlabs.ovh/api/chat/generate"
        self._image_base_url = "https://rsnlabs.ovh/api/image/generate"
        self._models_url = "https://rsnlabs.ovh/api/models"
        self._character_generate_url = "https://rsnlabs.ovh/api/character/girls/generate"
        self._valid_chat_models = None
        self._valid_image_models = None
        self._valid_character_models = None
        self._load_models()

    def _make_request(self, url: str, payload: dict = None, headers: dict = None):
        try:
            if payload:
                response = requests.post(url, json=payload, headers=headers)
            else:
                response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Request failed: {str(e)}")

    def _load_models(self):

        try:
            response = self._make_request(self._models_url)
            self._valid_chat_models = [model["name"] for model in response.get("chat_models", [])]
            self._valid_image_models = [model["name"] for model in response.get("image_models", [])]
            self._valid_character_models = [model["name"] for model in response.get("girls_character_models", [])]
        except ValueError as e:
            raise ValueError(f"Failed to fetch models from API: {str(e)}")

    def generate_chat_response(self, model: str, prompt: str):

        if model not in self._valid_chat_models:
            raise ValueError(f"Invalid chat model. Choose from: {', '.join(self._valid_chat_models)}")

        payload = {
            "model": model,
            "prompt": prompt
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        return self._make_request(self._chat_base_url, payload, headers)

    def generate_image(self, prompt: str, model: str = "default"):

        if model not in self._valid_image_models:
            raise ValueError(f"Invalid image model. Choose from: {', '.join(self._valid_image_models)}")

        payload = {
            "prompt": prompt,
            "model": model
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        return self._make_request(self._image_base_url, payload, headers)

    def list_models(self):

        return self._make_request(self._models_url)

    def generate_character_response(self, model: str, prompt: str):

        if model not in self._valid_character_models:
            raise ValueError(f"Invalid character model. Choose from: {', '.join(self._valid_character_models)}")

        payload = {
            "model": model,
            "prompt": prompt
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        return self._make_request(self._character_generate_url, payload, headers)