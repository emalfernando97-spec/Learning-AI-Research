import sys

class ContributionEngine:
    def __init__(self):
        # The threshold for what constitutes a 'worthy' legacy contribution
        self.utility_threshold = 0.7 

    def evaluate_thought(self, thought: str, utility_score: float):
        """
        Determines if a thought/action is worth the biological energy.
        """
        if utility_score >= self.utility_threshold:
            print(f"ACCEPTED: '{thought}' aligns with long-term legacy.")
        else:
            print(f"REJECTED: '{thought}' is a short-lived distraction.")

def main():
    print("--- Systemic Legacy Optimizer Online ---")
    engine = ContributionEngine()
    
    # Example logic: Testing the current endeavor
    engine.evaluate_thought("Building GitHub Architecture", 0.9)
    engine.evaluate_thought("Mindless Dopamine Scrolling", 0.1)

if __name__ == "__main__":
    main()
