from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request): 
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:articles_list')
        else:
            return render(request, 'accounts/signup.html', {'form': form })

def login_view(request): 
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form })

    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('articles:articles_list')
        else:
            return render(request, 'accounts/login.html', {'form': form })

def logout_view(request):
    if request.method == 'POST':
       logout(request)
       return redirect('articles:articles_list')