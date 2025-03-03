from csv import reader

def title_count():
    purple = '\u001b[35m'
    clear_text = '\u001b[0m'

    with open('books-en.csv', 'r') as csvfile:
        table = reader(csvfile, delimiter=';')
        title_counter = 0
        for row in table:
            if row[2] == 'Book-Title':
                continue
            if len(row[2]) > 30:
                title_counter += 1
    print(purple)
    print(f'The amount of books with title longer than 30 symbols: {title_counter}')
    print(clear_text)


def book_search():
    cyan = '\u001b[36m'
    blue = '\u001b[34m'
    clear_text = '\u001b[0m'

    while True:
        flag = 0
        search = input(f'{blue}Type "0" to quit. Type an author to search for their books:{clear_text}   ')
        if search == '0':
            break
        print()
        with open('books-en.csv', 'r') as csvfile:
            table = reader(csvfile, delimiter=';')
            for row in table:
                lower_case = row[2].lower()
                index = lower_case.find(search.lower())
                if index != -1 and (row[3] in ['1991', '1996']):
                    print(f'{cyan}{row[2]}.{clear_text} "{row[1]}" - {row[3]}')
                    flag += 1
            if flag == 0:
                print('No results.')
            else:
                print()
                print(f'Found {flag} results.')
                print()


def bib_ref_gen():
    with open('books-en.csv', 'r', ) as csvfile:
        table = reader(csvfile, delimiter=';')
        output = open('bib_ref.txt', 'w')
        counter = 0
        for row in table:
            output.write(f'{row[2]}. {row[1]} - {row[3]}\n')
            counter += 1
            if counter == 21: break
        output.close()

if __name__ == '__main__':
    title_count()
    book_search()
    bib_ref_gen()