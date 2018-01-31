"""This is my test python program."""
import sys
import requests
from bs4 import BeautifulSoup

url = 'https://blog.docker.com/category/engineering/'

blog_list = []
response_date = []


def verify_url_response_data(response_data):
    if response_data.__len__() == 0:
        print "no data returned"
        exit(1)


def verify_response_is_valid(response):
    if not response:
        exit(2)


def main():
    """Main entry point for the script."""

    response = requests.get(url)

    verify_response_is_valid(response)

    response_data = BeautifulSoup(response.text, "html.parser")

    verify_url_response_data(response_data)

    for each_title in response_data.find_all(lambda tag: tag.name == 'h2'
                                                         and tag.get('class') == ['entry-title']):
        blog_title = each_title.text
        if blog_title != 'X':
            blog_list.append(blog_title)

    print

    for blog_data in blog_list:
        print "blog_data-" + str(blog_list.index(blog_data)) + ": " + blog_data

    print

    pass


if __name__ == '__main__':
   sys.exit(main())