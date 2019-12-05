# Converts set of .mol files in /path to
#   filename list -> output.txt
#   SMILES list -> output_smiles.txt   
import os
import tqdm
import sys
from rdkit import Chem

def mols_to_smiles(input_dir, output_dir):
    output_file_smiles = open(os.path.join(output_dir, 'output_smiles.txt'), 'w')
    output_file_name = open(os.path.join(output_dir, 'output_filelist.txt'), 'w')
    
    smiles_list = []
    name_list = []
    os.chdir(input_dir)
    
    #sort files by ID
    file_list = os.listdir(os.getcwd())
    mol_file_list = [x for x in file_list if '.mol' in x]
    mol_file_list = sorted(mol_file_list, key=lambda x: int(x.split('.')[0]))
    
    #takes only 'structure 1'
    #mol_file_list = [x for x in mol_file_list if 'structure1' in x]
    
    for file in tqdm.tqdm(mol_file_list):
        try:
            aux = Chem.MolFromMolFile(file)
            Chem.Kekulize(aux)
            smiles = Chem.MolToSmiles(aux, kekuleSmiles=True)
            smiles_list.append(smiles.replace('*','R'))
            name_list.append(file)
        except:
            smiles_list.append('NONE')
            name_list.append(file)
    
    for item in smiles_list:
        output_file_smiles.write(item)
        output_file_smiles.write('\n')
    output_file_smiles.close()
    
    for item in name_list:
        output_file_name.write(item)
        output_file_name.write('\n')
    output_file_name.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(""" Usage: mols_to_smiles_v1.py [input dir] [output dir]""")
        exit()
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    mols_to_smiles(input_dir, output_dir)
