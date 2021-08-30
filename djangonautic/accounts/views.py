from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

# Create your views here.
def signup(request): 
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:articles_list')
        else:
            return render(request, 'accounts/signup.html', {'form': form })
