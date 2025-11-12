import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from pathlib import Path

CORPUS_PATH = "corpus.jsonl"
TOP_K = 3

def load_corpus(path):
    corpus = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                corpus.append(json.loads(line))
    return corpus
corpus = load_corpus("corpus.jsonl")
texts = [c["text"] for c in corpus]
ids   = [c["id"] for c in corpus]

model = SentenceTransformer("all-MiniLM-L6-v2")
emb = model.encode(texts, convert_to_numpy=True)
index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

def answer_query(query):
    q_emb = model.encode([query])
    D, I = index.search(q_emb, k=TOP_K)

    citations = []
    for i in I[0]:
        citations.append(f"[{ids[i]}]")
    answer = ""
    for i in I[0]:
        answer += texts[i] + " "

    print(f"Q: {query}")
    print(f"A: {answer} {' '.join(citations)}")

with open("queries.jsonl", "r") as file:
    for line in file:
        obj = json.loads(line)
        answer_query(obj["query"])
