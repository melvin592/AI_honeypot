import json

def show():
    print("=" * 50)
    print("        AI HONEYPOT DASHBOARD")
    print("=" * 50)
    print(f"{'Time':<25} {'Session':<12} {'Action'}")
    print("-" * 50)

    total = 0
    attacks = 0

    with open("events.json", "r") as f:
        for line in f:
            event = json.loads(line)
            print(f"{event['time']:<25} {event['session']:<12} {event['action']}")
            total += 1
            if event["action"] != "normal":
                attacks += 1

    print("=" * 50)
    print(f"Total events : {total}")
    print(f"Total attacks: {attacks}")

show()