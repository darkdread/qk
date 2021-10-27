from urllib.parse import unquote

link = "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/198949437_581651252797715_4182852608010071755_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com%5Cu0026_nc_cat=111%5Cu0026_nc_ohc=Teae-l5kuEoAX9o_flP%5Cu0026edm=APU89FABAAAA%5Cu0026ccb=7-4%5Cu0026oh=11109d4b6ec3bac6dea2a9917130e8b4%5Cu0026oe=616F9D7D%5Cu0026_nc_sid=86f79a"

url: str = unquote(link, 'utf-8')

print(bytes(url, 'utf-8').decode('unicode_escape'))
print("https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/198949437_581651252797715_4182852608010071755_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com\u0026_nc_cat=111\u0026_nc_ohc=Teae-l5kuEoAX9o_flP\u0026edm=APU89FABAAAA\u0026ccb=7-4\u0026oh=11109d4b6ec3bac6dea2a9917130e8b4\u0026oe=616F9D7D\u0026_nc_sid=86f79a")

# url2 = "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/198949437_581651252797715_4182852608010071755_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com\u0026_nc_cat=111\u0026_nc_ohc=Teae-l5kuEoAX9o_flP\u0026edm=APU89FABAAAA\u0026ccb=7-4\u0026oh=11109d4b6ec3bac6dea2a9917130e8b4\u0026oe=616F9D7D\u0026_nc_sid=86f79a".encode().decode()
# print(str(url2))
