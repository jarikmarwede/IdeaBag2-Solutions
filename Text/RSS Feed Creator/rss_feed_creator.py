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
        tree = ET.ElementTree(ET.Element("rss", {"version": "2.0"}))
        root = tree.getroot()
        channel = ET.SubElement(root, "channel")
        channel_title = ET.SubElement(channel, "title")
        channel_title.text = self.rss_document.channel_title
        channel_link = ET.SubElement(channel, "link")
        channel_link.text = self.rss_document.channel_link
        channel_description = ET.SubElement(channel, "description")
        channel_description.text = self.rss_document.channel_description
        for item in self.rss_document.items:
            item_element = ET.SubElement(channel, "item")
            title = ET.SubElement(item_element, "title")
            title.text = item.title
            if item.link:
                link = ET.SubElement(item_element, "link")
                link.text = item.link
            if item.description:
                description = ET.SubElement(item_element, "description")
                description.text = item.description
            if item.author:
                author = ET.SubElement(item_element, "author")
                author.text = item.author
            if item.category:
                category = ET.SubElement(item_element, "category")
                category.text = item.category
            if item.comments:
                comments = ET.SubElement(item_element, "comments")
                comments.text = item.comments
            if item.enclosure:
                enclosure = ET.SubElement(item_element, "enclosure")
                enclosure.text = item.enclosure
            if item.guid:
                guid = ET.SubElement(item_element, "guid")
                guid.text = item.guid
            if item.pub_date:
                pub_date = ET.SubElement(item_element, "pubDate")
                pub_date.text = item.pub_date
            if item.source:
                source = ET.SubElement(item_element, "source")
                source.text = item.source
        if self.rss_document.language:
            language = ET.SubElement(channel, "language")
            language.text = self.rss_document.language
        if self.rss_document.copyright:
            copyright = ET.SubElement(channel, "copyright")
            copyright.text = self.rss_document.copyright
        if self.rss_document.managing_editor:
            managing_editor = ET.SubElement(channel, "managingEditor")
            managing_editor.text = self.rss_document.managing_editor
        if self.rss_document.web_master:
            web_master = ET.SubElement(channel, "webMaster")
            web_master.text = self.rss_document.web_master
        if self.rss_document.pub_date:
            pub_date = ET.SubElement(channel, "pubDate")
            pub_date.text = self.rss_document.pub_date
        if self.rss_document.last_build_date:
            last_build_date = ET.SubElement(channel, "lastBuildDate")
            last_build_date.text = self.rss_document.last_build_date
        if self.rss_document.category:
            category = ET.SubElement(channel, "category")
            category.text = self.rss_document.category
        if self.rss_document.generator:
            generator = ET.SubElement(channel, "generator")
            generator.text = self.rss_document.generator
        if self.rss_document.docs:
            docs = ET.SubElement(channel, "docs")
            docs.text = self.rss_document.docs
        if self.rss_document.cloud:
            cloud = ET.SubElement(channel, "cloud")  # TODO
        if self.rss_document.ttl:
            ttl = ET.SubElement(channel, "ttl")
            ttl.text = self.rss_document.ttl
        if self.rss_document.image:
            image = ET.SubElement(channel, "image")  # TODO
        if self.rss_document.rating:
            rating = ET.SubElement(channel, "rating")  # TODO
        if self.rss_document.text_input:
            text_input = ET.SubElement(channel, "textInput")  # TODO
        if self.rss_document.skip_hours:
            skip_hours = ET.SubElement(channel, "skipHours")  # TODO
        if self.rss_document.skip_days:
            skip_days = ET.SubElement(channel, "skipDays")  # TODO

        tree.write(self.file_name)
