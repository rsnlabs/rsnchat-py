import requests

class RsnChat:
    api_key: str
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Please provide an API key")
        self.api_key = api_key
        self._base_url = "https://api.rsnai.org/api/v1/user/"

    def _make_request(self, endpoint: str, prompt: str):
        url = f"{self._base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        payload = {"prompt": prompt}
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_message = response.json().get("error", {}).get("message", str(e))
            raise ValueError(f"Request failed: {error_message}")

    def gpt(self, prompt: str):
        return self._make_request("gpt", prompt)

    def openchat(self, prompt: str):
        return self._make_request("openchat", prompt)

    def bard(self, prompt: str):
        return self._make_request("bard", prompt)

    def gemini(self, prompt: str):
        return self._make_request("gemini", prompt)

    def codellama(self, prompt: str):
        return self._make_request("codellama", prompt)

    def llama(self, prompt: str):
        return self._make_request("llama", prompt)
        
    def mixtral(self, prompt: str):
        return self._make_request("mixtral", prompt)
    
    def claude(self, prompt: str):
        return self._make_request("claude", prompt)

    def prodia(self, prompt: str):
        return self._make_request("prodia", prompt)
    
    def kandinsky(self, prompt: str):
        return self._make_request("kandinsky", prompt)

    def absolutebeauty(self, prompt: str):
        return self._make_request("absolutebeauty", prompt)

    def sdxl(self, prompt: str):
        return self._make_request("sdxl", prompt)

    def dalle(self, prompt: str):
        return self._make_request("dalle", prompt)

    def icon(self, prompt: str):
        return self._make_request("icon", prompt)
    