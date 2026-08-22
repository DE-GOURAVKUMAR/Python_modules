def hanoi(n, source, auxiliary, destination, source_name, aux_name, dest_name):
    # Base Case: If there is only 1 disk left, move it directly
    if n == 1:
        disk = source.pop()
        destination.append(disk)
        print(f"Move disk {disk} from {source_name} to {dest_name}")
        print_status()
        return

    # Step 1: Move top n-1 disks from Source to Auxiliary
    hanoi(n - 1, source, destination, auxiliary, source_name, dest_name, aux_name)

    # Step 2: Move the largest (nth) disk from Source to Destination
    disk = source.pop()
    destination.append(disk)
    print(f"Move disk {disk} from {source_name} to {dest_name}")
    print_status()

    # Step 3: Move the n-1 disks from Auxiliary to Destination
    hanoi(n - 1, auxiliary, source, destination, aux_name, source_name, dest_name)


def print_status():
    """Helper function to visualize the current state of the rods."""
    print(f"  A: {A}")
    print(f"  B: {B}")
    print(f"  C: {C}\n")


# --- Execution Configuration ---
NUMBER_OF_DISKS = 3

# Initialize rods as Python lists (Larger numbers represent larger disks)
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Becomes [3, 2, 1]
B = []
C = []

print("Initial State:")
print_status()

# Start the puzzle
hanoi(NUMBER_OF_DISKS, A, B, C, "A", "B", "C")
