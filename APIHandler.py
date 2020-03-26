import json
import datetime

from requests import get

from models.Book import Book

HEADER = {'email': 'matthew@cheneycreations.com'}

def get_book_from_api(isbn):
    url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data'
    r = get(url=url, headers=HEADER)
    if r.status_code == 200:
        # Successful request, parse info
        metadata = json.loads(r.text)
        if len(metadata.keys()) > 1:
            print('not sure what to do here.....')
            print(url)
            print(metadata)
            exit(1)
        isbn_key = next(iter(metadata))
        in_d = metadata[isbn_key]
        title = in_d.get('title')
        authors_list = in_d.get('authors')
        if authors_list is not None:
            authors = [x.get('name') for x in authors_list]
        else:
            authors = None
        date_added = datetime.datetime.now()
        url = in_d.get('url')
        subjects_list = in_d.get('subjects')
        if subjects_list is not None:
            subjects = [x.get('name') for x in subjects_list]
        else:
            subjects = None
        subject_places_list = in_d.get('subjects')
        if subject_places_list is not None:
            subject_places = [x.get('name') for x in subject_places_list]
        else:
            subject_places = None
        subject_people_list = in_d.get('subjects')
        if subject_people_list is not None:
            subject_people = [x.get('name') for x in subject_people_list]
        else:
            subject_people = None
        subject_times_list = in_d.get('subjects')
        if subject_times_list is not None:
            subject_times = [x.get('name') for x in subject_times_list]
        else:
            subject_times = None
        publishers_list = in_d.get('publishers')
        if publishers_list is not None:
            publishers = [x.get('name') for x in publishers_list]
        else:
            publishers = None
        publish_places_list = in_d.get('publish_places')
        if publish_places_list is not None:
            publish_places = [x.geT('name') for x in publish_places_list]
        else:
            publish_places = None
        publish_date = in_d.get('publish_date')

        if 'cover' in in_d:
            if 'medium' in in_d.get('cover'):
                cover_url = in_d.get('cover').get('medium')
            elif 'large' in in_d.get('cover'):
                cover_url = in_d.get('cover').get('large')
            else:
                cover_url = in_d.get('cover').get('small')
            # cover_filename = f'{isbn}_cover.jpg'
            # with open(f'cover_images/{cover_filename}', 'wb') as f:
            #     f.write(cover_r.content)
        else:
            cover_url = None
        number_of_pages = in_d.get('number_of_pages')
        weight = in_d.get('weight')
        book = Book(
            isbn=isbn,
            title=title,
            authors=authors,
            date_added=date_added,
            url=url,
            subjects=subjects,
            subject_places=subject_places,
            subject_people=subject_people,
            subject_times=subject_times,
            publishers=publishers,
            publish_places=publish_places,
            publish_date=publish_date,
            cover_url=cover_url,
            number_of_pages=number_of_pages,
            weight=weight,
        )
        return book
    elif r.status_code == 404:
        # Book now found
        return None
    elif r.status_code == 429:
        # Max usage hit
        return None
    else:
        # All other status_codes
        return None