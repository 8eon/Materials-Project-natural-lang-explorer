import os
from typing import Optional
from rich.console import Console
from rich.prompt import Prompt

console = Console()

class Config:
    def __init__(self):
        self.google_api_key: Optional[str] = None
        self.mp_api_key: Optional[str] = None

    def prompt_for_keys(self):
        console.print("[bold blue]Materials Project Natural Language Explorer[/bold blue]", justify="center")
        console.print("[italic]Please provide your API keys to begin. (Keys are held in memory and not saved to disk).[/italic]\n")
        
        # We use standard input (password=False) to ensure compatibility across all terminal types
        # and to allow for easier pasting of keys.
        self.google_api_key = os.getenv("GOOGLE_API_KEY") or Prompt.ask("Enter your [bold green]Google AI Studio API Key[/bold green]")
        self.mp_api_key = os.getenv("MP_API_KEY") or Prompt.ask("Enter your [bold red]Materials Project API Key[/bold red]")

    @property
    def is_configured(self) -> bool:
        return bool(self.google_api_key and self.mp_api_key)

config = Config()

