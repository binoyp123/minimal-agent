import json
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss


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
corpus = load_corpus(CORPUS_PATH)
texts = [c["text"] for c in corpus]
ids   = [c["id"] for c in corpus]

SOURCE_SUMMARIES = {
    "Source 1": "IGAP studies found several DNA changes linked to Alzheimer's and how they affect nearby genes.",
    "Source 2": "AD genetics can differ by clinical background like hypertension. Shows heterogeneity.",
    "Source 3": "Large genetic studies found many new risk genes tied to the immune system and fat metabolism.",
    "Source 4": "Meta-analysis confirmed known loci and added 5 new ones related to Abeta, tau, and immunity.",
    "Source 5": "Younger and older patients can have different genetic risks for Alzheimer’s, especially with APOE."
}

model = SentenceTransformer("all-MiniLM-L6-v2")
emb = model.encode(texts, convert_to_numpy=True)
index = faiss.IndexFlatL2(emb.shape[1])
index.add(emb)

def answer_query(query):
    q_emb = model.encode([query], convert_to_numpy=True)
    D, I = index.search(q_emb, k=TOP_K)

    retrieved_ids = []
    for i in I[0]:
        retrieved_ids.append(ids[i])

    print(f"Q: {query}")
    print("Top matches:")
    for r, idx in enumerate(I[0], 1):
        distance = float(D[0][r - 1])
        print(f"   #{r}: id={ids[idx]}  L2={distance:.2f}")

    summaries = []
    for sid in retrieved_ids:
        if sid in SOURCE_SUMMARIES:
            summaries.append(SOURCE_SUMMARIES[sid])

    if not summaries:
        summaries = ["The retrieved papers describe genetic risk factors for alzheimer's disease."]

    answer_text = " ".join(summaries[:3])
    citations = ""
    for rid in retrieved_ids:
        citations += f"[{rid}] "
    citations = citations.strip()

    print(f"A: {answer_text} {citations}")
    print("*******************")

with open("queries.jsonl", "r") as file:
    for line in file:
        obj = json.loads(line)
        answer_query(obj["query"])
