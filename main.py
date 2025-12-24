from config import config
from tools import MPClient
from llm.gemini_client import GeminiClient
import time
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from rich.text import Text

console = Console()

def create_status_display(mp_client):
    """Creates a clean, dynamic status line that switches between thinking and accessing."""
    # If a tool was called recently (within last 2 seconds), show the access status
    time_since_last_call = time.time() - mp_client.last_call_time
    
    if mp_client.call_count > 0 and time_since_last_call < 2.0:
        return Text.assemble(
            (f" 📂 Accessing {mp_client.current_action} ", "bold yellow"),
            (f"({mp_client.call_count})", "dim cyan")
        )
    
    # Default state is 'thinking'
    return Text(" ⌛ Gemini is thinking...", style="italic cyan")

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
            mp_client.get_magnetic_data,
            mp_client.get_surface_data
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
            
            # Reset counters for the new turn
            mp_client.call_count = 0
            mp_client.current_action = "Analyzing Query"

            with Live(create_status_display(mp_client), refresh_per_second=4) as live:
                # The tool calls inside get_response will update the mp_client state
                # and rich.Live will automatically refresh the display
                response = gemini_client.get_response(user_input)
                live.update(create_status_display(mp_client))
            
            console.print("\n[bold magenta]Gemini:[/bold magenta]")
            console.print(Markdown(response))
            console.print("\n" + "─" * 50 + "\n")

        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()

