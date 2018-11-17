#!/usr/bin/env python
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
        'CHANNEL_THUMBNAIL': 'https://goalkicker.com/JavaScriptBook/JavaScriptGrow.png',
        'CHANNEL_DESCRIPTION': 'Programming Notes for Professionals books',
    }

    def construct_channel(self, **kwargs):
        channel = self.get_channel(**kwargs)
        potato_topic = TopicNode(title="Potatoes!", source_id="<potatos_id>")
        channel.add_child(potato_topic)
        doc_node = DocumentNode(
            title='Growing potatoes',
            description='An article about growing potatoes on your rooftop.',
            source_id='pubs/mafri-potatoe',
            license=get_license('CC BY', copyright_holder='University of Alberta'),
            language='en',
            files=[DocumentFile(path='https://www.gov.mb.ca/inr/pdf/pubs/mafri-potatoe.pdf',
                                language='en')],
        )
        potato_topic.add_child(doc_node)
        return channel


if __name__ == '__main__':
    """
    Run this script on the command line using:
        python goalkicker_chef.py -v --reset --token=YOURTOKENHERE9139139f3a23232
    """
    goalkicker_chef = GoalkickerChef()
    goalkicker_chef.main()

