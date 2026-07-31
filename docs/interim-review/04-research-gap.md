# (4) Research Gap

**Status:** Approved  
**Word limit:** None specified (keep focused and clear)

---

## What current research already does

From the surveyed papers, two strong but incomplete lines of work dominate:

1. **Text → face generation** (Text2FaceGAN, FTGAN, Khan et al., TediGAN, ST²FG) can turn descriptions into faces, but usually stop at a photorealistic image. They rarely produce a forensic pencil-style composite, and most are one-shot generators without a structured witness interview loop.

2. **Sketch → photo / recognition** (DCGAN STF reviews, Devakumar & Sarath, attribute-conditioned CycleGAN, GLAS, adversarial sketch–photo transformation, CLIP4Sketch) improve matching once a sketch exists. They still assume a forensic artist or operator has already drawn or assembled the composite.

The **base paper** (Soppari et al., 2026) closes part of this loop by linking **text → diffusion sketch → biometric/semantic mugshot matching**. That is the closest end-to-end forensic Gen-AI design available to us. Even so, it remains largely a **prompt → generate → search** pipeline. Its own future-work section highlights missing pieces: iterative refinement without identity drift, richer marks (scars, tattoos), stronger multimodal fusion, and explainable scoring.

---

## Gaps relative to our goal

| Gap | Current state | Our goal / vision |
|-----|---------------|-------------------|
| **Starting point** | Many systems need a hand-drawn or software composite first | Start from witness language alone—no artist required for the first draft |
| **Workflow realism** | One-shot generation or prompt rewriting | Mirror real forensic practice: describe → structure features → construct → refine with witness feedback |
| **Feature control** | Opaque prompt or whole-image regeneration | Structured attributes (catalog-like JSON) editable one feature at a time (eyes, jaw, age, scar) |
| **Output form** | Often photo-like faces, or sketch-to-photo only | Explicit **photo → forensic sketch** rendering for investigator-usable composites |
| **Identity check** | Matching to mugshots *or* aesthetic scores, often separate | Built-in biometric evaluation (ArcFace / FaceNet) during research validation |
| **Modularity** | Tightly coupled diffusion + matching stacks | Five replaceable modules so each stage can be improved independently |
| **Assistive role** | Sometimes framed as full artist replacement | Investigator-assistive tool: speed + consistency, witness remains the authority |

---

## What we can do better (our vision)

Our research vision is not “another text-to-image demo.” It is to **digitize the forensic composite workflow**:

1. **Parse** witness speech/text into structured facial attributes (digital catalog selection).  
2. **Encode** those attributes into a controllable generative latent space.  
3. **Generate** a coherent face, then **render** a forensic-style sketch.  
4. **Refine** through natural-language feedback without discarding identity (“make eyes smaller,” “add scar on left cheek”).  
5. **Evaluate** identity preservation objectively so quality is measurable, not only subjective.

Relative to the base Gen-AI paper, we keep the same forensic mission (faster, less artist-dependent composites linked to identity support) but push further on **iterative witness refinement**, **attribute-level controllability**, **explicit sketch styling**, and a **modular research architecture** that maps cleanly onto how composite artists already think and work.

---

## Contribution statement

**Research gap in one line:** existing systems either generate faces from text *or* match sketches to photos; few unify language understanding, controllable face construction, forensic sketch rendering, iterative witness refinement, and biometric evaluation in one investigator-aligned pipeline.

**Our contribution:** bridge that gap with a modular AI-assisted forensic sketch generator designed around real composite practice—assist investigators, shorten hours to minutes, and keep the witness-in-the-loop as the source of truth.
