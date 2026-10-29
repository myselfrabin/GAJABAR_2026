a = 1
p = 29


def mod(a,p):

     for a in range(1,p):
         value = (a * a ) % p
         if value == 18:
             return True

if __name__=="__main__":
     print('We are doing our work')
     result = mod(a,p)
     if result:
         print('This is quadratic residue')
     else:
         print("This is not quardaric residue")

