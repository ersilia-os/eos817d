# Hyper-Dimensional Fingerprints

HDF is a training-free molecular representation based on hyperdimensional computing and iterative message passing. It encodes atom features into high-dimensional vectors and captures molecular connectivity through algebraic operations, producing deterministic fixed-length fingerprints. It retains graph information better than Morgan fingerprints at low dimensions, improves property prediction across benchmarks, and enhances sample efficiency in Bayesian molecular optimization.



## Information
### Identifiers
- **Ersilia Identifier:** `eos817d`
- **Slug:** `hyper-dimensional-fingerprints`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `32`
- **Output Consistency:** `Fixed`
- **Interpretation:** Vector representation of a molecule.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_00 | float |  | Hyperdimensional fingerprint dimension 0 encoding molecular structure |
| feat_01 | float |  | Hyperdimensional fingerprint dimension 1 encoding molecular structure |
| feat_02 | float |  | Hyperdimensional fingerprint dimension 2 encoding molecular structure |
| feat_03 | float |  | Hyperdimensional fingerprint dimension 3 encoding molecular structure |
| feat_04 | float |  | Hyperdimensional fingerprint dimension 4 encoding molecular structure |
| feat_05 | float |  | Hyperdimensional fingerprint dimension 5 encoding molecular structure |
| feat_06 | float |  | Hyperdimensional fingerprint dimension 6 encoding molecular structure |
| feat_07 | float |  | Hyperdimensional fingerprint dimension 7 encoding molecular structure |
| feat_08 | float |  | Hyperdimensional fingerprint dimension 8 encoding molecular structure |
| feat_09 | float |  | Hyperdimensional fingerprint dimension 9 encoding molecular structure |

_10 of 32 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`

### Resource Consumption


### References
- **Source Code**: [https://doi.org/10.5281/zenodo.19373621](https://doi.org/10.5281/zenodo.19373621)
- **Publication**: [https://arxiv.org/abs/2604.27810](https://arxiv.org/abs/2604.27810)
- **Publication Type:** `Preprint`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos817d
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos817d
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
