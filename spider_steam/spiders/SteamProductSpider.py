import scrapy
from spider_steam.items import SpiderSteamItem

import re
import json

queries = ['cs', 'racing', 'anime']


class SteamproductspiderSpider(scrapy.Spider):
    name = 'SteamProductSpider'

    # allowed_domains = ['store.steampowered.com']
    # start_urls = ['https://store.steampowered.com/search/?term=cs',
    #               'https://store.steampowered.com/search/?term=football',
    #               'https://store.steampowered.com/search/?term=minecraft']

    def start_requests(self):
        page = 2
        for query in queries:
            for i in range(1, page + 1):
                url = 'https://store.steampowered.com/search/?term=' + query + '&page=' + str(i)
                yield scrapy.Request(url, callback=self.parse_keyword_response)

    def parse_keyword_response(self, response):
        products = []
        for i in response.css('a::attr(href)').getall():
            if re.search(r'app', i):
                products.append(i)

        for product in products:
            yield scrapy.Request(product, callback=self.parse)

    def parse(self, response):
        items = SpiderSteamItem()  # cs racing anime
        name = response.xpath('//div[@class = "blockbg"]/a/span[@itemprop = "name"]/text()').extract()
        category = response.xpath('//div[@class = "blockbg"]/a/text()').extract()
        cnt_reviews = response.xpath(
            '//div [@class="summary column"]/span[@class="responsive_hidden"]/text()').extract()
        score = response.xpath(
            '//div [@class="summary column"]/span[@class="nonresponsive_hidden responsive_reviewdesc"]/text()').extract()
        date_release = response.xpath('//div[@class="release_date"]/div[@class="date"]/text()').extract()
        developer = response.xpath('//div[@id="developers_list"]/a/text()').extract()
        tag = response.xpath(
            '//a[@class="app_tag"]/text()').extract()
        price = response.xpath(
            '//div[@class="game_purchase_action"]/div[@class="game_purchase_action_bg"]/div[@class="game_purchase_price price"]/text()').extract()
        platforms = response.xpath('//div[@class="sysreq_tabs"]/div/text()').extract()

        items["name"] = ''.join(name).strip()
        items["category"] = '/'.join(category).strip()
        items["cnt_reviews"] = ''.join(cnt_reviews).strip().replace("\t", "").replace("\n", " ").replace("\r", "")
        items["score"] = ''.join(score).strip().replace("\t", "").replace("\n", "").replace("\r", "")
        items["date_release"] = ''.join(date_release).strip()
        items["developer"] = ''.join(developer).strip()
        items["tag"] = ''.join(tag).strip().replace("\t", "").replace("\n", ", ").replace("\r", "")
        items["price"] = ''.join(price).strip().replace("\t", "").replace("\n", ", ").replace("\r", "")
        items["platforms"] = '/'.join(platforms).strip().replace("\t", "").replace("\n", ", ").replace("\r", "")

        yield items
