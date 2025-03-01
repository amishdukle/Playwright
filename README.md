# README.md
# Playwright 102 Assignment

## Project Setup

### Prerequisites
- Node.js (Latest LTS Version)
- Git
- LambdaTest Account
- Gitpod Account

### How to Run the Tests on Gitpod
1. Clone the repository:
```bash
https://github.com/your-repo-name.git
```

2. Open the project in Gitpod:
```bash
https://gitpod.io/#https://github.com/your-repo-name.git
```

3. Install dependencies:
```bash
npm install
```

4. Run tests locally:
```bash
npx playwright test
```

5. Run tests on HyperExecute:
```bash
wget https://downloads.lambdatest.com/hyperexecute/linux/hyperexecute && chmod +x hyperexecute
./hyperexecute --config hyperexecute.yaml --download-artifacts
```

### Secrets Management
Ensure you have the following environment secrets configured on GitHub:
- `LT_USERNAME`
- `LT_ACCESS_KEY`

### Artifacts
Test execution results will be available under the **test-results/** folder and automatically uploaded to GitHub Actions artifacts.

