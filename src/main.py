---

## ⚡ Run Locally
```bash
git clone https://github.com/YOUR-ORG/discovery-service.git
cd discovery-service

# Create venv
python -m venv venv
source venv/bin/activate

# Install deps
pip install -r requirements.txt

# Run
uvicorn src.main:app --reload