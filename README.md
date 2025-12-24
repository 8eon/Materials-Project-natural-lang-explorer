# Materials Project Natural Language Explorer

**An advanced, research-oriented TUI for autonomous materials discovery and analysis.**

Built with **Python**, the **Materials Project API (mp-api)**, and **Gemini 3 Flash**, this project bridges the gap between massive computational databases and expert-level chemical reasoning. It transforms the Materials Project into a "live" knowledge graph that an LLM can navigate autonomously to assist researchers in identifying, analyzing, and hypothesizing on novel materials.

---

## 🔬 Scientific Portfolio Highlight: Autonomous Property Synthesis

The explorer enables a high-fidelity collaboration where the AI acts as a domain-expert partner. Below is a transcript of a real-world interaction demonstrating the agent's ability to orchestrate multiple API calls to synthesize a complex material profile.

### **Query**: *"Compare the cubic and tetragonal phases of SrTiO3."*

> **User**: *"Find SrTiO3 and tell me its stability and bandgap."*
>
> **Gemini 3 Flash**:
>
> Based on the Materials Project data, **SrTiO₃ (Strontium Titanate)** exists in several polymorphs. The most significant are the cubic and tetragonal phases.
> 
> #### 1. Cubic Perovskite Phase (Stable Phase)
> - **Material ID**: `mp-5229` (also referred to as `mp-htd` in newer documentation)
> - **Crystal System**: Cubic (Space Group: $Pm\bar{3}m$, No. 221)
> - **Stability**: Ground-state phase at room temperature. It is a highly stable perovskite structure.
> - **Bandgap**: 1.772 eV (Indirect)
>   - *Note: DFT calculations (typically using PBE functionals) significantly underestimate the bandgap. The experimental bandgap of SrTiO₃ is approximately 3.2 eV.*
> 
> #### 2. Tetragonal Phase (Low-Temperature Phase)
> - **Material ID**: `mp-4651` (also referred to as `mp-gwx`)
> - **Crystal System**: Tetragonal (Space Group: $I4/mcm$, No. 140)
> - **Stability**: Associated with the low-temperature structural transition of SrTiO₃ (<105 K) due to the rotation of the TiO₆ octahedra.
> - **Bandgap**: 1.849 eV (Indirect)
> 
> #### 3. Other Polymorphs
>
> | Material ID | Crystal System | Bandgap | Gap Type |
> | :--- | :--- | :--- | :--- |
> | `mp-551830` | Tetragonal ($I4/mcm$) | 1.787 eV | Direct |
> | `mp-776018` | Hexagonal ($P6_3/mmc$) | 1.736 eV | Direct |
> 
> #### Summary of Stability and Electronic Properties
> - **Phase Transition**: SrTiO₃ is famous for its cubic-to-tetragonal phase transition at 105 K. In the cubic phase, the Ti atom is at the center of an O₆ octahedron, which provides the classic perovskite stability.
> - **Bandgap Nature**: In the stable cubic phase, the valence band maximum (VBM) is at the R point and the conduction band minimum (CBM) is at the $\Gamma$ point, resulting in an indirect bandgap.
> - **Magnetism**: All searched phases are identified as Non-Magnetic (NM).

---

## 🛠️ Key Architectural Innovations

### 1. High-Fidelity "No-Summary" Ingestion
Traditional LLM integrations often suffer from information loss due to aggressive summarization or limited context. This explorer leverages the **1,000,000+ token context window** of Gemini 3 Flash to ingest **raw JSON responses** directly. 
- **Integrity**: Every decimal point of lattice parameters and every k-point in a bandgap calculation is preserved.
- **Accuracy**: Eliminates the "hallucination" risk often found in LLMs with static training data.

### 2. Granular Tool Orchestration
Instead of monolithic API calls, the system is designed as a suite of granular modules. The LLM intelligently "requests" only the necessary data segments:
- **`Thermodynamics`**: Phase stability, formation energies, and convex hull analysis.
- **`ElectronicStructure`**: Bandgap analysis, Fermi level, and density of states.
- **`Symmetry & Structure`**: Space group identification, lattice vectors, and site-symmetry.
- **`Magnetism`**: Magnetic ordering and total magnetic moment quantification.

### 3. Expert-Grounded Reasoning
The system prompt is engineered to prioritize **Ground Truth (API)** over **Parametric Knowledge (Training Data)**. It forces the model to verify its "intuition" with live calculations from the Materials Project, while still leveraging the LLM's vast understanding of general chemistry principles to explain complex phenomena.

---

## 💻 Technical Implementation

- **Interface**: High-performance **Terminal User Interface (TUI)** built with `rich`, providing a clean, developer-centric research environment.
- **Architecture**: Modular, class-based Python package structure designed for horizontal scalability (easily add Elasticity, Surfaces, or Piezoelectricity modules).
- **Security**: Stateless runtime API key configuration (via environment variables or secure terminal prompts).

### **Installation & Deployment**

```bash
# Clone and install dependencies
git clone https://github.com/your-username/Materials-Project-Explorer.git
cd Materials-Project-Explorer
pip install mp-api google-generativeai rich

# Configure environment (Recommended)
export GOOGLE_API_KEY="your_api_key"
export MP_API_KEY="your_api_key"

# Launch the explorer
python main.py
```

---

## 📈 Roadmap & Development Principles

This project is developed with **incremental modularity** as a core principle. Each scientific module is developed and verified independently to ensure a robust, error-free integration.

*For detailed technical specifications and the engineering roadmap, please refer to **[PLANNING.md](./PLANNING.md)**.*
