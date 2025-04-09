# Git and CI/CD Laboratory Report

## Authors
- Kadirhan Emre Memiş

## Repository Link
[https://github.com/kassvl/git_lab_repository](https://github.com/kassvl/git_lab_repository)

## Steps Performed During the Lab and Observations

### 1. Creating a Python Project
A new Python project was created in PyCharm. The project includes a basic calculator application and consists of the following files:

- `main.py`: Main application file
- `calculator.py`: Calculator class
- `test_main.py`: Test file for the main application
- `test_calculator.py`: Test file for the calculator class
- `requirements.txt`: Project dependencies
- `README.md`: Project description

### 2. Setting Up a Git Repository and Connecting to GitHub
A local Git repository was created and connected to GitHub. The initial commit included the basic project structure.

```bash

git init


git remote add origin https://github.com/kassvl/git_lab_repository.git


git add .
git commit -m "Initial commit: Basic project structure with main.py and tests"
```

### 3. Making Changes, Committing, and Pushing
The `calculator.py` file was added to the project, and a `Calculator` class was created to perform basic arithmetic operations. The changes were committed and pushed to GitHub.

```bash

git add .
git commit -m "Add Calculator class with basic arithmetic operations"


git push -u origin main
```

### 4. Git Workflows

#### Creating a New Branch and Making Changes
A new branch named `feature/add-calculator` was created, and the `Calculator` class was developed on this branch.

```bash
# Create new branch
git checkout -b feature/add-calculator

# Commit changes
git add .
git commit -m "Add Calculator class with basic arithmetic operations"
```

#### Switching Between Branches
Switching between branches was performed.

```bash
# Switch to main branch
git checkout main

# Switch to feature branch
git checkout feature/add-calculator
```

#### Merging Changes
Changes from the feature branch were merged into the main branch.

```bash
# Switch to main branch
git checkout main

# Merge feature branch
git merge feature/add-calculator
```

#### Pushing a Branch to GitHub
The feature branch was pushed to GitHub.

```bash
# Push feature branch
git push -u origin feature/add-calculator
```

### 5. CI/CD Configuration
A CI/CD pipeline was set up using GitHub Actions. The `.github/workflows/main.yml` file defines a workflow that installs dependencies and runs tests.

```yaml
name: Python CI

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install pytest
    
    - name: Test with pytest
      run: |
        pytest test_main.py
```

## Screenshots and Code Snippets of Key Operations

### Calculator Class
```python
class Calculator:
   
    
    def add(self, a, b):
      
        return a + b
    
    def subtract(self, a, b):
     
        return a - b
    
    def multiply(self, a, b):
       
        return a * b
    
    def divide(self, a, b):
      
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
```

### Main Application
```python
from calculator import Calculator

def main():
    print("Hello, Git Lab Project!")
    print("This is a demonstration of version control with PyCharm and GitHub.")
    
    calc = Calculator()
    print("\nCalculator Demo:")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 7 * 6 = {calc.multiply(7, 6)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")

if __name__ == "__main__":
    main()
```

### Test File
```python
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
```

## Challenges Faced and Solutions Applied

### Challenge 1: GitHub Connection
Initially, the GitHub repository URL was not set correctly, causing the push operation to fail.

**Solution:** The remote repository URL was corrected using the `git remote set-url` command:
```bash
git remote set-url origin https://github.com/kassvl/git_lab_repository.git
```

### Challenge 2: Branch Merging
Conflicts may occur when merging changes from the feature branch into the main branch.

**Solution:** Conflicts were resolved manually, and the merge operation was completed.

## Final State of the Repository

### File Structure
```
.
u251cu2500u2500 .git/
u251cu2500u2500 .github/
u2502   u2514u2500u2500 workflows/
u2502       u2514u2500u2500 main.yml
u251cu2500u2500 README.md
u251cu2500u2500 calculator.py
u251cu2500u2500 main.py
u251cu2500u2500 requirements.txt
u251cu2500u2500 test_calculator.py
u2514u2500u2500 test_main.py
```

### Branches
- `main`: Main branch containing the stable version of the project
- `feature/add-calculator`: Branch created to develop the calculator feature

### Commit History
```
f68f7ee (HEAD -> main, origin/main, feature/add-calculator) Add Calculator class with basic arithmetic operations
67f5af7 Initial commit: Basic project structure with main.py and tests
```

## Conclusion
This laboratory exercise provided practical experience with version control in PyCharm and CI/CD integration. The basic commands of Git and integration with GitHub were successfully implemented. Automatic test execution was configured using GitHub Actions. A simple calculator application was developed in the project, allowing version control and CI/CD processes to be experienced on a real application.
