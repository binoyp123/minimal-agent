Binoy Patel

### SETUP INSTRUCTIONS:
1. git clone and cd into minimal-agent
2. Install dependencies: pip install sentence-transformers faiss-cpu numpy chromadb transformers
3. Run: python rag.py


### MODEL + EMBEDDING CHOICES:
- Programming: Python
        Rationale: Easy to handle and debug when coming across errors. Python is  
                   also most compatible and widely used/accepted.  
- Sentence Encoder: sentence-transformers/all-MiniLM-L6-v2  
        Rationale: It is lightweight, accurate, and fast for semantic similarity.  
- Vector Index: faiss-cpu  
        Rationale: Fast and reliable similarity search even on small databases.  


### RETRIVAL SETTINGS (k, chunk size, threshold):
1. k = 3: return top 3 most relevant corpus snippets
2. Chunk size: Each entry is small summary from the paper
3. Threshold: No threshold required for small data set. All retrieved snippets included.


### EXAMPLE OUTPUT:
```text
Q: Which genes are most linked to Alzheimer's disease?
Top matches:
   #1: id=Source 1  L2=0.64
   #2: id=Source 3  L2=0.73
   #3: id=Source 5  L2=0.79
A: IGAP studies found several DNA changes linked to Alzheimer's and how they affect nearby genes. Large genetic studies found many new risk genes tied to the immune system and fat metabolism. Younger and older patients can have different genetic risks for Alzheimer’s, especially with APOE. [Source 1] [Source 3] [Source 5]
```


### EVALUTATION TABLE:

| Question                                                                    | What it found?                                              | Was it accurate? |
| --------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| Which genes are most linked to Alzheimer's disease?                         | Retrieved studies mentioning APOE, CD33, and other genes.   | Yes.             |
| How/why does age play a role in Alzheimer's disease?                        | Found info explaining how APOE effects vary by age.         | Yes.             |
| What do the studies say about the role of the immune system in Alzheimer's? | Retrieved studies on immune system and how it plays a role. | Yes.             |
| How does APOE affect the chance of getting Alzheimer's?                     | Found papers on APOE-related genetic risk.                  | Yes.             |
| What are some new findings scientists have discovered in recent years?      | Showed new studies identifying new loci.                    | Yes.             |



### COST NOTES:
- Project runs offline
- Uses free open-source models from sentence-transformers library
- Total runtime cost: 0


### Notes on Bonus Features:
I attempted to implement one of the bonus features, specifically the "Reranking" one. I tried using a cross-encoder, like the document said, to rerank the top results for better accuracy. However, I failed to complete that task. I believe it didn't work because my code wasn't matching the IDs correctly, so everything got out of synch.
