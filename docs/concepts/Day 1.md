# Day 1 - Notes
## Vector
In AI, a **vector is a list of numbers that represents meaning**. When an embedding model processes the sentence, it converts that entire sentence into something like list of numbers! That list of numbers _encodes the semantic meaning_ of the sentence. Two sentences that mean similar things will produce vectors that point in similar directions in `N` dimensional space (for example, N may be 1536-dimensional space for *Open AI* models?). Two sentences that mean completely different things will point in very different directions.
This is the entire foundation of RAG, semantic search, and document retrieval. Every time your system asks "which invoice chunk is most relevant to this question?", it is comparing vectors.
>"Invoice from Tata Consultancy, amount ₹4,50,000, due March 31"
>will be encoded something like:

    [0.023, -0.841, 0.312, 0.009, -0.227, ... ] ← 1536 numbers (for OpenAI's model)

## Cosine Similarity
It measures the **angle** between two vectors — not their distance, their angle. Result is always between -1 and 1:

-   **1.0** → vectors point in exactly the same direction → sentences mean the same thing
-   **0.0** → vectors are perpendicular → sentences are completely unrelated
-   **-1.0** → vectors point in opposite directions → sentences are semantic opposites.
Cosine similarity is calculated by the formula: 
$\text{Cosine Similiarity (A,B)}= \frac{(A.B)}{(|A| \star |B|)}$
**Why angle and not distance?** Because a short sentence and a long sentence about the same topic will have vectors of different magnitudes (lengths), but similar _directions_. Cosine similarity normalises out the length difference and focuses purely on directional agreement — which is what "semantic similarity" actually means.
**Accounts Payable domain analogy:** 
Think of it like a vendor risk score. Two invoices from the same vendor, same product category, similar amounts — their vectors will have cosine similarity close to 0.95. An invoice from an unknown vendor for an unusual service — cosine similarity against your "normal" cluster will drop to 0.3. That's how anomaly detection via embeddings works.
