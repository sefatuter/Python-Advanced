with open("newfile.txt", "r", encoding='utf-8') as file:
    content = file.read(10)
    print(content)
    print(file.tell()) # tell() fonksiyonu cursor'un konumunu verir. kaçıncı karakterde ise

    file.seek(10) #  seek fonksyionu, cursor nereye gitsin?

    content2 = file.read(10)
    print(content2)

# with ile artık oluşturmuş olduğumuz kod bloğunun sonuna geldiğimiz andan itibaren dosya 
# kendi kendine kapanacak

