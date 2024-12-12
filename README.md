# Initial setup

mkdir my_fastapi_project
cd my_fastapi_project

python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
pip install -r requirements.txt

## Run the application

uvicorn app.main:app --reload

## When done

deactivate

## Next time you work on the project

cd my_fastapi_project
source venv/bin/activate # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload
