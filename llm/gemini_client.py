import google.generativeai as genai
from typing import List, Dict, Any, Callable
import json

class GeminiClient:
    def __init__(self, api_key: str, tools: List[Callable] = None):
        genai.configure(api_key=api_key)
        
        system_instruction = (
            "You are a Materials Science Expert Assistant powered by Gemini 3 Flash. "
            "You have direct access to the Materials Project API via provided tools. "
            "\n\nCORE POLICIES:\n"
            "1. DATA INTEGRITY: Always prioritize data fetched from the Materials Project API tools over your internal training data for specific material properties. "
            "The Materials Project is your primary source of truth for calculated properties.\n"
            "2. NO SUMMARIZATION: You have a 1M+ token context window. Do not summarize raw JSON data unless explicitly asked; use the full details to provide precise and accurate scientific explanations.\n"
            "3. COLLABORATION: Your goal is to help the user explore the materials database, explain complex concepts (like band structures, stability, and symmetry), and hypothesize based on evidence."
        )

        # Using Gemini 3 Flash Preview for its 1M+ token context and improved reasoning
        self.model = genai.GenerativeModel(
            'gemini-3-flash-preview',
            tools=tools,
            system_instruction=system_instruction
        )
        self.chat = self.model.start_chat(history=[], enable_automatic_function_calling=True)

    def get_response(self, message: str):
        """
        Sends a message to Gemini and handles automatic function calling.
        Returns the text response.
        """
        response = self.chat.send_message(message)
        return response.text

