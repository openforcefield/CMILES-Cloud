from fastapi.testclient import TestClient
import pytest
from .app import app

client = TestClient(app)

# fmt: off
hooh = {
    'symbols': ['H', 'O', 'O', 'H'],
    'geometry': [
         1.84719633,  1.47046223,  0.80987166,
         1.3126021,  -0.13023157, -0.0513322,
        -1.31320906,  0.13130216, -0.05020593,
        -1.83756335, -1.48745318,  0.80161212
    ],
    'connectivity': [[0, 1, 1], [1, 2, 1], [2, 3, 1]],
}
# fmt: on

hooh_results = {
    "canonical_smiles": "OO",
    "canonical_isomeric_smiles": "OO",
    "canonical_explicit_hydrogen_smiles": "[H][O][O][H]",
    "canonical_isomeric_explicit_hydrogen_smiles": "[H][O][O][H]",
    "canonical_isomeric_explicit_hydrogen_mapped_smiles": "[H:1][O:2][O:3][H:4]",
    "molecular_formula": "H2O2",
    "standard_inchi": "InChI=1S/H2O2/c1-2/h1-2H",
    "inchi_key": "MHAJPDPJQMAIIY-UHFFFAOYSA-N",
    "unique_tautomer_representation": "OO",
    "provenance": "cmiles_0+unknown_rdkit_2020.03.1",
}

@pytest.mark.parametrize("molecule, results", [(hooh, hooh_results)])
def test_cmiles_qcmolecule(molecule, results):

    response = client.post("/qcmolecule", json=hooh,)

    assert response.status_code == 200, response.json()
    mol_id = response.json()

    for key, ref in results.items():
        assert mol_id[key] == ref
