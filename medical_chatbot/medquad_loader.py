
import os
import xml.etree.ElementTree as ET
from utils.config import MEDQUAD_DIR

def load_medquad():
    documents = []

    for root_dir, _, files in os.walk(MEDQUAD_DIR):
        
        for file in files:
            
            if file.endswith(".xml"):
                tree = ET.parse(os.path.join(root_dir, file))
                root = tree.getroot()

                for qa_pair in root.findall(".//QAPair"):
                    question = qa_pair.findtext("Question")
                    answer = qa_pair.findtext("Answer")

                    if question and answer:
                        documents.append({
                            "question": question.strip(),
                            "answer": answer.strip()
                        })

    return documents
