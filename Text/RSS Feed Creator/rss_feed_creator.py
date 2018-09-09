#!/usr/bin/env python3
"""

Title:
RSS Feed Creator

Description:
A program which can read in text from other sources
and put it in RSS or Atom news format for syndication.
"""
import datetime
import xml.etree.ElementTree as ET
from typing import List


class RSSItem:
    """An RSS item."""

    def __init__(self,
                 title: str,
                 link: str = None,
                 description: str = None,
                 author: str = None,
                 category: str = None,
                 comments: str = None,
                 enclosure=None,
                 guid: str = None,
                 pub_date: datetime.datetime = None,
                 source: str = None):
        self.title = title
        self.link = link
        self.description = description
        self.author = author
        self.category = category
        self.comments = comments
        self.enclosure = enclosure
        self.guid = guid
        self.pub_date = pub_date
        self.source = source


class RSSDocument:
    """A RSS Document."""

    def __init__(self,
                 channel_title: str,
                 channel_link: str,
                 channel_description: str,
                 items: List[RSSItem],
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
        self.items = items
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
        tree = ET.parse(self.file_name)
        root = tree.getroot()
        channel = root.find("channel")

        channel_title = channel.find("title").text
        channel_link = channel.find("link").text
        channel_description = channel.find("description").text
        items = []
        for item in channel.findall("item"):
            item_title = item.find("title").text
            item_link = item.find("link")
            if item_link:
                item_link = item_link.text
            item_description = item.find("description")
            if item_description:
                item_description = item_description.text
            item_author = item.find("author")
            if item_author:
                item_author = item_author.text
            item_category = item.find("category")
            if item_category:
                item_category = item_category.text
            item_comments = item.find("comments")
            if item_comments:
                item_comments = item_comments.text
            item_enclosure = None  # TODO
            item_guid = item.find("guid")
            if item_guid:
                item_guid = item_guid.text
            item_pub_date = item.find("pubDate")
            if item_pub_date:
                item_pub_date = datetime.datetime.fromisoformat(item_pub_date.text)
            item_source = item.find("source")
            if item_source:
                item_source = item_source.text
            items.append(RSSItem(
                item_title,
                item_link,
                item_description,
                item_author,
                item_category,
                item_comments,
                item_enclosure,
                item_guid,
                item_pub_date,
                item_source
            ))
        language = channel.find("language")
        if language:
            language = language.text
        copyright = channel.find("copyright")
        if copyright:
            copyright = copyright.text
        managing_editor = channel.find("managingEditor")
        if managing_editor:
            managing_editor = managing_editor.text
        web_master = channel.find("webMaster")
        if web_master:
            web_master = web_master.text
        pub_date = channel.find("pubDate")
        if pub_date:
            pub_date = datetime.datetime.fromisoformat(pub_date.text)
        last_build_date = channel.find("lastBuildDate")
        if last_build_date:
            last_build_date = datetime.datetime.fromisoformat(last_build_date.text)
        category = channel.find("category")
        if category:
            category = category.text
        generator = channel.find("generator")
        if generator:
            generator = generator.text
        docs = channel.find("docs")
        if docs:
            docs = docs.text
        cloud = None  # TODO
        ttl = channel.find("ttl")
        if ttl:
            ttl = int(ttl.text)
        image = None  # TODO
        rating = None  # TODO
        text_input = None  # TODO
        skip_hours = None  # TODO
        skip_days = None  # TODO

        self.rss_document = RSSDocument(
            channel_title,
            channel_link,
            channel_description,
            items,
            language,
            copyright,
            managing_editor,
            web_master,
            pub_date,
            last_build_date,
            category,
            generator,
            docs,
            cloud,
            ttl,
            image,
            rating,
            text_input,
            skip_hours,
            skip_days
        )

    def save(self):
        """Save the rss document to the file."""
        if not self.rss_document or not type(self.rss_document) is RSSDocument:
            raise TypeError(f"rss_document should be of type RSSDocument "
                            f"instead of type: {type(self.rss_document)}")
