"""
Referee Module
Handles the core referee functionality for cloud operations.
"""

import os


class Referee:
    """Cloud Referee class for managing and validating cloud operations."""

    def __init__(self):
        """Initialize the Referee with default settings."""
        self.prompt_path = os.path.join(
            os.path.dirname(__file__), "prompts", "referee_prompt.txt"
        )

    def load_prompt(self):
        """Load the referee prompt from file."""
        try:
            with open(self.prompt_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt file not found: {self.prompt_path}")
        except IOError as e:
            raise IOError(f"Error reading prompt file: {e}")

    def run(self):
        """Run the referee process."""
        prompt = self.load_prompt()
        print("Cloud Referee initialized with prompt:")
        print(prompt)
