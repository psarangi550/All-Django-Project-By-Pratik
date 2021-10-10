from django.shortcuts import render
from django.contrib import messages #importing the messages module
from .forms import SignUpForm
# Create your views here.
def index_view(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(messages.get_level(request))
            messages.add_message(request, messages.DEBUG, "Sign Up Successful")
            messages.add_message(request, messages.INFO, "Sign Up Successful")
            my_msg=messages.get_messages(request)
            print(next(my_msg))
            # for m_msg in my_msg:
            #     print(m_msg)
            form=SignUpForm()
    return render(request, "messageBasicApp/index.html", {"form":form})
