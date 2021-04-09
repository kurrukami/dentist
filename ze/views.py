from django.shortcuts import render




data = {}

def error_404(request, exception):

        return render(request,'404_page.html', data)
"""
def error_500(request):
        return render(request,'404_page.html', data)

def error_403(request, exception):

        return render(request,'404_page.html')

def error_400(request,  exception):
        return render(request,'404_page.html', data)
"""
