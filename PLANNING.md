# Technical Planning: Materials Project Natural Language Explorer

This document outlines the architecture, data strategy, and implementation roadmap for the collaborative materials science assistant.

## 1. Project Vision
A TUI-based collaborative environment where a researcher interacts with Gemini Flash. The model has direct, granular access to the Materials Project database to inform its chemistry reasoning with high-fidelity, raw data.

## 2. Tech Stack
- **LLM**: Gemini 3 Flash (via Google AI Studio API).
- **Data Source**: Materials Project API (mp-api).
- **Interface**: Python-based TUI (Terminal User Interface) using rich for styling.
- **Environment**: Python 3.10+, managed via pyproject.toml.

## 3. Data Strategy: High-Fidelity, No Summary
To ensure scientific accuracy:
- **Zero Summarization**: The Python layer fetches raw JSON from the MP API and passes it directly into Gemini's context window.
- **Granular Retrieval**: Instead of fetching all data for a material at once, Gemini requests specific modules based on the conversation flow.
- **Context Management**: Leverages the 1M+ token context window to maintain a history of all raw data fetched during a session.

## 4. Function Calling Suite (The Tools)

### Category A: Discovery
- find_materials: Search for material IDs based on chemical system, elements, or formula.

### Category B: Data Modules (Granular)
Each function takes a material_id and returns the complete raw JSON for that specific sub-API:
- get_thermo_data: Enthalpy, stability, energy above hull.
- get_electronic_data: Bandgap, Fermi energy.
- get_structure_data: Lattice parameters, space group, atomic sites.
- get_magnetic_data: Magnetic moments, ordering.
- get_surface_data: Wulff shapes, surface energies.

## 5. TUI Design
- **Key Input**: On launch, the TUI prompts the user for their Google AI Studio API Key and Materials Project API Key.
- **Chat Interface**: A scrolling conversation view.
- **Dynamic Status**: A visual indicator showing when Gemini is accessing specific data modules.
- **Rich Formatting**: Use of markdown rendering in the terminal to display data clearly.

## 6. Directory Structure
```text
/
├── main.py                # Entry point & TUI Loop
├── config.py              # API Key management & validation
├── pyproject.toml         # Package definition and dependencies
├── tools/
│   ├── __init__.py        # Tool aggregation
│   ├── base.py            # Shared API client logic
│   ├── discovery.py       # Search functionality
│   ├── thermodynamics.py  # Stability data
│   ├── electronic.py      # Bandgap data
│   ├── structure.py       # Crystal symmetry data
│   ├── magnetic.py        # Magnetic data
│   └── surfaces.py        # Surface data
├── llm/
│   ├── __init__.py
│   └── gemini_client.py   # Gemini API integration
├── PLANNING.md            # This document
└── README.md              # Project overview
```

## 7. Implementation Roadmap

### Phase 1: Foundation (Status: Complete)
- Initialized Python environment and modular structure.
- Implemented runtime credential management.
- Established Gemini 3 Flash connection with automated function calling.

### Phase 2: Modular Toolset (Status: Complete)
- Developed and integrated Discovery, Thermodynamics, Electronic Structure, Crystal Structure, Magnetism, and Surface Property modules.
- Verified raw JSON data ingestion pipeline.

### Phase 3: TUI and UX Refinement (Status: Complete)
- Implemented Gemini-style dynamic status switching (Thinking vs. Accessing).
- Optimized terminal output for professional research interaction.
- Formally packaged the application for portfolio deployment.
