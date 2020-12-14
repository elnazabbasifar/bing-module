from bing import BingBackground as bb
"""
get_image_url() has an optional arg:
0: just download the url
1: download and set it as a background
"""
print(bb().get_image_url())
print(bb(2).get_image_url(1)) 
print(bb(2).get_list_of_urls(1,4))
