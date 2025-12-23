# Technical Planning: Materials Project Natural Language Explorer

This document outlines the architecture, data strategy, and implementation roadmap for the collaborative materials science assistant.

## 1. Project Vision
A TUI-based collaborative environment where a researcher interacts with Gemini Flash. The model has direct, granular access to the Materials Project database to inform its chemistry reasoning with high-fidelity, raw data.

## 2. Tech Stack
- **LLM**: Gemini 1.5 Flash (via Google AI Studio API). Chosen for its 1M+ token context window.
- **Data Source**: Materials Project API (`mp-api`).
- **Interface**: Python-based TUI (Terminal User Interface) using `rich` for styling and potentially `textual` for layout management.
- **Environment**: Python 3.10+, managed via `pyproject.toml` or `requirements.txt`.

## 3. Data Strategy: "High-Fidelity, No Summary"
To ensure scientific accuracy:
- **Zero Summarization**: The Python layer will fetch raw JSON from the MP API and pass it directly into Gemini's context window.
- **Granular Retrieval**: Instead of fetching all data for a material at once, Gemini will "request" specific modules based on the conversation flow.
- **Context Management**: Leverage the large context window to maintain a history of all raw data fetched during a session.

## 4. Function Calling Suite (The "Tools")

### Category A: Discovery
- `find_materials(criteria)`: Search for material IDs based on chemical system, elements, or property ranges (bandgap, stability). Returns a list of IDs and formulas.

### Category B: Data Modules (Granular)
Each function takes a `material_id` and returns the complete raw JSON for that specific sub-API:
- `get_thermo_data(id)`: Enthalpy, stability, energy above hull.
- `get_electronic_data(id)`: Bandgap, DOS, Fermi energy.
- `get_structure_data(id)`: Lattice parameters, space group, atomic sites.
- `get_magnetic_data(id)`: Magnetic moments, ordering.
- `get_surface_data(id)`: Wulff shapes, surface energies.

## 5. TUI Design
- **Key Input**: On launch, the TUI prompts the user for their Google AI Studio API Key and Materials Project API Key.
- **Chat Interface**: A scrolling conversation view.
- **Live Tool Status**: A visual indicator showing when Gemini is "Fetching [Thermo Data] for mp-1234...".
- **Rich Formatting**: Use tables and markdown rendering in the terminal to display data clearly.

## 6. Directory Structure
```text
/
├── main.py                # Entry point & TUI Loop
├── config.py              # API Key management & validation
├── tools/
│   ├── __init__.py
│   ├── mp_client.py       # Materials Project API wrappers
│   └── definitions.py     # JSON schemas for Function Calling
├── llm/
│   ├── __init__.py
│   └── gemini_client.py   # Gemini API integration & tool handling
├── PLANNING.md            # This document
└── README.md              # Project overview
```

## 7. Implementation Roadmap
1. **Phase 1: Foundation**
   - Initialize Python environment.
   - Implement `config.py` for runtime key entry.
   - Set up basic `mp-api` connection.
2. **Phase 2: The Core Tools**
   - Implement the `find_materials` and `get_thermo_data` functions.
   - Test raw JSON output to Gemini context.
3. **Phase 3: TUI Development**
   - Build the main chat loop using `rich`.
   - Implement real-time tool execution feedback.
4. **Phase 4: Expansion**
   - Add remaining data modules (Electronic, Structure, etc.).
   - Refine system prompts for better scientific collaboration.

