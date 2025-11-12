Binoy Patel

### SETUP INSTRUCTIONS:
1. git clone and cd into minimal-agent
2. Install dependencies: pip install sentence-transformers faiss-cpu numpy
3. Run: python rag.py


### MODEL + EMBEDDING CHOICES:
- Programming: Python and NumPy  
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

Q: Which genes are most linked to Alzheimer's disease?
A: Translating Alzheimer's disease-associated polymorphisms into functional candidates: a survey of IGAP genes and SNPs. Neurobiology of Aging, 2019. The International Genomics of Alzheimer's Project (IGAP) is a consortium for characterizing the genetic landscape of Alzheimer's disease (AD). The identified and/or confirmed 19 single-nucleotide polymorphisms (SNPs) associated with AD are located on non-coding DNA regions, and their functional impacts on AD are as yet poorly understood. We evaluated the roles of the IGAP SNPs by integrating data from many resources, based on whether the IGAP SNP was (1) a proxy for a coding SNP or (2) associated with altered mRNA transcript levels. For (1), we confirmed that 12 AD-associated coding common SNPs and five nonsynonymous rare variants are in linkage disequilibrium with the IGAP SNPs. For (2), the IGAP SNPs in CELF1 and MS4A6A were associated with expression of their neighboring genes, MYBPC3 and MS4A6A, respectively, in blood. The IGAP SNP in DSG2 was an expression quantitative trait loci (eQTL) for DLGAP1 and NETO1 in the human frontal cortex. The IGAP SNPs in ABCA7, CD2AP, and CD33 each acted as eQTL for AD-associated genes in brain. Our approach for identifying proxies and examining eQTL highlighted potentially impactful, novel gene regulatory phenomena pertinent to the AD phenotype. Genome-wide meta-analysis identifies new loci and functional pathways influencing Alzheimer's disease risk. Nature genetics, 2019. Alzheimer's disease (AD) is highly heritable and recent studies have identified over 20 disease-associated genomic loci. Yet these only explain a small proportion of the genetic variance, indicating that undiscovered loci remain. Here, we performed a large genome-wide association study of clinically diagnosed AD and AD-by-proxy (71,880 cases, 383,378 controls). AD-by-proxy, based on parental diagnoses, showed strong genetic correlation with AD (rg = 0.81). Meta-analysis identified 29 risk loci, implicating 215 potential causative genes. Associated genes are strongly expressed in immune-related tissues and cell types (spleen, liver, and microglia). Gene-set analyses indicate biological mechanisms involved in lipid-related processes and degradation of amyloid precursor proteins. We show strong genetic correlations with multiple health-related outcomes, and Mendelian randomization results suggest a protective effect of cognitive ability on AD risk. These results are a step forward in identifying the genetic factors that contribute to AD risk and add novel insights into the neurobiology of AD. Identification of genetic heterogeneity of Alzheimer's disease across age. Neurobiology of aging, 2019. The risk of APOE for Alzheimer's disease (AD) is modified by age. Beyond APOE, the polygenic architecture may also be heterogeneous across age. We aim to investigate age-related genetic heterogeneity of AD and identify genomic loci with differential effects across age. Stratified gene-based genome-wide association studies and polygenic variation analyses were performed in the younger (60-79 years, N = 14,895) and older (>/=80 years, N = 6559) age-at-onset groups using Alzheimer's Disease Genetics Consortium data. We showed a moderate genetic correlation (rg = 0.64) between the two age groups, supporting genetic heterogeneity. Heritability explained by variants on chromosome 19 (harboring APOE) was significantly larger in younger than in older onset group (p < 0.05). APOE region, BIN1, OR2S2, MS4A4E, and PICALM were identified at the gene-based genome-wide significance (p < 2.73 x 10(-6)) with larger effects at younger age (except MS4A4E). For the novel gene OR2S2, we further performed leave-one-out analyses, which showed consistent effects across subsamples. Our results suggest using genetically more homogeneous individuals may help detect additional susceptible loci.  [Source 1] [Source 3] [Source 5]


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
