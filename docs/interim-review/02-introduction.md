# (2) Introduction

**Status:** Approved  
**Word limit:** 300–400 words  
**Word count:** 378

---

A facial composite (commonly called a forensic or police sketch) is a graphical reconstruction of a witness’s memory of a suspect’s face. When surveillance footage or biometric evidence is unavailable, composites remain a primary investigative aid: they support public alerts, help check leads, and assist identification in the critical early hours of a case.

In current practice, construction does not begin with free artistic drawing. It begins with a **Cognitive Interview (CI)**—and often a Holistic Cognitive Interview (H-CI)—recommended by forensic art guidelines and widely used by police. The witness is guided to reinstate the context of the crime in the “mind’s eye,” give uninterrupted free recall of the face, and then answer feature-focused prompts (eyes, nose, mouth, hair, scars, and so on). Reference catalogs such as the **FBI Facial Identification Catalog** or Steinberg-style feature libraries help the witness point to shapes when words alone fail. Only then does construction begin—by hand sketch (proportions, characteristics, shading) or by software composites such as Identikit, E-FIT, PRO-fit, FACES, and EvoFIT—always under continuous witness feedback.

Our research starts from this real forensic workflow, not from generic text-to-image generation. Certified composite artists are scarce, sessions last hours, and both hand and software methods still lose detail when verbal memory must be translated into a fixed feature library. We therefore propose an **AI-Assisted Forensic Sketch Generator** that mirrors the interview–catalog–construct–refine loop used by practitioners, while reducing turnaround from hours to minutes.

The proposed system is a modular research pipeline. An NLU parser converts the witness’s natural-language description into structured facial attributes (the digital equivalent of catalog selection). An attribute encoder maps those features into a generative latent space; a face generator synthesizes a photorealistic face; and a sketch renderer produces a forensic-style pencil composite. A witness feedback loop then updates specific attributes—exactly as an artist revises eyes, age, or scars on request—rather than regenerating an unrelated image from a new prompt.

Finally, during research validation an identity evaluator (ArcFace / FaceNet) measures whether the generated composite preserves biometric likeness against ground-truth references. The intended product is therefore an investigator-assistive tool: it does not replace legal judgment or the witness, but digitizes the forensic artist’s construction steps so usable suspect sketches can be produced quickly, iteratively, and in a manner aligned with established composite practice.
