def towerBreakers (n, m):
    print((m > 1))
    print (n % 2)
    return 2 - ((m > 1) and (n % 2))

if __name__ == '__main__':
   n1 = 3
   m1 = 1
   print(towerBreakers(n1, m1))