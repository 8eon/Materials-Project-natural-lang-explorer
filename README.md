# Materials Project Natural Language Explorer

An intelligent interface for the [Materials Project](https://materialsproject.org/) database, leveraging Gemma 3 and the Model Context Protocol (MCP).

## Overview

The **Materials Project Natural Language Explorer** aims to bridge the gap between complex materials science data and intuitive human inquiry. By wrapping the Materials Project API (`mp-api`) into a set of MCP tools, we enable LLMs like **Gemma 3** to act as a domain-expert assistant that can not only fetch data but also explain concepts, hypothesize on material properties, and guide researchers through the vast chemical space.

## Key Features

- **Natural Language Querying**: No more complex JSON filters or API documentation deep-dives. Ask "Find me stable perovskites with a bandgap between 1.5 and 2.0 eV."
- **MCP Tool Integration**: Built using the Model Context Protocol, allowing Gemma 3 to seamlessly call Materials Project functions as native tools.
- **Expert Context**: Leverages Gemma 3's internal knowledge to explain *why* certain results are significant or what specific material properties (like "Fermi level" or "space group") mean in context.
- **Structured Insights**: Combines raw data from MPRest with synthesized explanations.

## Tech Stack

- **Language**: Python 3.10+
- **Materials Data**: [mp-api](https://github.com/materialsproject/api) (Materials Project)
- **LLM**: Gemma 3 (via API)
- **Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- **Orchestration**: Python-based MCP server

## Roadmap

1. [ ] **Foundation**: Set up MCP server structure and MP API authentication.
2. [ ] **Tooling**: Implement core MP search functions (summary, thermo, dielectric, etc.) as MCP tools.
3. [ ] **Reasoning**: Configure Gemma 3 system prompts to handle materials science queries effectively.
4. [ ] **Interface**: Create a CLI or Web UI for interactive exploration.
5. [ ] **Expansion**: Add support for structure visualization and more complex multi-step queries.

## Getting Started

*(Coming Soon)*

