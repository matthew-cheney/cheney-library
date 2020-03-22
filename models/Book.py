class Book:

    def __init__(self, isbn, title='', authors=[], date_added='', url='', subjects=[], subject_places=[], subject_people=[], subject_times=[], publishers=[], publish_places=[], publish_date='', cover_filename='', number_of_pages='', weight=''):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.date_added = date_added
        self.url = url
        self.subjects = subjects
        self.subject_places = subject_places
        self.subject_people = subject_people
        self.subject_times = subject_times
        self.publishers = publishers
        self.publish_places = publish_places
        self.publish_date = publish_date
        self.cover_filename = cover_filename
        self.number_of_pages = number_of_pages
        self.weight = weight

    def __repr__(self):
        s = f'isbn: {self.isbn}\n'
        s += (f'title: {self.title}\n' if not self.title == '' else '')
        s += (f'authors: {self.authors}\n' if not self.authors == [] else '')
        s += (f'date_added: {self.date_added}\n' if not self.date_added == '' else '')
        s += (f'url: {self.url}\n' if not self.url == '' else '')
        s += (f'subjects: {self.subjects}\n' if not self.subjects == [] else '')
        s += (f'subject_places: {self.subject_places}\n' if not self.subject_places == [] else '')
        s += (f'subject_people: {self.subject_people}\n' if not self.subject_people == [] else '')
        s += (f'subject_times: {self.subject_times}\n' if not self.subject_times == [] else '')
        s += (f'publishers: {self.publishers}\n' if not self.publishers == [] else '')
        s += (f'publish_places: {self.publish_places}\n' if not self.publish_places == [] else '')
        s += (f'publish_date: {self.publish_date}\n' if not self.publish_date == '' else '')
        s += (f'cover_filename: {self.cover_filename}\n' if not self.cover_filename == '' else '')
        s += (f'number_of_pages: {self.number_of_pages}\n' if not self.number_of_pages == '' else '')
        s += (f'weight: {self.weight}\n' if not self.weight == '' else '')
        return s
