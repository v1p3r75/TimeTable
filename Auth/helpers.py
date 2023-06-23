from django.shortcuts import redirect

def redirect_authenticated_user(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:

            return redirect_users(request, request.user)
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def redirect_users(request, user):

    if (user.role.id == 1): 

        return redirect('admin-dashboard')
    
    if (user.role.id == 2):

        return redirect('admin-dashboard')
    
    else :

        return redirect('student-dashboard')


