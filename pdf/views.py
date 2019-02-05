from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
from django_xhtml2pdf.utils import generate_pdf


def index(request):
    return render(request, 'index.html')


def pdf(request):
    html_string = render_to_string('index.html', {})

    html = HTML(string=html_string)
    html.write_pdf(target='./tmp/mypdf.pdf')

    fs = FileSystemStorage('./tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response


def pdf2(request):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('index.html', file_object=resp)
    return result
