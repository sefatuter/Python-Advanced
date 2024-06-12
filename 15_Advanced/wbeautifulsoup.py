html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Web Site</title>
</head>
<body>
    <h1 id="header">
        Python kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    
    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="fred.jpg" alt="">
    
    <a class ="sister" href="https://example1.com/elsie" id="link1">Elsie</a>
    <a class ="sister" href="https://example2.com/elsie" id="link1">Elsie</a>
    <a class ="sister" href="https://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>

"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify() # html dökümanını düzenleme işlemi yapar
result = soup.title # title bilgisini alır
result = soup.head # head kısmının tamamı gelir
result = soup.body # body gelir

result = soup.title.name # etiket ismi gelir
result = soup.title.string

result = soup.h1
result = soup.h2 # iki h2 var sadece ilkini getirir.
result = soup.h2.name
result = soup.h2.string

result = soup.find_all('h2') # bütün h2 etiketlerini getir
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1] # 1. elemanı içinden aldık

result = soup.div
result = soup.find_all('div')[1] # ikinci div gelir.
result = soup.find_all('div')[1].ul.li.string
result = soup.find_all('div')[1].ul.find_all('li')

result = soup.div.findChildren() # bütün alt elemanları getir.
result = soup.div.findNextSibling().findNextSibling() # django gelir 3next'in next'i

result = soup.find_all('a')

for link in result:
    print(link.get('href')) # sadece linkleri aldık
    
