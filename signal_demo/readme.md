README.md Template
# Django Signals & Python Rectangle Class Demo

This project demonstrates:

1. **Django Signals**
   - Synchronous vs asynchronous behavior
   - Thread execution (same or different thread)
   - Transaction execution (same DB transaction)

2. **Python Custom Class**
   - Iterable `Rectangle` class

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/signal_demo.git
cd signal_demo

2. Create virtual environment & install dependencies
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

pip install -r requirements.txt

3. Run Django migrations
python manage.py migrate

4. Test Django Signals
python manage.py shell


Then run:

from core.models import DummyModel
import time

start = time.time()
DummyModel.objects.create(name="Test")
end = time.time()
print("Total time:", end-start)


This will show the synchronous, same-thread, same-transaction behavior of signals.

5. Test Rectangle Class
python core/rectangle_demo.py


Expected output:

{'length': 10}
{'width': 5}

Author

Suhail Shaik


---

## 4️⃣ Git Commands to Upload

From the project root (`signal_demo/`):

```bash
git init
git add .
git commit -m "Initial commit: Django signals demo + Rectangle class"
git branch -M main
git remote add origin https://github.com/<your-username>/signal_demo.git
git push -u origin main
