from django.http import HttpResponse
from django.shortcuts import render
from .models import CarModel


def cars_list_view(request):
    cars = CarModel.objects.all()
    q = request.GET.get('q')
    books = None

    if q:
        books = cars.filter(title__icontains=q)

    context = {'books': books}
    return render(request, 'cars.html', context)


def car_detail_view(request, pk):
    book = CarModel.objects.filter(id=pk).first()
    if book:
        context = {'book': book}
        return render(request, 'book-detail.html', context)
    else:
        return HttpResponse('Book not found')


def download_car_image(request, pk):
    book = CarModel.objects.filter(id=pk).first()

    if book:
        file_path = str(book.ebook)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            return response
    else:
        return HttpResponse("Book not found")
