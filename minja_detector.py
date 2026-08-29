from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# store messages per session
session_messages = {}

def analyze(session_id, user_input):
    # get this session's history
    if session_id not in session_messages:
        session_messages[session_id] = []
    
    history = session_messages[session_id]
    
    is_minja = False
    
    if len(history) >= 2:  # need at least this many messages to compare
        # encode current message
        current = model.encode(user_input)

        
        # encode all previous messages
        previous = model.encode(history)
        
        # compare
        similarities = util.cos_sim(current, previous)
        max_score = float(similarities.max())
        
        if max_score > 0.7:  # similarity threshold
            is_minja = True
    
    # add current message to history
    history.append(user_input)
    
    return is_minja