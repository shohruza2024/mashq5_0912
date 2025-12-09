#1-misol
roy = [3, 126, 4.21, 701, 99.9, 1001, 100, 7]
result = list(filter(lambda x: isinstance(x, int) and 100 <= x <= 999, roy))
print(result)

#2-misol
sites = ["google.com", "example.uz", "test.uz", "mail.ru"]
result = list(filter(lambda x: x.endswith(".uz"), sites))
print(result)

#3-misol
sozlar = ["itparkdagi", "dasturbek", "professional", "bolalar", "mayli", "qizlar"]
natija = list(filter(lambda x: len(x) % 2 == 0, sozlar))
print(natija)

#4-misol
sonlar = [105, 50, 14, 701, 2900, 25, 10, 790]
natija = list(filter(lambda x: x % 10 == 0, sonlar))
print(natija)

#5-misol
sonlar = [15, 5, 14, 70, 29, 25, 35, 7, 140]
natija = list(filter(lambda x: x % 5 == 0 and x % 7 == 0, sonlar))
print(natija)
