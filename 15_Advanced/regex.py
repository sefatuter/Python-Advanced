import re

result = dir(re)

# re module

str = "Python kursu: Python programlama kursu basladi | 40 saat"

#---> re.findall()

# result = re.findall("Python",str) #string bulma
# result = len(result) # kaç tane bulduğu

#---> re.split()

# result = re.split(" ", str) # boşluk karakteriyle böler

#---> re.sub()

# result = re.sub(" ", "-", str) # boşluk karakterlerini - ile değiştir
# result = re.sub("\s", "-", str) # \s boşluk karakteridir üsttekiyle aynı işlevi görür

#---> re.search()

# result = re.search("Python", str) # ilk istenileni bulur
# result = result.span() # kaçıncı indexte olduğunu söyler
# result = result.start() # başlangıç indeksini gösterir
# result = result.end() # bitiş indeksini gösterir
# result = result.group() # bulduğu ifadeyi gösterir
# result = result.string # aradığı ifadeyi nerede aradığını gösterir

# Regular expression

'''

    [] - Köşeli parantezler arasına yazılan bütün karakterler
        aranır.
        
         [abc] => a     : 1 match
                  ac     : 2 match
                  Python: No matches
        
         [a-e] => [abcde]
         [1-5] => [12345]
         [0-395]=> [12395]
         
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

'''

result = re.findall("[abc]", str) # bütün abc karakterlerini bize verir.
result = re.findall("[sat]", str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[0-5]", str)
result = re.findall("[^abc]", str)

'''
    . - Herhangi bir tek karakteri belirtir

        .. => a     : No match
              ab    : 1 match
              abc   : 1 match
              abcd  : 2 matches
              
'''

result = re.findall("...", str) # her 3'lü gruplar 
result = re.findall("Py..on", str)

'''
    ^ - Belirtilen karakterle başlıyor mu?

        ^a => a     : 1 match
              abc   : 1 match
              bac   : No match
              
'''

result = re.findall("^P", str) # P ile başlayan ifade var mı en başındaki ifadeye bakar 

'''
    $ - Belirtilen karakterle bitiyor mu?

        a$ => a     : 1 match
              lamba : 1 match
              Python: No match
              
'''

result = re.findall("t$", str)
result = re.findall("saat$", str)


'''
    * - Bir karakterin sıfır ya da daha fazla sayıda olmasını
        kontrol eder.

        ma*n => mn    : 1 match
                man   : 1 match
                maaan : 1 match
                main  : No match (a'nın arkasından n gelmiyor.)

'''

result = re.findall("sa*t", str)

'''
    + - Bir karakterin bir ya da daha fazla sayıda olmasını
        kontrol eder.

        ma+n => mn    : No match
                man   : 1 match
                maaan : 1 match
                main  : No match (a'nın arkasından n gelmiyor.)

'''

result = re.findall("sa+t", str) # a karakterinden en az 1 tane olcak

'''
    ? - Bir karakterin sıfır ya da bir kez olmasını
        kontrol eder.

        ma?n => mn    : No match
                man   : 1 match
                maaan : 1 match
                main  : No match (a'nın arkasından n gelmiyor.)

'''

result = re.findall("sa?t", str) # a iki kere tekrarladığı için olmaz

'''
    {} - Karakter sayısını kontrol eder.

        al{2}       => a karakterinin arkasına 1 karakteri 2 kez tekrarlamalı.
        al{2,3}     => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı
        [0-9]{2-4}  => en az 2 en çok 4 basamaklı sayılar.
        
'''

result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str) # iki basamaklı rakam arıyoruz 0 dan 9 a

'''
    |  - Alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        
        a|b => a ya da b 

        cde     => No match
        ade     => 1 match
        acdbea  => 3 match
        
'''

result = re.findall("a|b", str) # a ya da b str'nin içinde kaç tane varsa gösterir.

'''
    ()  - Gruplamak için kullanılır.
        
        (a|b|c)xz   => a,b,c karakterlerinin birinin arkasından xz gelmelidir.
        
'''


'''
    \  - Özel karakterleri aramamızı sağlar.
        
        \$a => $ karakterinin arkasına a karakterini arar. Yani
               $ regular exp. engine tarafından yorumlanamaz.
            
    \A - Belirtilen karakter string in başında mı?
        \Athe => the string in başında mı
    
    \Z - Belirtilen karakter string in sonunda mı?
        the\Z => the string in sonunda mı

    \b - Belirtilen karakter kelimenin başında ya da sonunda mı?
        \bthe => the kelimenin başında mı?
        the\b => the kelimenin sonunda mı?
    
    \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi?
        \Bthe => the kelimenin başında değil mi?
        the\B => the kelimenin sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc34
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 1ab44_50
        
    \s - Boşluk karakterlerini arar.
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w 'nin tam tersi.
            
'''
print(result)