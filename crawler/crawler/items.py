# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

import string

def clean_strings(input_list):
    combined_string = "".join(input_list)
    cleaned_string = combined_string.replace('\n', ' ')
    cleaned_string = combined_string.replace('\xa0', ' ')
    cleaned_string = cleaned_string.translate(str.maketrans('', '', string.punctuation))
    
    return cleaned_string

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    tag = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    description = scrapy.Field(
        input_processor = MapCompose(remove_tags, clean_strings),
        output_processor = Join()
    )

    pass
