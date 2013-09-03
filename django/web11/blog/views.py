# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Author,Book

def book(req,id):
    if id=='':
        author = 'book'
        book_list = Book.objects.all()
    else:
        author = Author.objects.get(id=id)
        book_list = author.book_set.all()
    return render_to_response('book.html',{'author':author,'book_list':book_list})

def author(req,id):
    if id=='':
        book = 'author'
        author_list = Author.objects.all()
    else:
        book = Book.objects.get(id=id)
        author_list = book.authors.all()
    return render_to_response('author.html',{'book':book,'author_list':author_list})
