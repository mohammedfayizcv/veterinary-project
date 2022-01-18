from django.shortcuts import redirect

def admin_log(fun):
    def wrap(request,*args,**kwargs):
        if request.session.has_key('sess'):
            return fun(request,*args,**kwargs)
        else:
            return redirect('/login')
    return wrap   
        