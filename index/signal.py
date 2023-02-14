from index.models import Book
from django.dispatch.dispatcher import Signal, receiver
# from django.dispatch import receiver

book_search_signal = Signal(providing_args=['request', 'book'])
@receiver(book_search_signal, dispatch_uid = "book_search_callback")
def book_search_callback(sender, **kwargs):
    print('book_search_callback回调函数被调用', kwargs['book'].title)