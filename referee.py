"""
Referee module for Cloud Referee Kiro.
Handles the core referee logic and decision-making processes.
"""

import os
from typing import Dict, List, Optional


class Referee:
    """
    Main Referee class that evaluates and makes judgments.
    """
    
    def __init__(self, prompt_file: str = "prompts/referee_prompt.txt"):
        """
        Initialize the Referee with a prompt configuration.
        
        Args:
            prompt_file: Path to the referee prompt file
        """
        self.prompt_file = prompt_file
        self.prompt = self._load_prompt()
    
    def _load_prompt(self) -> str:
        """
        Load the referee prompt from file.
        
        Returns:
            The prompt text as a string
        """
        try:
            with open(self.prompt_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except FileNotFoundError:
            return "Default referee prompt: Evaluate the input fairly and objectively."
    
    def evaluate(self, input_data: Dict) -> Dict:
        """
        Evaluate the input data and return a judgment.
        
        Args:
            input_data: Dictionary containing data to be evaluated
            
        Returns:
            Dictionary containing the evaluation results
        """
        result = {
            "status": "evaluated",
            "input": input_data,
            "judgment": self._make_judgment(input_data),
            "prompt_used": self.prompt
        }
        return result
    
    def _make_judgment(self, input_data: Dict) -> str:
        """
        Make a judgment based on the input data.
        
        Args:
            input_data: Dictionary containing data to be evaluated
            
        Returns:
            Judgment as a string
        """
        # Basic judgment logic - can be extended
        if not input_data:
            return "No data provided for evaluation"
        
        return f"Evaluated {len(input_data)} items"
    
    def batch_evaluate(self, items: List[Dict]) -> List[Dict]:
        """
        Evaluate multiple items in batch.
        
        Args:
            items: List of items to evaluate
            
        Returns:
            List of evaluation results
        """
        results = []
        for item in items:
            results.append(self.evaluate(item))
        return results
