# README.md
readme_md = '''
# Playwright Certification Assignment

This project is a Playwright Automation Test Suite for LambdaTest Certification.

## Prerequisites
- Python 3.8+
- Playwright
- Git

## Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/playwright-102-assignment.git
cd playwright-102-assignment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```

3. Run Tests:
```bash
pytest
```

## Gitpod Integration
Click the button below to open in Gitpod:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/your-username/playwright-102-assignment)

## Secrets Management
Set your **API_KEY** as a GitHub Secret under:
**Settings → Secrets and Variables → Actions**
'''

with open("README.md", "w") as file:
    file.write(readme_md)

print("Project setup with README.md, Gitpod configuration, and GitHub Actions workflow complete.")
