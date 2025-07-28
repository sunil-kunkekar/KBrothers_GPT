#core/views.py 
from django.shortcuts import render
from .langchain_helper import *


# In-memory history (reset on server restart)
history = []

def index(request):
    result = None
    selected_prompt_type = "qa"
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        selected_prompt_type = request.POST.get('prompt_type', 'qa')
        if prompt:
            result = generate_response(prompt, selected_prompt_type)
            history.append((prompt, selected_prompt_type))
    return render(request, "index.html", {
        "result": result,
        "history": reversed(history),
        "selected_prompt_type": selected_prompt_type
    })
