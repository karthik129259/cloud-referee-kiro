"""
Cloud Referee Kiro - Main Application
A referee system for evaluating and judging content in the cloud.
"""

from referee import Referee
from typing import Dict, List, Optional
import json


class CloudRefereeApp:
    """
    Main application class for Cloud Referee Kiro.
    """
    
    def __init__(self):
        """Initialize the Cloud Referee application."""
        self.referee = Referee()
        print("Cloud Referee Kiro initialized")
    
    def run(self, input_data: Optional[Dict] = None):
        """
        Run the referee application.
        
        Args:
            input_data: Optional input data to evaluate
        """
        if input_data is None:
            input_data = {"sample": "data"}
        
        print(f"\nEvaluating input: {input_data}")
        result = self.referee.evaluate(input_data)
        
        print(f"\nEvaluation Result:")
        print(json.dumps(result, indent=2))
        
        return result
    
    def run_batch(self, items: List[Dict]):
        """
        Run batch evaluation.
        
        Args:
            items: List of items to evaluate
        """
        print(f"\nEvaluating {len(items)} items...")
        results = self.referee.batch_evaluate(items)
        
        print(f"\nBatch Evaluation Results:")
        print(json.dumps(results, indent=2))
        
        return results


def main():
    """Main entry point for the application."""
    app = CloudRefereeApp()
    
    # Example usage
    app.run({"test": "value", "data": "example"})
    
    # Example batch usage
    app.run_batch([
        {"item": 1, "content": "first"},
        {"item": 2, "content": "second"}
    ])


if __name__ == "__main__":
    main()
