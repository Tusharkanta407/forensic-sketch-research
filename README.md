<h1 align="center">
  🧬 Forensic Sketch Generator
</h1>

<p align="center">
  <strong>Research Lab&nbsp;&nbsp;·&nbsp;&nbsp;Team Notebook&nbsp;&nbsp;·&nbsp;&nbsp;Experiment Journal</strong>
</p>

<p align="center">
  <a href="https://github.com/Sradha2474/Forensic-Sketch-Generator"><img src="https://img.shields.io/badge/▶_Main_Repo-000000?style=for-the-badge&logo=github&logoColor=white" alt="Main Repo"/></a>&nbsp;
  <a href="./docs/research-roadmap.md"><img src="https://img.shields.io/badge/Roadmap-6C3483?style=for-the-badge&logo=target&logoColor=white" alt="Roadmap"/></a>&nbsp;
  <a href="./papers/"><img src="https://img.shields.io/badge/Papers-1A5276?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Papers"/></a>&nbsp;
  <a href="./tasks/ownership.md"><img src="https://img.shields.io/badge/Team_Roles-117A65?style=for-the-badge&logo=people&logoColor=white" alt="Team Roles"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Active_Research-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
</p>

---

### What is this?

This is our team's research notebook — not production code.

We read papers here, sketch architectures, run experiments, log findings, and stay aligned. Think of it as our shared lab journal.

Production codebase lives here → **[Forensic-Sketch-Generator](https://github.com/Sradha2474/Forensic-Sketch-Generator)**

---

### The Problem

Forensic sketch creation still depends on a trained artist sitting with a witness for hours. It's slow, subjective, hard to scale, and bottlenecked by artist availability.

We're building an AI system that takes a witness's natural language description and generates a forensic-quality sketch — with iterative refinement until the witness approves.

> **Assist**, not replace. This tool supports investigators, it doesn't make legal decisions.

---

### How It Works

```mermaid
graph TD
    A["🔊 Crime Occurs"] --> B["🗣️ Witness Describes Suspect"]
    B --> C["🧠 AI Parses Description"]
    C --> D["📋 Extracts Facial Attributes"]
    D --> E["🎨 Generates Face"]
    E --> F["✏️ Renders as Sketch"]
    F --> G["👁️ Witness Reviews"]
    G --> H{"✅ Good enough?"}
    H -- No --> I["🔄 Witness gives feedback"]
    I --> D
    H -- Yes --> J["🏁 Final Sketch"]

    style J fill:#a5d6a7,stroke:#2e7d32,stroke-width:2px,color:#1b5e20
    style A fill:#ef9a9a,stroke:#c62828,stroke-width:2px,color:#b71c1c
    style C fill:#90caf9,stroke:#1565c0,stroke-width:2px
    style E fill:#ce93d8,stroke:#7b1fa2,stroke-width:2px
    style F fill:#ffcc80,stroke:#e65100,stroke-width:2px
```

---

### Research Modules

Our pipeline is five separate research problems:

<table>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Module_1-NLU_Parser-FF6F00?style=for-the-badge" alt="M1"/></td>
    <td>Turns witness text → structured JSON attributes</td>
    <td><code>DistilBERT</code> · <code>Self-Attention</code> · <code>Zero-shot LLMs</code></td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Module_2-Encoder-FF8F00?style=for-the-badge" alt="M2"/></td>
    <td>Maps JSON features → latent vectors</td>
    <td><code>MLP Mappers</code> · <code>Projection Layers</code></td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Module_3-Generator-7B1FA2?style=for-the-badge" alt="M3"/></td>
    <td>Synthesizes photorealistic face from latents</td>
    <td><code>StyleGAN2-ADA</code> · <code>Diffusion Models</code></td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Module_4-Sketch_Renderer-1565C0?style=for-the-badge" alt="M4"/></td>
    <td>Converts photo → pencil-style forensic sketch</td>
    <td><code>OpenCV</code> · <code>NST</code> · <code>Pix2Pix</code></td>
  </tr>
  <tr>
    <td align="center"><img src="https://img.shields.io/badge/Module_5-Evaluator-2E7D32?style=for-the-badge" alt="M5"/></td>
    <td>Checks identity preservation vs ground truth</td>
    <td><code>ArcFace</code> · <code>FaceNet</code> · <code>Cosine Similarity</code></td>
  </tr>
</table>

```mermaid
flowchart LR
    A["🗣️ Text"] --> B["🧠 NLU"]
    B --> C["🔢 Encoder"]
    C --> D["🎨 Generator"]
    D --> E["✏️ Sketch"]
    E --> F["📄 Output"]
    D -. "🔍 Identity Check" .-> G["🛡️ Evaluator"]
    G -. "Score" .-> D

    style A fill:#FF6F00,color:#fff
    style B fill:#FF8F00,color:#fff
    style C fill:#F9A825,color:#000
    style D fill:#7B1FA2,color:#fff
    style E fill:#1565C0,color:#fff
    style F fill:#2E7D32,color:#fff
    style G fill:#00695C,color:#fff
```

<details>
<summary><strong>↳ Example: NLU Parser input → output</strong></summary>
<br/>

**Input:**
> "Male, around 35, oval face, brown eyes, scar on left cheek"

**Output:**
```json
{
  "gender": "male",
  "age": 35,
  "face_shape": "oval",
  "eye_color": "brown",
  "scar": "left_cheek"
}
```
</details>

---

### Repo Structure

Click any folder to browse it.

<table>
  <tr>
    <td><a href="./docs/"><img src="https://img.shields.io/badge/📂_docs-4A148C?style=flat-square" alt="docs"/></a></td>
    <td>Problem statement, literature review, roadmap, evaluation metrics, glossary</td>
  </tr>
  <tr>
    <td><a href="./papers/"><img src="https://img.shields.io/badge/📂_papers-1A237E?style=flat-square" alt="papers"/></a></td>
    <td>Paper summaries + PDFs organized by publisher</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href="./papers/concept/"><img src="https://img.shields.io/badge/concept-000000?style=flat-square&logo=bookstack&logoColor=white" alt="concept"/></a></td>
    <td>Foundational papers — Attention, ArcFace, FaceNet, StyleGAN, StyleGAN2, Pix2Pix</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href="./papers/IEEE/"><img src="https://img.shields.io/badge/IEEE-00629B?style=flat-square&logo=ieee&logoColor=white" alt="IEEE"/></a></td>
    <td>Text-to-Face, Sketch-to-Photo, Face Sketch Recognition, Photo Synthesis</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href="./papers/ELSEVIER/"><img src="https://img.shields.io/badge/Elsevier-FF6C00?style=flat-square&logo=elsevier&logoColor=white" alt="ELSEVIER"/></a></td>
    <td>DCGAN and generative adversarial network research</td>
  </tr>
  <tr>
    <td>&nbsp;&nbsp;&nbsp;&nbsp;<a href="./papers/Research-GATE/"><img src="https://img.shields.io/badge/ResearchGate-00CCBB?style=flat-square&logo=researchgate&logoColor=white" alt="ResearchGate"/></a></td>
    <td>Forensic sketch generation using Gen-AI and DCGAN review papers</td>
  </tr>
  <tr>
    <td><a href="./architecture/"><img src="https://img.shields.io/badge/📂_architecture-004D40?style=flat-square" alt="architecture"/></a></td>
    <td>Mermaid diagrams — system overview, training flow, inference pipeline</td>
  </tr>
  <tr>
    <td><a href="./datasets/"><img src="https://img.shields.io/badge/📂_datasets-BF360C?style=flat-square" alt="datasets"/></a></td>
    <td>CelebA, FFHQ, CUHK dataset docs and preprocessing pipelines</td>
  </tr>
  <tr>
    <td><a href="./paper-implementations/"><img src="https://img.shields.io/badge/📂_paper--implementations-E65100?style=flat-square" alt="paper-implementations"/></a></td>
    <td>From-scratch implementations of core paper algorithms</td>
  </tr>
  <tr>
    <td><a href="./experiments/"><img src="https://img.shields.io/badge/📂_experiments-6A1B9A?style=flat-square" alt="experiments"/></a></td>
    <td>Experiment logs, configs, results — organized per experiment</td>
  </tr>
  <tr>
    <td><a href="./prototypes/"><img src="https://img.shields.io/badge/📂_prototypes-283593?style=flat-square" alt="prototypes"/></a></td>
    <td>Sandbox code — notebooks, quick tests, early-stage modules</td>
  </tr>
  <tr>
    <td><a href="./tasks/"><img src="https://img.shields.io/badge/📂_tasks-1B5E20?style=flat-square" alt="tasks"/></a></td>
    <td>Sprint plans, backlog, task ownership</td>
  </tr>
  <tr>
    <td><a href="./resources/"><img src="https://img.shields.io/badge/📂_resources-37474F?style=flat-square" alt="resources"/></a></td>
    <td>Books, YouTube, GitHub repos, references</td>
  </tr>
</table>

---

### Roadmap

```mermaid
graph LR
    subgraph "Phase 1 🔬"
        A["Literature Review"] --> B["Dataset Setup"]
    end
    subgraph "Phase 2 🧠"
        B --> C["Text-to-Attribute Parser"]
    end
    subgraph "Phase 3 🎨"
        C --> D["Face Generation Prototypes"]
    end
    subgraph "Phase 4 ✏️"
        D --> E["Sketch Rendering"]
        D --> F["Identity Evaluation"]
    end
    subgraph "Phase 5 🚀"
        E --> G["Main Repo Integration"]
        F --> G
    end

    style A fill:#E8EAF6,stroke:#3F51B5
    style B fill:#E8EAF6,stroke:#3F51B5
    style C fill:#EDE7F6,stroke:#7B1FA2
    style D fill:#F3E5F5,stroke:#9C27B0
    style E fill:#E0F2F1,stroke:#00695C
    style F fill:#E0F2F1,stroke:#00695C
    style G fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px
```

---

### Team & Guide

#### 🎓 Project Guide & Advisor
<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/dr-sukant-k-bisoy-21701176/">
        <img src="./docs/images/sukant_bisoyi.png" width="100" height="100" style="border-radius:50%;" alt="Dr. Sukant K. Bisoyi"/><br/>
        <sub><strong>Dr. Sukant K. Bisoyi</strong></sub><br/>
        <sub>Dean & Professor, CSE Dept.</sub><br/>
        <sub>C. V. Raman Global University</sub>
      </a>
    </td>
  </tr>
</table>

#### 👥 Research Team
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Sradha2474">
        <img src="https://github.com/Sradha2474.png" width="100" height="100" style="border-radius:50%;" alt="Sradha"/><br/>
        <sub><strong>Sradha</strong></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Tusharkanta407">
        <img src="https://github.com/Tusharkanta407.png" width="100" height="100" style="border-radius:50%;" alt="Tushar"/><br/>
        <sub><strong>Tushar</strong></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/sandeepswain54">
        <img src="https://github.com/sandeepswain54.png" width="100" height="100" style="border-radius:50%;" alt="Sandeep"/><br/>
        <sub><strong>Sandeep</strong></sub>
      </a>
    </td>
  </tr>
</table>

Role assignments → [**tasks/ownership.md**](./tasks/ownership.md)

---

### How We Work

- **Experiments** go in [`experiments/`](./experiments/) — one folder per experiment with objective, results, next steps.
- **Paper reviews** follow the template in [`papers/README.md`](./papers/README.md).
- **No random files** in root. Prototypes → [`prototypes/`](./prototypes/). Scratch code → experiments.
- **Sprint tracking** in [`tasks/`](./tasks/) — updated before each weekly sync.

---

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square"/>
  &nbsp;
  <a href="https://github.com/Sradha2474/Forensic-Sketch-Generator"><img src="https://img.shields.io/badge/Production_Repo-→-black?style=flat-square&logo=github" alt="Production Repo"/></a>
</p>