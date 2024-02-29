#29/02/2024
#Author Data Wizard

import random
def sontop(x=10):
  attempt = 0
  tasodifiy_son = random.randint(1,x)
  print(f"Men 1 dan {x} gacha son o'yladim, topa olasizmi?")

  while True:
    attempt +=1
    taxmin = int(input('>>'))
    if taxmin < tasodifiy_son:
      print("Xato men o'ylagan son bundan kattaroq, yana urinib ko'ring\n")
    elif taxmin > tasodifiy_son:
      print("Xato men o'ylagan son bundan kichikroq, yana urinib ko'ring\n")
    else:
      break

  print(f"Tabriklayman!, {attempt} tahmin bilan Topdingiz")

def sontop_pc(x=10):
    print(f"1 dan 10 gacha bo'lgan son o'ylang, men topaman!  Boshladim...")
    min = 0
    max = 10
    attempt = 0
    while True:
     attempt +=1
     if max != min:
        random_son = random.randint(min,max)
     else:
        taxmin = min
        javob = input(f"Siz {taxmin} sonini o'yladingizaa??  (T) - to'g'ri, bundan kattaroq - (+), bundan kichikroq - (-)\n".upper())
        if javob == '-':
          max = taxmin - 1
        elif javob == '+':
          min = taxmin +1
        else:
          break
        print(f"Men {attempt} da tahmin bilan, Topdim!")


def play(x=10):
    while True:
        attempt_user = sontop(x)
        attempt_pc = sontop_pc(x)
        if attempt_user < attempt_pc:
            print(f"Men {sontop_pc(x)} ta , siz esa {sontop(x)} tahmin bilan topdingiz, Siz G'olibsiz!")
        elif attempt_user > attempt_pc:
            print(f"Siz {sontop(x)} ta, men esa {sontop_pc(x)} ta tahmin bilan topdim, Men G'olibman!")
        else:
            break

        print(f"Ikkimiz ham {attempt_user} ta tahmin bilan topdik, Durrang!")


print(sontop())
print(sontop_pc())
    
