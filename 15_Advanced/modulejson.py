# database'den verileri json ile taşınır. Cihazlar arasında ortak bir veri taşıma objesi
import json

person_string = '{"name": "Ali", "languages": ["python", "C#"]}' # bu bir string json halinde

person_dict = {
    "name": "Ali",
    "languages": ["Python", "C#"]
}

# JSON string to Dict

# result = json.loads(person_string) # Bunu bir dictionary'ye çevirmiş oluyoruz
# result = result['name'] # artık name bilgisine ulaşılabilir.
# result = result['languages']

# with open("C://Users//SefaPc//Desktop//btkPythonL//15_Advanced//person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

# Dict to JSON string

# person_dict = {
#     "name": "Ali",
#     "languages": ["Python", "C#"]
# }

# result = json.dumps(person_dict) # aldığımız bu person dictionary'i çeviriyoruz

# print(type(result)) # stringe başarılı bir şekilde çevrildi
# print(result)


# with open("C://Users//SefaPc//Desktop//btkPythonL//15_Advanced//person.json", "w") as f:
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent= 4, sort_keys= True) # Dictionary'i düzgün bir şekilde yazdırdı okunabilirliği artırdık
print(result)
print(person_dict)