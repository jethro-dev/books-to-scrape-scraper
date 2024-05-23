# Books to Scrape Scraper

This project is a web scraper for the ["Books to Scrape"](https://books.toscrape.com/) website. It scrapes book details such as title, price, and availability from all the pages on the website.

## Features

- Scrapes book data from all pages of the "Books to Scrape" website.
- Extracts book title, price, and availability.
- Prints the total number of books scraped.
- Provides real-time status updates during scraping.

## Prerequisites

Make sure you have Python installed. This project uses the following Python libraries:

- `requests`
- `beautifulsoup4`
- `lxml`

You can install these libraries using pip:

```sh
pip install requests beautifulsoup4 lxml
```

## Usage

Clone this repository:

```sh
git clone https://github.com/your-username/books-to-scrape-scraper.git
cd books-to-scrape-scraper
```

Run the scraper script:

```sh
python main.py
```

The script will print the details of the books scraped and provide a real-time status update.

## Example Output

```sh
Scraped 20 book(s)
Scraped 40 book(s)
...
Scraped 1000 book(s)
Total books scraped: 1000
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
