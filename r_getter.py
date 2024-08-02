import json
import requests
import urllib.parse

url = 'https://www.facebook.com/api/graphql/'



def make_request(headers, av):
    r = requests.post(url, headers=headers, params=av)
    print(r.status_code, len(r.text))
    return r.text
    # print(len(r.text))
# r = requests.post(url, headers=headers, params=av)
# # r = requests.post('https://www.facebook.com/', headers=h)
# print(r.status_code, r.text)
# print(len(r.text))



# # av = urllib.parse.urlencode(av)
# # av = urllib.parse.parse_qs(av)
# # av["variables"] = urllib.parse.parse_qs(av["variables"])
# # av["variables"] = urllib.parse.urlencode(av["variables"])
# # av = urllib.parse.urlencode(av)

# print("av1")
# print(type(av))
# # print(av)
# # print(av["variables"])
# print(type(av["variables"][0]))
# # av["variables"] = convert_to_correct(av["variables"])
# # print(convert_to_correct(av["variables"]))
# print(av["variables"])
# print()

# # av["variables"] = urllib.parse.parse_qs(av["variables"])
# # av["variables"] = urllib.parse.urlencode(av["variables"])
# # print(av["variables"])
# # print(av)
# # print(type(av["variables"]))
# # print("av1")
# # print(urllib.parse.urlencode(av))
# # av = urllib.parse.urlencode(av)
# # av = urllib.parse.parse_qs(av)
# print(av)
# # print(av["variables"])
# # print("\n\n\n\n\n")
# # av = 'av=100077590856462&__aaid=0&__user=100077590856462&__a=1&__req=fz&__hs=19935.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1015287630&__s=ujw6yn%3A1mnem6%3Ae8n240&__hsi=7397835976657211299&__dyn=7AzHK4HwBgDx-5Q1hyoyEqxd4Ag5S3G2O5U4e2C3-ubyQdwSAx-bwyzE2qwJyEiwsobo5a58e8hw8u250n82nwb-q7oc81xoszU887m2210wEwgo9oO0wE7u12wOx62G5Usw9m1cwLwBgK7o8o4u2O0B84G1hx-3m1mzXw8W58jwGzEjxq1jxS6Fobrwh8lwUwOzEjUlDw-wSU8o4qum7-2K1yw9qm2CVEbUGdG0HE88cA0z8c84p1e4UK2K364UrwFgbU5-269wkopg6C13whEeE4WVU-4EdrxG1fBG2-2K2G&__csr=gxM9In0yMSIQnsnd4gDd9156hk-AwzbPOH7hQO5YpsR89ib4isjaznmT9j9cDhTQGmIOuBQQKsBdeimKQVAHABbOlRFdaQHht5FbBKFFUOXZvGSiBQqVeRXy9raGpkHFuVaHF7BDA-SuiHGLK-qAdhpU-XG8rAh9pFF4luFaZ4UObAxm9iye4WGBgC8mp1arUnzVELK9KdXV8mxmm9yGG78hxGuQqaBBBKrBAwGDyt2pbGE8UHx-FFEC2e8AxKVvxmcwHwMABm58-aAwAwlFoG2aii5oTAxy7oc8Cm8hu9xe7EuwMy8K9KAcALK6oK4KeG1nx22ScxW4Ujx2i5pEjwJy-q9zpK5VVZ6gmwmFogyE9UnwDwJxC0nm16w8WdwhU4i2K3Sm0X8d83bzU5Tw8K0zUgwdq2rwmU9o6a2W26RK-m3e0tR4w2CE0KG0cBw3nocGw4Ig1W-E0zN09JvU5eaw3Yo5F09i0hS7A01SSG06y6m8mNU0f4ry8Gq0nK2Cq0l60v503485u0hi0y81t8W3-0fNDw67o0rEw2n8S04nU0Wu0i-E618wC028-0bEhFU6m0ejxswSdG02C609ohFU0wJoaE1vem096wAwBga85y0bwy82bwq87CUdU129U7C4EkS&__comet_req=15&fb_dtsg=NAcMO_qE3LRcBgwRfDNW-5yE7U9AULvDrRBWC_IoNLY1PuSyWITFQ-Q%3A23%3A1715015853&jazoest=25227&lsd=r3aU0PzENift-O_6ForT6-&__spin_r=1015287630&__spin_b=trunk&__spin_t=1722442912&qpl_active_flow_ids=521482763&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=CometFocusedStoryViewUFIQuery&variables=%7B%22feedbackID%22%3A%22ZmVlZGJhY2s6MjM5MDc5NzQ2MTI2MzUzMQ%3D%3D%22%2C%22feedbackSource%22%3A110%2C%22feedLocation%22%3A%22DEDICATED_COMMENTING_SURFACE%22%2C%22scale%22%3A1%2C%22storyID%22%3A%22UzpfSUZTOjE6LTE1MzQzODE3Mzc5MTU1NDQ4NzI6ZUp3VCs3dDErN0ZIWDY4LytzU29LU04yN2RLUmFYZG43ZWNRNVJPYk5Qdm16MGQ3ZE1YMk5lOTh4U04yYStPdFZ6elNqRzRyNU5VMFpVUmVzS2d4bUlJbHpCakVHTktnU2xjenVWMFJaN3JEOU9MUS93L0hqOHhrbFdiMG1OTEF4RlJVQ2pkV21vR0JRZHd4MEs5SWdZR0JRVlZJbXRGTkNpWmxobkJIS29Nb2k0NDBZeU5mWm5GOGNXcEpmR1plZkZwcWFncWpOQU4yeU1EakpjWVFJeVRFd0pCa3lzQUFBRWFLVGI0PQ%3D%3D%22%2C%22__relay_internal__pv__CometUFIShareActionMigrationrelayprovider%22%3Atrue%2C%22__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=7411648862272565'
# print("av2")
# # av = json.loads(av)
# # av = urllib.parse.parse_qs(av)
# print(type(av))
# # print(av["variables"])
# # print(json.loads(av["variables"][0]))
# # print(len(av["variables"]))
# print(av)
# # print(type(av["variables"][0]))
# # print(av["variables"][0])

# # av = json.dumps(av)

# # variables = '{"RELAY_INCREMENTAL_DELIVERY":true,'+\
# #     '"count":1,'+\
# #     '"cursor":"FQQVAhsCXAIVABhcTVRjeU1USXdNemt3TkRveE56SXhNakF6T1RBME9qRTZNalF3TWpneU1qWTFNelV4TXpVek1qUXlNVG93T2kweE5qSXpOakEwT0RNNE56QTROemcwTWpjNU9nPT0ABhUEGAdwMHxNVG89ABsCVQICCgQVAAA=",'+\
# #     '"feedLocation":"NEWSFEED",'+\
# #     '"feedStyle":"DEFAULT",'+\
# #     '"focusCommentID":null,'+\
# #     '"orderby":["TOP_STORIES"],'+\
# #     '"privacySelectorRenderLocation":"COMET_STREAM",'+\
# #     '"refreshMode":"COLD_START",'+\
# #     '"renderLocation":"homepage_stream",'+\
# #     '"scale":1,'+\
# #     '"__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":false}'

# # variables = urllib.parse.parse_qs(variables)
# # print(variables)
    

# # print(json.dumps(av, indent=4))

# # av = urllib.parse.urlencode(av)
# # headers = urllib.parse.urlencode(headers)
# # print(av)
# r = requests.post(url, headers=headers, params=av)
# print(r.status_code, r.text)
# print(len(r.text))



# # variables=%7B%22feedbackID%22%3A%22ZmVlZGJhY2s6MjM5MDc5NzQ2MTI2MzUzMQ%3D%3D%22%2C%22feedbackSource%22%3A110%2C%22feedLocation%22%3A%22DEDICATED_COMMENTING_SURFACE%22%2C%22scale%22%3A1%2C%22storyID%22%3A%22UzpfSUZTOjE6LTE1MzQzODE3Mzc5MTU1NDQ4NzI6ZUp3VCs3dDErN0ZIWDY4LytzU29LU04yN2RLUmFYZG43ZWNRNVJPYk5Qdm16MGQ3ZE1YMk5lOTh4U04yYStPdFZ6elNqRzRyNU5VMFpVUmVzS2d4bUlJbHpCakVHTktnU2xjenVWMFJaN3JEOU9MUS93L0hqOHhrbFdiMG1OTEF4RlJVQ2pkV21vR0JRZHd4MEs5SWdZR0JRVlZJbXRGTkNpWmxobkJIS29Nb2k0NDBZeU5mWm5GOGNXcEpmR1plZkZwcWFncWpOQU4yeU1EakpjWVFJeVRFd0pCa3lzQUFBRWFLVGI0PQ%3D%3D%22%2C%22__relay_internal__pv__CometUFIShareActionMigrationrelayprovider%22%3A%22true%22%2C%22__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider%22%3A%22true%22%2C%22__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider%22%3A%22false%22%7D&server_timestamps=true&doc_id=7411648862272565

# # variables=%7B%22feedbackID%22%3A%22ZmVlZGJhY2s6MjM5MDc5NzQ2MTI2MzUzMQ%3D%3D%22%2C%22feedbackSource%22%3A110%2C%22feedLocation%22%3A%22DEDICATED_COMMENTING_SURFACE%22%2C%22scale%22%3A1%2C%22storyID%22%3A%22UzpfSUZTOjE6LTE1MzQzODE3Mzc5MTU1NDQ4NzI6ZUp3VCs3dDErN0ZIWDY4LytzU29LU04yN2RLUmFYZG43ZWNRNVJPYk5Qdm16MGQ3ZE1YMk5lOTh4U04yYStPdFZ6elNqRzRyNU5VMFpVUmVzS2d4bUlJbHpCakVHTktnU2xjenVWMFJaN3JEOU9MUS93L0hqOHhrbFdiMG1OTEF4RlJVQ2pkV21vR0JRZHd4MEs5SWdZR0JRVlZJbXRGTkNpWmxobkJIS29Nb2k0NDBZeU5mWm5GOGNXcEpmR1plZkZwcWFncWpOQU4yeU1EakpjWVFJeVRFd0pCa3lzQUFBRWFLVGI0PQ%3D%3D%22%2C%22__relay_internal__pv__CometUFIShareActionMigrationrelayprovider%22%3Atrue%2C%22__relay_internal__pv__IncludeCommentWithAttachmentrelayprovider%22%3Atrue%2C%22__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider%22%3Afalse%7D&server_timestamps=true&doc_id=7411648862272565
