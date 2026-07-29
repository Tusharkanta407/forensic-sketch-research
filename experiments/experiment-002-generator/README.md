# Experiment 002: Attribute-Conditioned Generation

## Objective
Synthesize faces conditioning on CelebA attributes using StyleGAN2-ADA.

## Files
* `train_conditional.py` - Custom training wrapper.

## Results
* *In progress...*

## Observations
* Model is prone to class collapse when conditioning on sparse features (e.g., "scar", "eyeglasses").

## Next Steps
* Implement weight conditioning via modulation networks.\n