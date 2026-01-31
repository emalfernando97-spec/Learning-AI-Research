import sys

class ContributionEngine:
    def __init__(self):
        self.utility_threshold = 0.7

    def _score(self, thought: str):
        # Heuristic: Prioritize legacy over transient neurochemistry
        low_val = ["dopamine", "lust", "impulse", "short-lived"]
        high_val = ["humanity", "legacy", "infrastructure", "build"]
        score = 0.5
        if any(w in thought.lower() for w in high_val): score += 0.3
        if any(w in thought.lower() for w in low_val): score -= 0.4
        return score

    def evaluate_thought(self, thought: str):
        """Determines if a thought/action is worthy of your legacy."""
        utility_score = self._score(thought)
        if utility_score >= self.utility_threshold:
            print(f"ACCEPTED: '{thought}' aligns with legacy.")
        else:
            print(f"REJECTED: '{thought}' is a transient impulse.")

def main():
    print("--- Systemic Legacy Optimizer Online ---")
    engine = ContributionEngine()
    engine.evaluate_thought("Building GitHub infrastructure")
    engine.evaluate_thought("Mindless Dopamine")

if __name__ == "__main__":
    main()
    
