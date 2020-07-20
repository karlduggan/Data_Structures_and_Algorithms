
# Recursive Python function to solve tower of hanoi 
  
#Tower Of Hanoi


def hanoi(n, sorc, dest, aux):
    if n == 1:
        print(f'Move disk {n} from {sorc} to {dest}')
        return 
    else:
        hanoi(n-1, sorc, aux, dest)
        print(f'Move disk {n} from {sorc} to {dest}')
        hanoi(n-1, aux, dest, sorc)

hanoi(3,'a','c','b')