def tower_of_hanoi(n, source, target, aux):
    a = len(source) - 1
    if n == 1:
        target.append(source[-1])
        source.pop()
        print_status()
        return 
    
    # Move n-1 disks from source to aux using target as auxiliary
    tower_of_hanoi(n - 1, source, aux, target)
    
    # Move the nth disk from source to target
    
    target.append(source[-1])
    source.pop()
   # print(f"{source}{target}{aux}")
    print_status()
    
    # Move n-1 disks from aux to target using source as auxiliary
    tower_of_hanoi(n - 1, aux, target, source)

def print_status():
    print(f"{poll_1}{poll_2}{poll_3}")
    
# Example usage
n = 5
poll_1 = [i for i in range(n, 0, -1)]
poll_2 = []
poll_3 = []

tower_of_hanoi(n, poll_1, poll_3, poll_2)