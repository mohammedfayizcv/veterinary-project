from django.shortcuts import redirect

def staff_log(fun):
    def wrap(request,*args,**kwargs):
        if request.session.has_key('sTAFF'):
            return fun(request,*args,**kwargs)
        else:
            return redirect('/login')
    return wrap   
        
        