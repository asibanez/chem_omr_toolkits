""" Evaluate for a set of models on the validation set
    The main purpose of this script is to see the learning curve """

#v3 saves the list of correct predictions

import rdkit.Chem as Chem
from collections import defaultdict
import json
import sys
import os

def normalize(gold_smi, pred_smi):
    valid_gold = False; valid_pred = False

    gold_mol = Chem.MolFromSmiles(gold_smi)
    pred_mol = Chem.MolFromSmiles(pred_smi)
    if not gold_mol:
        return gold_smi, pred_smi, (valid_gold, valid_pred)

    valid_gold = True
    if not pred_mol:
        return gold_smi, pred_smi, (valid_gold, valid_pred)

    valid_pred = True
    #Chem.Kekulize(mol)
    pred_smi_norm = Chem.MolToSmiles(pred_mol)
    gold_smi_norm = Chem.MolToSmiles(gold_mol)
    return gold_smi_norm, pred_smi_norm, (valid_gold, valid_pred)

def evaluate(pred_path, gold_path):
    stats = defaultdict(int)
    correct_predictions = []
    print("Evaluting Valid/EM")
    
    with open(gold_path) as gold:
        with open(pred_path) as pred:
            for i, (gold_smi, pred_smi) in enumerate(zip(gold, pred)):

                gold_smi = gold_smi.strip().replace(' ', '')
                pred_smi = pred_smi.strip().replace(' ', '')
                gold_smi_norm, pred_smi_norm, (valid_gold, valid_pred) = normalize(gold_smi, pred_smi)

                if gold_smi_norm == pred_smi_norm:
                    stats['cnt_corr'] += 1
                    correct_predictions.append(i)
                stats['cnt'] += 1

                if valid_gold:
                    stats['valid_gold'] += 1
                if valid_pred:
                    stats['valid_pred'] += 1

    stats['valid'] = (float(stats['valid_pred']) / stats['valid_gold']) * 100
    stats['acc'] = (float(stats['cnt_corr']) / stats['cnt']) * 100    
    return stats, correct_predictions

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python real_evaluate_v2.py [predictions path], [gold path], [output directory]')
        exit()

pred_path = sys.argv[1]
gold_path = sys.argv[2]
output_path_stats = os.path.join(sys.argv[3], 'stats.txt')
output_path_correct_predictions = os.path.join(sys.argv[3], 'correct_predictions.txt')

nested_dict = lambda: defaultdict(nested_dict)
report = nested_dict()
report, correct_predictions = evaluate(pred_path, gold_path)

with open(output_path_stats, "w+") as open_file:
    open_file.write(json.dumps(report))
    
with open(output_path_correct_predictions, "w+") as open_file:
    for item in correct_predictions:
        open_file.write(str(item))
        open_file.write('\n')

print(report)

