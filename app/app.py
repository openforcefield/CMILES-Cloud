from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Tuple
import cmiles

app = FastAPI()

class QCMolecule(BaseModel):
    symbols: List[str]
    geometry: List[float]
    connectivity: List[Tuple[int, int, int]] # Atom1, Atom2, Bond Order
    molecular_charge: int = 0
    molecular_multiplicity: int = 1

@app.post("/qcmolecule")
async def root(molecule: QCMolecule = Body(...)):

    mapped_smiles = cmiles.get_molecule_ids(molecule.dict(), toolkit="rdkit")
    return mapped_smiles

