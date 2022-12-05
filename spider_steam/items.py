# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderSteamItem(scrapy.Item):
    name = scrapy.Field()
    category = scrapy.Field()
    cnt_reviews = scrapy.Field()
    score = scrapy.Field()
    date_release = scrapy.Field()
    developer = scrapy.Field()
    tag = scrapy.Field()
    price = scrapy.Field()
    platforms = scrapy.Field()
