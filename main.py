def is_prime(num):
    '''
    Determina daca numarul dat este prim
    :param num:
    :return: 1 daca numarul este prim, 0 in caz contrar
    '''
    if num > 1:
        for i in range(2, int(num // 2) + 1):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0

def test_is_prime():
    assert is_prime(2) == 1
    assert is_prime(4) == 0
    assert is_prime(5) == 1
    assert is_prime(17) == 1
    assert is_prime(27) == 0

def remove_prime_from_list(l):
    '''
    Returneaza lista elementelor mai putin cele prime
    :param l:
    :return: o lista cu proprietatea ca elementul nu este prim
    '''
    return [x for x in l if is_prime(x) == 0]

def test_remove_prime_from_list():
    assert remove_prime_from_list([8,17,19,25]) == [8,25]
    assert remove_prime_from_list([10,11,12]) == [10,12]
    assert remove_prime_from_list([13,17,19]) == []

def medie_mai_mica_decat_n(l, n):
    '''
    Functie care compara media aritmetica a elementelor unei liste cu un nr dat n
    :param l:
    :param n:
    :return: mesajul "DA" daca media este mai mare decat n, mesajul "NU" in caz contrar
    '''
    s = 0
    nr_elem = 0
    for x in l:
        s += x
        nr_elem +=1

    ma = s/nr_elem
    if ma > n:
        return "DA"
    else:
        return "NU"

def test_medie_mai_mica_decat_n():
    assert medie_mai_mica_decat_n([10, -3, 25, -1, 3, 25, 18], 10) == "DA"
    assert medie_mai_mica_decat_n([1,2,3,4,5], 2) == "DA"
    assert medie_mai_mica_decat_n([1,2,3,5,6,7], 92) == "NU"

def nr_diviz_proprii(n):
    '''
    Functie care calculeaza numarul de divizorii proprii ai lui n
    :param n:
    :return: returneaza variabila contor in care e stocat numarul de divizori proprii ai lui n
    '''

    cont = 0
    for d in range(2, n//2 + 1):
        if n % d == 0:
            cont +=1

    return cont

def test_nr_diviz_proprii():
    assert nr_diviz_proprii(6) == 2
    assert nr_diviz_proprii(10) == 2
    assert nr_diviz_proprii(12) == 4
    assert nr_diviz_proprii(19) == 0

def adaugare_nr_diviz_proprii(l):
    '''
    Functie care prelucreaza lista data adaugand dupa fiecare element numarul de divizori proprii
    :param l:
    :return: Returneaza o lista noua in care se adauga fiecare element din lista veche urmat de numarul prorpiu de divizori al acestuia
    '''

    lista_noua = []
    for x in l:
        lista_noua.append(x)
        lista_noua.append(nr_diviz_proprii(x))

    return lista_noua


def test_adaugare_nr_diviz_proprii():
    assert adaugare_nr_diviz_proprii([19, 5, 24, 12, 9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]
    assert adaugare_nr_diviz_proprii([5,10,6]) == [5, 0, 10, 2, 6, 2]
    assert adaugare_nr_diviz_proprii([12, 9,9, 14]) == [12, 4, 9 ,1, 9 ,1 ,14, 2]

def nr_aparitii(l, x):
    '''
    Calculeaza numarul de aparitii a lui x in lista l
    :param l: lista
    :param x:
    :return: numarul de aparitii a lui x in l in variabila contor
    '''
    contor = 0
    for i in l:
        if i == x:
            contor +=1

    return contor

def test_nr_aparitii():
    assert nr_aparitii([1,2,3], 2) == 1
    assert nr_aparitii([1,2,2,3,2,4,2], 2) == 4
    assert nr_aparitii([1,2,3,4], 5) == 0

def formare_lista_tuplu(l):
    '''
    Functie care formeaza o lista al carei elemente un tuplu format din elementele dintr-o lista data l, indexarea lor in lista si numarul de aparitii al elementului in lista data
    :param l:
    :return: lista cu elemente tuplu care indeplinesc cerinta data
    '''
    lista_noua = []
    for i in range(len(l)):
        tuplu = (l[i], i, nr_aparitii(l,l[i]))
        lista_noua.append(tuplu)

    return lista_noua

def test_formare_lista_tuplu():
    assert formare_lista_tuplu([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert formare_lista_tuplu([1, 2, 3, 2]) == [(1, 0, 1), (2, 1, 2), (3, 2, 1), (2, 3, 2)]
    assert formare_lista_tuplu([2, 2, 2]) == [(2, 0, 3), (2, 1, 3), (2, 2, 3)]

def print_menu():
    print("1. Citire lista")
    print("2. Afișarea listei după eliminarea numerelor prime din listă")
    print("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
    print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului.")
    print("5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un tuplu în care pe")
    print("prima poziție este numărul, pe a doua poziție va fi indexul elementului din listă, iar pe a treia")
    print("poziție apare numărul de apariții a numărului.")
    print("x. Iesire")

def citire_lista():
    l = []
    n = int(input("Numarul de elemente din lista: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]= ")))

    return l

def all_test():
    test_is_prime()
    test_remove_prime_from_list()
    test_medie_mai_mica_decat_n()
    test_nr_diviz_proprii()
    test_adaugare_nr_diviz_proprii()
    test_nr_aparitii()
    test_formare_lista_tuplu()

def main():

    all_test()
    l = []
    while True:
        print_menu()
        optiune = input("Alegeti optiunea dorita: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(remove_prime_from_list(l))
        elif optiune == "3":
            n = int(input("Alegeti un numar: "))
            print(medie_mai_mica_decat_n(l,n))
        elif optiune == "4":
            print(adaugare_nr_diviz_proprii(l))
        elif optiune == "5":
            print(formare_lista_tuplu(l))
        elif optiune == "x":
            break
        else:
            print("Alegeti alta optiune!")


if __name__ == '__main__':
    main()