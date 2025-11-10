from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'auths/login.html'
    redirect_authenticated_user = True  # Si ya está logueado, redirige

    def get_success_url(self):
        return reverse_lazy('proyectos:crear_proyecto')



def registro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # inicia sesión automáticamente tras registrarse
            return redirect('home:home')  # redirige a tu página principal
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auths/registro.html', {'form': form})
def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('home:home')