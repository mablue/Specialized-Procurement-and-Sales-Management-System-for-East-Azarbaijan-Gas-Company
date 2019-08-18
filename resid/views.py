from django.shortcuts import render


def report(request):
    return render(request, 'reports/ResidReport.html')
