import requests
from bs4 import BeautifulSoup
import csv


def get_books_from_page(soup):
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find(
            'p', class_='instock availability').text.strip()
        books.append({
            'title': title,
            'price': price,
            'availability': availability
        })
    return books


def scrape_books(base_url):
    books = []
    url = base_url
    while True:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page: {url}")
            break

        soup = BeautifulSoup(response.content, 'lxml')
        page_books = get_books_from_page(soup)
        books.extend(page_books)

        # Print status message
        print(f"Scraped {len(books)} book(s)")

        # Find the 'next' button to navigate to the next page
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page = next_button.a['href']
            url = base_url.rsplit('/', 1)[0] + '/' + next_page
        else:
            break

    return books


if __name__ == "__main__":
    base_url = 'https://books.toscrape.com/catalogue/page-1.html'
    all_books = scrape_books(base_url)

    # Save data to CSV file
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file, fieldnames=['title', 'price', 'availability'])
        writer.writeheader()
        for book in all_books:
            writer.writerow(book)

    print(f"Total books scraped: {len(all_books)}")
