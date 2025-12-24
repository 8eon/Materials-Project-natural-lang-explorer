from config import config
from tools import MPClient
from llm.gemini_client import GeminiClient
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def main():
    # 1. Setup Keys
    config.prompt_for_keys()
    
    if not config.is_configured:
        console.print("[bold red]Error: API keys are required to proceed.[/bold red]")
        return

    # 2. Initialize Clients
    try:
        mp_client = MPClient(config.mp_api_key)
        
        # Define the tools we want Gemini to have access to
        # We start with a minimal set to ensure clean, incremental progress
        tools = [
            mp_client.find_materials,
            mp_client.get_thermo_data,
            mp_client.get_electronic_data,
            mp_client.get_structure_data,
            mp_client.get_magnetic_data
        ]
        
        gemini_client = GeminiClient(config.google_api_key, tools=tools)
    except Exception as e:
        console.print(f"[bold red]Initialization failed: {e}[/bold red]")
        return

    console.print("\n[bold green]System Ready.[/bold green] You are now collaborating with Gemini 3 Flash.")
    console.print("[italic]Ask anything about materials science...[/italic]\n")

    # 3. Main Chat Loop
    while True:
        try:
            user_input = console.input("[bold blue]You:[/bold blue] ")
            if user_input.lower() in ["exit", "quit"]:
                break
            
            with console.status("[italic]Gemini is thinking and searching...[/italic]"):
                response = gemini_client.get_response(user_input)
            
            console.print("\n[bold magenta]Gemini:[/bold magenta]")
            console.print(Markdown(response))
            console.print("\n" + "─" * 50 + "\n")

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()

