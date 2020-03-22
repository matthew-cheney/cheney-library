class BookAlreadyInDB(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f'BookAlreadyInDB, {self.message}'
        else:
            return 'BookAlreadyInDB has been raised. A book with given isbn already in database.'
