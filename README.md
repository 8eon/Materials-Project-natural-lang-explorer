# Materials Project Natural Language Explorer

**A research-oriented Terminal User Interface (TUI) for autonomous materials discovery and analysis.**

This project integrates the **Materials Project API (mp-api)** with **Gemini 3 Flash** to facilitate an advanced interface for materials science research. By bridging large-scale computational databases with large language model (LLM) reasoning, the explorer enables researchers to navigate material property spaces, analyze stability, and synthesize complex structural insights through natural language interaction.

---

## Technical Showcase: Property Synthesis and Analysis

The explorer serves as a domain-expert collaborator, capable of orchestrating multiple API calls to verify and synthesize material profiles. Below is a representative interaction demonstrating the system's analytical capabilities.

### **Example Interaction Transcript**

```bash
You: Compare the crystal structure and bandgap of SrTiO3 and BaTiO3.
Gemini is thinking...

Gemini:
SrTiO3 (Strontium Titanate) and BaTiO3 (Barium Titanate) are both archetypal    
perovskite oxides ($ABO_3$) with significant importance in condensed matter     
physics and electronics, particularly for their dielectric and ferroelectric    
properties. Below is a comparison based on data from the Materials Project.     

                        1. Crystal Structure Comparison                         

                                                                            
  Property         SrTiO3 (mp-gwx / mp-4651)    BaTiO3 (mp-eli / mp-2998)   
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
  Crystal System   Tetragonal (at 0K/Low T)     Cubic (Paraelectric Phase)  
  Space Group      $I4/mcm$ (No. 140)           $Pm\bar{3}m$ (No. 221)      
  Lattice Volume   ~59.81 Å³ per formula unit   ~64.37 Å³ per formula unit  
  Density          5.09 g/cm³                   6.02 g/cm³                  
  Symmetry         $4/mmm$                      $m\bar{3}m$                 
                                                                            

 • SrTiO3 Structure: In its most stable calculated form (mp-gwx), SrTiO3        
   exhibits a tetragonal distortion from the ideal cubic perovskite structure.  
   This transition from cubic to tetragonal typically occurs experimentally at  
   approximately 105 K due to the rotation of the $TiO_6$ octahedra (the        
   "antiferrodistortive" transition).                                           
 • BaTiO3 Structure: The primary entry (mp-eli) represents the cubic            
   paraelectric phase. BaTiO3 is well-known for a sequence of ferroelectric     
   phase transitions: Cubic → Tetragonal → Orthorhombic → Rhombohedral as       
   temperature decreases. The cubic phase shown here is the high-temperature    
   state (stable above ~120°C).                                                 
 • Comparison: BaTiO3 has a larger unit cell volume than SrTiO3, primarily due  
   to the larger ionic radius of $Ba^{2+}$ (1.61 Å) compared to $Sr^{2+}$ (1.44 
   Å). This size difference is also a driving factor in the differing phase     
   transition temperatures and the ferroelectric nature of BaTiO3.              

                        2. Electronic Bandgap Comparison                        

The following values are calculated using Density Functional Theory (DFT) with  
the GGA functional. Note that DFT systematically underestimates bandgaps        
compared to experimental values (which are both ~3.2 eV).                       

                                                                     
  Property            SrTiO3                         BaTiO3          
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
  Bandgap (DFT-GGA)   1.85 eV                        1.67 eV         
  Gap Type            Indirect                       Indirect        
  VBM Position        $R$-point (or near $\Gamma$)   $R$-point       
  CBM Position        $\Gamma$-point                 $\Gamma$-point  
                                                                     

 • Band Structure: Both materials are wide-bandgap insulators with indirect     
   bandgaps. The Valence Band Maximum (VBM) is primarily composed of Oxygen $2p$
   orbitals, while the Conduction Band Minimum (CBM) is dominated by Titanium   
   $3d$ ($t_{2g}$) orbitals.                                                    
 • Comparison: The calculated bandgap for SrTiO3 is slightly higher than that of
   BaTiO3. In both cases, the conduction band minimum is located at the $\Gamma$
   point. The electronic structure reflects the similar chemistry of the $TiO_6$
   octahedral network, which determines the fundamental electronic properties in
   these titanates.                                                             

                                    Summary                                     

While both materials share the perovskite framework, BaTiO3 is denser and has a 
larger unit cell due to the Barium cation. SrTiO3 is often used as a substrate  
for thin-film growth because it remains cubic down to nearly 100 K and is a     
"quantum paraelectric," whereas BaTiO3 is a prototypical ferroelectric with a   
lower calculated electronic bandgap.                                            

──────────────────────────────────────────────────

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

## Installation and Setup

To use the explorer, you will need to copy the project to your computer and install its requirements. This process requires **Python 3.10** or higher.

### 1. Get Your API Keys
You will need two free keys to power the agent:
- **Google AI Studio Key**: Get this at [aistudio.google.com](https://aistudio.google.com/) to provide the "brain" (Gemini 3).
- **Materials Project Key**: Get this at [materialsproject.org](https://next-gen.materialsproject.org/api) to provide the data.

### 2. Setup and Execution
Open your terminal and run this single command to install the explorer directly from GitHub:

```bash
pip install git+https://github.com/8eon/Materials-Project-natural-lang-explorer.git
```

Once installed, launch the explorer by typing:

```bash
mp-explorer
```

The program will ask you to paste your API keys. It only keeps these keys in its active memory while it's running; they are never saved to your files. To stop the program at any time, type `exit` or `control + c`.

---

## Research and Usage Considerations

### 1. Scientific Accuracy and DFT Limitations
All material properties retrieved via this tool are derived from **Density Functional Theory (DFT)** calculations provided by the Materials Project. DFT is a computational approximation; calculated values such as bandgaps and formation energies may deviate from experimental observations.

### 2. Experimental Data Grounding
In instances where specific property data is unavailable in the Materials Project database, the model may utilize its internal training data. Users are encouraged to cross-reference LLM-synthesized insights with peer-reviewed literature and explicitly request API verification for critical research data.

### 3. API Rate Limiting
This application utilizes the Google Gemini and Materials Project APIs. Usage is subject to the respective service tier limits. The Gemini 3 Flash free tier currently allows **15 requests per minute**.

---

## Support and Contributions

### Reporting Issues
If you encounter bugs, technical inconsistencies, or unexpected behavior, please open an issue in the **[GitHub Issue Tracker](https://github.com/8eon/Materials-Project-natural-lang-explorer/issues)**.

### Contributions
Contributions to the project are welcome. If you wish to propose new features, scientific modules (e.g., Elasticity, Piezoelectricity), or UI improvements:
1. Fork the repository.
2. Create a feature branch.
3. Submit a Pull Request for review.

---

## Development Roadmap

The project utilizes an **incremental modularity** development principle. Each scientific module is independently developed and verified to maintain a robust research environment.

Technical specifications and engineering objectives are maintained in **[PLANNING.md](./PLANNING.md)**.
