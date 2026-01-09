"""
Cloud Referee Application
Main entry point for the cloud referee service.
"""

from referee import Referee


def main():
    """Main function to run the cloud referee application."""
    referee = Referee()
    referee.run()


if __name__ == "__main__":
    main()
