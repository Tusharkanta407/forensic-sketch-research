# (6) Results and Discussion

**Status:** Included in Interim Review-1 DOCX  

---

## 6.1 Present Research Status

At the time of Interim Review-1, the project is in the foundational research and early experimentation phase. Documentation, literature grounding, architecture design, and initial identity-evaluation experiments have been completed. Full end-to-end interview-to-sketch product integration (Next.js client with generative backend) remains in progress.

---

## 6.2 Experimental Outcomes to Date

### Experiment 001 — ArcFace identity verification on CUHK sketches

**Objective:** Measure how well pretrained ArcFace embeddings preserve identity when comparing photorealistic faces to hand-drawn sketches from the CUHK dataset.  

**Status:** Completed.  

| Comparison | Average Cosine Similarity |
|------------|---------------------------|
| Photo vs. Photo | 0.92 |
| Photo vs. Sketch | 0.72 |

**Discussion:** The photo–photo baseline confirms strong identity clustering under ArcFace. The drop to 0.72 for photo–sketch pairs indicates a substantial domain shift introduced by sketch styling (exaggerated chin, thinned eyes, line abstraction). This result justifies treating sketch rendering as a dedicated module and motivates future work on style-invariant recognition or sketch-domain adaptation before operational mugshot matching.

### Experiment 002 — Attribute-conditioned face generation

**Objective:** Synthesize faces conditioned on CelebA attributes using StyleGAN2-ADA.  

**Status:** In progress.  

**Preliminary observations:** Conditioning on sparse or rare attributes (for example, scars or eyeglasses) shows tendency toward class collapse. Weight modulation / improved conditioning strategies are under investigation.

### Experiment 003 — Sketch rendering method comparison

**Objective:** Compare OpenCV edge-based shaders against Pix2Pix neural translation for forensic sketch appearance.  

**Status:** Not started (scheduled).  

---

## 6.3 Discussion Relative to Project Goals

Current results support three design decisions reflected in the proposed architecture:

1. **Identity validation is measurable but domain-sensitive.** ArcFace is usable as a research metric; sketch-domain shift must be accounted for in evaluation protocols.  
2. **Controllable generation requires careful conditioning.** Attribute sparsity issues observed in Experiment 002 reinforce the need for a structured Face Feature Profile rather than brittle one-shot prompts.  
3. **Interview-first design remains the primary product differentiator.** Empirical generation and rendering work is underway, while the interactive Cognitive-Interview-style agent and Next.js session UI constitute the next integration milestone.

---

## 6.4 Expected Advantages (Projected)

- Reduced composite turnaround from multi-hour artist sessions to minutes.  
- Improved procedural consistency through protocol-constrained interviewing.  
- Feature-level refinement without full identity regeneration.  
- Investigator-assistive deployment via a Next.js application.

## 6.5 Current Limitations

- End-to-end interview → sketch pipeline not yet fully integrated.  
- Generator conditioning for rare forensic marks remains unstable.  
- Sketch rendering comparative study pending.  
- Training corpora (CelebA/FFHQ) may under-represent demographic diversity and forensic marks.  
- System remains research-grade; not a substitute for legal identification.

## 6.6 Next Steps

1. Complete StyleGAN2-ADA conditioning improvements (Experiment 002).  
2. Execute sketch rendering comparison (Experiment 003).  
3. Implement interview state machine and Face Feature Profile APIs.  
4. Deliver Next.js investigator session interface (interview chat + sketch review).  
5. Re-evaluate identity metrics after sketch-domain adaptation.

## 6.7 Interim Conclusion

Interim outcomes demonstrate a viable research trajectory: the forensic interview-aligned architecture is specified; identity evaluation baselines are established (photo–sketch cosine similarity ≈ 0.72); and generative/rendering experiments are sequenced. The immediate priority is closing the loop from structured interview responses to controllable sketch refinement within the Next.js application stack.
