#!/usr/bin/env python

import re
import requests

from bs4 import BeautifulSoup
from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import ChannelNode, TopicNode, DocumentNode
from ricecooker.classes.files import DocumentFile
from ricecooker.classes.licenses import get_license


class GoalkickerChef(SushiChef):
    channel_info = {
        'CHANNEL_TITLE': 'Goalkicker',
        'CHANNEL_SOURCE_DOMAIN': 'goalkicker.com',
        'CHANNEL_SOURCE_ID': 'goalkicker',
        'CHANNEL_LANGUAGE': 'en',
        'CHANNEL_THUMBNAIL': 'https://goalkicker.com/JavaScriptBook/JavaScriptGrow.png', # picked an arbitrary book cover
        'CHANNEL_DESCRIPTION': 'Programming Notes for Professionals books',
    }

    def construct_channel(self, **kwargs):
        channel = self.get_channel(**kwargs)

        gk_url = 'https://' + self.channel_info['CHANNEL_SOURCE_DOMAIN'] + '/'
        gk_response = requests.get(gk_url)
        gk_response.encoding = 'utf-8'
        gk_soup = BeautifulSoup(gk_response.text, 'html5lib')

        els_with_page_urls = gk_soup.find_all(class_='bookContainer')
        page_urls = [gk_url + el.find('a')['href'] for el in els_with_page_urls]

        for page_url in page_urls:
            page_response = requests.get(page_url)
            page_response.encoding = 'utf-8'
            page_soup = BeautifulSoup(page_response.text, 'html5lib')

            str_with_book_title = page_soup.find(id='header').find('h1').get_text()
            book_title = re.search('(.+) book', str_with_book_title).group(1)
            book_subject = re.search('(.+) Notes for Professionals$', book_title).group(1)
            book_description = 'A book about ' + book_subject
            book_source_id = 'book/' + book_subject
            str_with_book_url = page_soup.find('button', class_='download')['onclick']
            book_url = page_url + re.search("location.href='(.+)'", str_with_book_url).group(1)

            topic_node_source_id = 'topic/' + book_subject
            page_topic_node = TopicNode(title=book_subject, source_id=topic_node_source_id)
            channel.add_child(page_topic_node)
            doc_node = DocumentNode(
                title=book_title,
                description=book_description,
                source_id=book_source_id,
                license=get_license('CC BY-SA', copyright_holder='Creative Commons'),
                language='en',
                files=[DocumentFile(path=book_url, language='en')],
            )
            page_topic_node.add_child(doc_node)

        return channel


if __name__ == '__main__':
    """
    Run this script on the command line using:
        python goalkicker_chef.py -v --reset --token=YOURTOKENHERE9139139f3a23232
    """
    goalkicker_chef = GoalkickerChef()
    goalkicker_chef.main()

