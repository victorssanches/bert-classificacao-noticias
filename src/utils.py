"""funções auxiliares pro projeto"""

from typing import Dict

def create_label_mappings(selected_classes):
    """cria dicionários label->id e id->label a partir de uma lista de classes."""
    label2id: Dict[str, int] = {label: idx for idx, label in enumerate(selected_classes)}
    id2label: Dict[int, str] = {idx: label for label, idx in label2id.items()}
    return label2id, id2label