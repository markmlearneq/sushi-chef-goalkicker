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
        algorithms_topic = TopicNode(title="Algorithms Notes for Professionals book", source_id="algorithms")
        channel.add_child(algorithms_topic)
        doc_node = DocumentNode(
            title='Algorithms Notes for Professionals',
            description='',
            source_id='goalkicker/AlgorithmsBook',
            license=get_license('CC BY', copyright_holder='University of Alberta'),
            language='en',
            files=[DocumentFile(path='https://goalkicker.com/AlgorithmsBook/AlgorithmsNotesForProfessionals.pdf',
                                language='en')],
        )
        algorithms_topic.add_child(doc_node)
        return channel


if __name__ == '__main__':
    """
    Run this script on the command line using:
        python goalkicker_chef.py -v --reset --token=YOURTOKENHERE9139139f3a23232
    """
    goalkicker_chef = GoalkickerChef()
    goalkicker_chef.main()

