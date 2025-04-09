# Git Lab Project

This project demonstrates version control with PyCharm, Git, and GitHub, along with CI/CD integration using GitHub Actions.

## Project Structure

- `main.py`: The main Python script
- `calculator.py`: Calculator class with basic arithmetic operations
- `test_main.py`: Unit tests for the main script
- `test_calculator.py`: Unit tests for the calculator class
- `.github/workflows/main.yml`: CI/CD configuration for GitHub Actions

## Setup Instructions

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main script: `python main.py`
4. Run tests: `pytest test_main.py`

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration. The pipeline:

1. Installs dependencies
2. Runs tests
3. Reports test results

https://github.com/kassvl/git_lab_repository