# Materials Project Natural Language Explorer

**A research-oriented Terminal User Interface (TUI) for autonomous materials discovery and analysis.**

This project integrates the **Materials Project API (mp-api)** with **Gemini 3 Flash** to facilitate an advanced interface for materials science research. By bridging large-scale computational databases with large language model (LLM) reasoning, the explorer enables researchers to navigate material property spaces, analyze stability, and synthesize complex structural insights through natural language interaction.

---

## Technical Showcase: Property Synthesis and Analysis

The explorer serves as a domain-expert collaborator, capable of orchestrating multiple API calls to verify and synthesize material profiles. Below is a representative interaction demonstrating the system's analytical capabilities.

### **Example Interaction Transcript**

```bash
You: Find SrTiO3 and tell me its stability and bandgap.

Gemini:
Based on the Materials Project data, SrTiO₃ (Strontium Titanate) exists in several polymorphs. The most significant are the cubic and tetragonal phases.

1. Cubic Perovskite Phase (Stable Phase)
 • Material ID: mp-5229
 • Crystal System: Cubic (Space Group: Pm-3m, No. 221)
 • Stability: Ground-state phase at room temperature.
 • Bandgap: 1.772 eV (Indirect)
    • Note: DFT calculations significantly underestimate the bandgap. 
      The experimental bandgap is approximately 3.2 eV.

2. Tetragonal Phase (Low-Temperature Phase)
 • Material ID: mp-4651
 • Crystal System: Tetragonal (Space Group: I4/mcm, No. 140)
 • Stability: Associated with the low-temperature structural transition (<105 K).
 • Bandgap: 1.849 eV (Indirect)

Summary of Stability and Electronic Properties:
 • Phase Transition: Characterized by a cubic-to-tetragonal phase transition at 105 K.
 • Bandgap Nature: Indirect gap with VBM at R and CBM at Gamma.
 • Magnetism: All analyzed phases are identified as Non-Magnetic (NM).
```

---

## Architectural Design

### 1. High-Fidelity Data Ingestion
To mitigate information loss inherent in text summarization, this system utilizes the **1,000,000+ token context window** of Gemini 3 Flash to process **raw JSON responses** directly from the source. 
- **Data Integrity**: All numerical values, symmetry details, and metadata are preserved for the model's reasoning engine.
- **Hallucination Mitigation**: The model is architected to ground its responses in live API data rather than relying solely on static training parameters.

### 2. Modular Tool Orchestration
The system is composed of discrete modules that the agent invokes dynamically based on the research context:
- **Discovery**: Autonomous search by chemical system, elements, or formula.
- **Thermodynamics**: Analysis of phase stability, formation energies, and convex hull positioning.
- **Electronic Structure**: Evaluation of band structures, Fermi levels, and bandgap characteristics.
- **Crystal Structure**: Investigation of lattice parameters, space group symmetry, and atomic site data.
- **Magnetism**: Analysis of magnetic ordering and moment quantification.
- **Surfaces**: Retrieval of surface energies and Wulff-shape reconstructions.

---

## Installation and Deployment

### 1. Prerequisites
- **Python 3.10+**
- **Google AI Studio API Key** (Available at [aistudio.google.com](https://aistudio.google.com/))
- **Materials Project API Key** (Available at [materialsproject.org](https://next-gen.materialsproject.org/api))

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/your-username/Materials-Project-Explorer.git
cd Materials-Project-Explorer

# Install the package and dependencies
pip install .
```

### 3. Execution
The explorer can be launched via the command line. The system will prompt for necessary API credentials at startup; these keys are stored only in volatile memory for the duration of the session.

```bash
mp-explorer
```

---

## Usage Guidelines and Commands

| Requirement | Description / Command |
| :--- | :--- |
| **Credential Automation** | Set `GOOGLE_API_KEY` and `MP_API_KEY` environment variables to bypass startup prompts. |
| **Termination** | Input `exit` or `quit` to terminate the session. |
| **Search Syntax** | Use elemental symbols for chemical system searches (e.g., "Find materials with Li, Fe, and P"). |
| **Property Comparison** | Request comparative analysis between multiple Material IDs (e.g., "Compare mp-149 and mp-19017"). |

---

## Research and Usage Considerations

### 1. Scientific Accuracy and DFT Limitations
All material properties retrieved via this tool are derived from **Density Functional Theory (DFT)** calculations provided by the Materials Project. DFT is a computational approximation; calculated values such as bandgaps and formation energies may deviate from experimental observations.

### 2. Experimental Data Grounding
In instances where specific property data is unavailable in the Materials Project database, the model may utilize its internal training data. Users are encouraged to cross-reference LLM-synthesized insights with peer-reviewed literature and explicitly request API verification for critical research data.

### 3. API Rate Limiting
This application utilizes the Google Gemini and Materials Project APIs. Usage is subject to the respective service tier limits (e.g., the Gemini 3 Flash free tier currently allows **15 requests per minute**).

---

## Support and Contributions

### Reporting Issues
If you encounter bugs, technical inconsistencies, or unexpected behavior, please open an issue in the **[GitHub Issue Tracker](https://github.com/8eon/Materials-Project-natural-lang-explorer/issues)**. Detailed bug reports with steps to reproduce the issue are highly appreciated.

### Contributions
Contributions to the project are welcome. If you wish to propose new features, scientific modules (e.g., Elasticity, Piezoelectricity), or UI improvements:
1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request for review.

---

## Development Roadmap

The project utilizes an **incremental modularity** development principle. Each scientific module is independently developed and verified to maintain a robust research environment.

Technical specifications and engineering objectives are maintained in **[PLANNING.md](./PLANNING.md)**.
