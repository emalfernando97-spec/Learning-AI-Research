import sys

class ContributionEngine:
    def __init__(self):
        # The threshold for what constitutes a legacy-worthy action
        self.utility_threshold = 0.7

    def _quantify_utility(self, thought: str) -> float:
        """Internal heuristic to filter transient impulses."""
        # High-value markers vs. short-lived impulses
        impact_map = {"humanity": 0.9, "build": 0.8, "dopamine": 0.1, "lust": 0.0}
        return sum(impact_map.get(word, 0.5) for word in thought.lower().split()) / max(len(thought.split()), 1)

    def evaluate_thought(self, thought: str):
        """Determines if a thought/action is worthy of your legacy."""
        utility_score = self._quantify_utility(thought)
        
        if utility_score >= self.utility_threshold:
            print(f"ACCEPTED: '{thought}' aligns with long-term legacy.")
        else:
            print(f"REJECTED: '{thought}' is a transient impulse.")

def main():
    print("--- Systemic Legacy Optimizer Online ---")
    engine = ContributionEngine()

    # Example logic: Testing the current endeavors
    engine.evaluate_thought("Building GitHub infrastructure")
    engine.evaluate_thought("Mindless Dopamine")

if __name__ == "__main__":
    main()
    
