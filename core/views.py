from django.shortcuts import render
from .langchain_helper import generate_answer_from_prompt 


# In-memory history (reset on server restart)
history = []

def index(request):
    result = None
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        if prompt:
            result = generate_answer_from_prompt(prompt)
            history.append(prompt)
    return render(request, "index.html", {"result": result, "history": reversed(history[-10:])})

