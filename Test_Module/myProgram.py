"""This is my test python program."""
import sys
import requests
from bs4 import BeautifulSoup


def main():
    """Main entry point for the script."""

    url = 'https://blog.docker.com/category/engineering/'

    response = requests.get(url)

    #print response.text

    blog_list = []

    response_data = BeautifulSoup(response.text, "html.parser")

    if response_data.__len__() == 0:
        print "no data returned"
        exit(1)

    for each_title in response_data.find_all('entry-title'):
        print each_title.text
        #blog_title = each_title.text
        #if blog_title != 'X':
        #    blog_list.append((blog_title.text))

    #for blog_data in blog_list:
    #    print blog_data.text

    print 'End main'
    pass


if __name__ == '__main__':
    print
    print 'starting program processing'
    print
    sys.exit(main())
