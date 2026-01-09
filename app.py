"""Cloud Referee Application - Main entry point."""

from referee import Referee


def main():
    """Main function to run the Cloud Referee application."""
    referee = Referee()
    referee.run()


if __name__ == "__main__":
    main()
