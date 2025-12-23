# Materials Project Natural Language Explorer

An intelligent interface for the [Materials Project](https://materialsproject.org/) database, leveraging Gemma 3 and the Model Context Protocol (MCP).

## Overview

The **Materials Project Natural Language Explorer** aims to bridge the gap between complex materials science data and intuitive human inquiry. By giving **Gemini Flash** direct access to the Materials Project API (`mp-api`) via an extensive suite of functions, we enable a collaborative, expert-level chat experience. 

Leveraging Gemini's massive context window, the explorer passes raw data directly to the model, ensuring **data integrity, completeness, and expert-level synthesis** without the risks of over-summarization.

## Key Features

- **Collaborative AI Researcher**: Gemini Flash acts as a partner, using its world knowledge to explain concepts and the Materials Project API to verify facts.
- **High-Fidelity Data**: Utilizes Gemini's 1M+ token context window to process complete API responses, maintaining scientific accuracy. No summaries used.
- **Granular Control**: Gemini requests specific data modules (Thermodynamics, Electronic, etc.) as needed, ensuring it has the exact raw data required for its reasoning.
- **Privacy-First**: Designed for users to provide their own Google AI Studio and Materials Project API keys at runtime.

## Tech Stack

- **Language**: Python 3.10+
- **Materials Data**: [mp-api](https://github.com/materialsproject/api)
- **LLM**: Gemini Flash (via Google AI Studio)
- **UI**: TUI (Terminal User Interface) using `rich` or `textual`

## Roadmap

1. [ ] **Foundation**: Set up MCP server structure and MP API authentication.
2. [ ] **Tooling**: Implement core MP search functions (summary, thermo, dielectric, etc.) as MCP tools.
3. [ ] **Reasoning**: Configure Gemma 3 system prompts to handle materials science queries effectively.
4. [ ] **Interface**: Create a CLI or Web UI for interactive exploration.
5. [ ] **Expansion**: Add support for structure visualization and more complex multi-step queries.

## Getting Started

*(Coming Soon)*

