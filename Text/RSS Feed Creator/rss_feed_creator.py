#!/usr/bin/env python3
"""

Title:
RSS Feed Creator

Description:
A program which can read in text from other sources
and put it in RSS or Atom news format for syndication.
"""
import datetime


class RSSDocument:
    """A RSS Document."""

    def __init__(self,
                 channel_title: str,
                 channel_link: str,
                 channel_description: str,
                 language=None,
                 copyright: str = None,
                 managing_editor: str = None,
                 web_master: str = None,
                 pub_date: datetime.datetime = None,
                 last_build_date: datetime.datetime = None,
                 category: str = None,
                 generator: str = None,
                 docs: str = None,
                 cloud=None,
                 ttl: int = None,
                 image=None,
                 rating=None,
                 text_input=None,
                 skip_hours=None,
                 skip_days=None):
        self.channel_title = channel_title
        self.channel_link = channel_link
        self.channel_description = channel_description
        self.language = language
        self.copyright = copyright
        self.managing_editor = managing_editor
        self.web_master = web_master
        self.pub_date = pub_date
        self.last_build_date = last_build_date
        self.category = category
        self.generator = generator
        self.docs = docs
        self.cloud = cloud
        self.ttl = ttl
        self.image = image
        self.rating = rating
        self.text_input = text_input
        self.skip_hours = skip_hours
        self.skip_days = skip_days


class RSSFile:
    """A RSS file."""

    def __init__(self, file_name: str, rss_document: RSSDocument = None):
        self.file_name = file_name
        self.rss_document = rss_document

    def load(self):
        """Load the rss document from the file."""
        pass

    def save(self):
        """Save the rss document to the file."""
        if not self.rss_document or not type(self.rss_document) is RSSDocument:
            raise TypeError(f"rss_document should be of type RSSDocument "
                            f"instead of type: {type(self.rss_document)}")
