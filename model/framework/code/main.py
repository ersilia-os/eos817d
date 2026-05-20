import os
import sys
import numpy as np
from ersilia_pack_utils.core import read_smiles, write_out

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root)

from hyper_fingerprints import Encoder

DIMENSION = 32
SEED = 42


def my_model(smiles_list):
    enc = Encoder(dimension=DIMENSION, seed=SEED, backend="numpy")
    outputs = []
    for smi in smiles_list:
        try:
            fp = enc.encode(smi)
            outputs.append(fp[0])
        except Exception:
            outputs.append(np.full(DIMENSION, np.nan))
    return np.array(outputs, dtype=np.float32)


_, smiles_list = read_smiles(input_file)

outputs = my_model(smiles_list)

assert len(smiles_list) == len(outputs)

pad = len(str(DIMENSION - 1))
header = [f"feat_{str(i).zfill(pad)}" for i in range(DIMENSION)]

write_out(outputs, header, output_file, np.float32)
