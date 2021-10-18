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

def main():
    print_menu()
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
            pass
        elif optiune == "5":
            pass
        elif optiune == "x":
            break
        else:
            print("Alegeti alta optiune!")


if __name__ == '__main__':
    main()