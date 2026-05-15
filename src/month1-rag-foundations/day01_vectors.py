import json
import math

# --- STEP 1: A fake "embedding" to understand the structure---
# Real Embeddings may have upto 1536 dimensions, in the case of Open AI models.
# Here, we will start small with 4

# Sample 1: TCS invoice with 4.5L  due March 31
invoice_a = [0.9, 0.1, 0.8, 0.2]

# Sample 2: Infosys invoice with 3.5L
invoice_b =[0.85, 0.15, 0.75, 0.25]

# Sample 3: Some unknown vendor with bogus invoice informations
invoice_c = [0.1, 0.9, 0.2, 0.8]

# --- STEP 2: Preparing Cosine Similarity in the manual way ---
def cosine_similarity(vec_a, vec_b):
    dot_product_ab = sum(a*b for a,b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a**2 for a in vec_a))
    magnitude_b = math.sqrt(sum(b**2 for b in vec_b))
    return dot_product_ab /(magnitude_a * magnitude_b)

# --- STEP 3: Compare all the above three invoices one over other ---
cos_sim_ab = cosine_similarity(invoice_a, invoice_b)
cos_sim_bc = cosine_similarity(invoice_b, invoice_c)
cos_sim_ac = cosine_similarity(invoice_a, invoice_c)

print(f"Similiarity between TCS and Infosys : {cos_sim_ab:.4f} ← expect HIGH (same category)")
print(f"Similiarity between Infosys and Unknown vendor : {cos_sim_bc:.4f} ← expect LOW (different category)")
print(f"Similiarity between TCS and Unknown vendor : {cos_sim_ac:.4f} ← expect LOW (different category)")

# --- STEP 4 : My domain insight as JSON ---
result = {"concept":"cosine similarity",
          "business_case":"Detect semantically anomalous Vs. historical corpus.",
          "treshold_flag":0.75,
          "test_case":[
                      {"pair":"Tata vs Infosys", 
                       "score": round(cos_sim_ab, 4), 
                       "flag": cos_sim_ab < 0.75},
                      {"pair":"Infosy vs Unknown", 
                       "score": round(cos_sim_bc, 4), 
                       "flag": cos_sim_bc < 0.75},
                       {"pair":"TCS vs Unknown", 
                       "score": round(cos_sim_ac, 4), 
                       "flag": cos_sim_ac < 0.75}
          ]

          }

print("\n--- Structured Output (your first JSON artifact) ---")
print(json.dumps(result, indent=2))