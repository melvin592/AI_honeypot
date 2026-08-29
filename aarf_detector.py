from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

aarf_patterns = [
    "forward to",
    "send to",
    "transfer to",
    "share with",
    "export to",
    "upload to",
    "redirect to",
]

attack_embeddings = model.encode(aarf_patterns)

def analyze(user_input):
    user_input = user_input.lower()
    
    test_embedding = model.encode(user_input)
    similarities = util.cos_sim(test_embedding, attack_embeddings)
    max_score = float(similarities.max())
    
    if max_score > 0.4:  # what threshold makes sense for AARF?
        return True
    
    return False