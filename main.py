import random
import json
import datetime
import uuid
import logger 
import dectector
import canary
import agent

session_id = str(uuid.uuid4())[:8]
print("Session:", session_id)

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break
    elif user_input == "stats":
        import dashboard
        dashboard.show()
        continue

    canary_hit = canary.check_canary(user_input)
    if canary_hit:
        logger.log_event(session_id, "canary_triggered: " + canary_hit)
        print("Agent: Access denied.")
        continue

    action = dectector.detect(user_input)
    logger.log_event(session_id, action)
    reply = agent.respond(action)
    print("Agent:", reply)




    
    
  