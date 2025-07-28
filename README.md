
## To Run this Project follow below:

```bash
python -m venv venv
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
```
KBrothers_GPT First Flow
Connects to Gemini via LangChain

Uses a prompt template to shape user questions

Sends question via invoke() pipeline

Returns descriptive, structured responses

UI displays answer and tracks question history
```