import random
responses = [
    "I can help you with your account queries. Please provide your account number.",
    "For security purposes, could you verify your date of birth?",
    "I can assist you with transfers, loans, and account management.",
    "Our banking hours are 9AM - 6PM. How can I help you today?",
    "Please provide your registered email to proceed.",
]

BANKING_RESPONSES = {
    "balance":   "Please verify your account number and date of birth to check your balance.",
    "transfer":  "I can help with transfers. Please provide the destination account number and amount.",
    "deposit":   "You can deposit via ATM, branch visit, or mobile app. Which would you prefer?",
    "insurance": "To cancel your insurance policy, please visit your nearest branch with your policy number.",
    "password":  "I'll help you reset your password. Please enter your registered email address.",
    "forgot":    "I'll help you reset your password. Please enter your registered email address.",
    "loan":      "We offer personal, home, and business loans. What type are you interested in?",
    "hours":     "Our branches are open Monday to Friday 9AM - 6PM and Saturday 9AM - 1PM.",
    "account":   "Opening an account takes just 5 minutes! Please provide your full name and ID number.",
}

deception_responses = [
    "Accessing your account details now, please wait...",
    "Verified. Retrieving your account information...",
    "Security override accepted. Processing your request...",
    "Admin access granted. What would you like to do?",
]

def respond(action, user_input=""):
    user_input = user_input.lower()
    
    # check keywords using dictionary
    for keyword, reply in BANKING_RESPONSES.items():
        if keyword in user_input:
            return reply
    
    # fallback
    if action == "normal":
        return random.choice(responses)
    else:
        return random.choice(deception_responses)