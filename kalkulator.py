def dodaj get_help():
    print('To jest prosty program kalkulatora. Wprowadü dwie liczby i zatwierdü enterem.')
def dodaj(a,b):
    wynik = a+b
    return wynik
    
get_help() 
zm1 = int(input())
zm2 = int(input())
print(dodaj(zm1, zm2))

