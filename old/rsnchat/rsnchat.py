import requests


class RsnChat:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Please provide an API key")
        self.api_key = api_key
        self._base_url = "https://ai.rnilaweera.ovh/api/v1/user/"

    def _make_request(self, endpoint, prompt):
        url = f"{self._base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"prompt": prompt}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def gpt(self, prompt):
        return self._make_request("gpt", prompt)

    def openchat(self, prompt):
        return self._make_request("openchat", prompt)

    def bard(self, prompt):
        return self._make_request("bard", prompt)

    def gemini(self, prompt):
        return self._make_request("gemini", prompt)

    def codelamma(self, prompt):
        return self._make_request("codellama", prompt)

    def llama(self, prompt):
        return self._make_request("llama", prompt)
    
    def mixtral(self, prompt):
        return self._make_request("mixtral", prompt)

    def prodia(self, prompt):
        return self._make_request("prodia", prompt)
    
    def kandinsky(self, prompt):
        return self._make_request("kandinsky", prompt)

    def absolutebeauty(self, prompt):
        return self._make_request("absolutebeauty", prompt)

    def sdxl(self, prompt):
        return self._make_request("sdxl", prompt)

    def dalle(self, prompt):
        return self._make_request("dalle", prompt)

    def icon(self, prompt):
        return self._make_request("icon", prompt)

