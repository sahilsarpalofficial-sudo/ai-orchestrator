import os

from openai import OpenAI

from app.providers.base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key) if api_key else None

    def generate(self, prompt: str) -> str:
        if not self.client:
            return "OPENAI_API_KEY is not configured."

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content or ""
        except Exception as exc:  # noqa: BLE001
            return f"Provider error: {exc}"

