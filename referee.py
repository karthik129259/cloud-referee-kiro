"""Referee module for Cloud Referee application."""

import os


class Referee:
    """Referee class to handle cloud refereeing operations."""

    def __init__(self):
        """Initialize the Referee with the prompt template."""
        self.prompt_path = os.path.join(
            os.path.dirname(__file__), "prompts", "referee_prompt.txt"
        )
        self.prompt = self._load_prompt()

    def _load_prompt(self):
        """Load the referee prompt from file."""
        if os.path.exists(self.prompt_path):
            with open(self.prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    def run(self):
        """Run the referee process."""
        print("Cloud Referee initialized.")
        if self.prompt:
            print("Prompt loaded successfully.")
        else:
            print("No prompt loaded.")
