#Exercise 1:
import json

def sum_tuples():
    try:
        tuple1 = tuple(map(int, input("Enter tuple 1 (comma-separated): ").split(',')))
        tuple2 = tuple(map(int, input("Enter tuple 2 (comma-separated): ").split(',')))

        if len(tuple1) != len(tuple2):
            print("Error: Tuples must be the same length to sum.")
            return

        tuple_sum = tuple(a + b for a, b in zip(tuple1, tuple2))
        print(f"Sum of tuples: {tuple_sum}")
    except ValueError:
        print("Error: Invalid input. Please enter only integers separated by commas.")

def export_json(data, filename):
    """Exports data to a JSON file using the built-in json module."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data exported to {filename}")
    except Exception as e:
        print(f"Error exporting data: {e}")

def import_json(filename):
    """Imports data from a JSON file using the built-in json module."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print("Data imported from JSON:")
        print(data)
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found. Please export data first.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {filename}.")
    except Exception as e:
        print(f"Error importing data: {e}")

def main():
    while True:
        print("\n1. Sum Tuples")
        print("2. Export JSON")
        print("3. Import JSON")
        print("4. Exit")
        
        choice = input("Enter a choice: ")
        
        if choice == '1':
            sum_tuples()
        elif choice == '2':
            data = {
                'name': 'Fatima',
                'age': 22,
                'nationality': 'Lebanese'
            }
            filename = input("Enter the filename to export to JSON (e.g., data.json): ")
            export_json(data, filename)
        elif choice == '3':
            filename = input("Enter the filename to import from JSON (e.g., data.json): ")
            import_json(filename)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

#Exercise 2:
# a) 1/6N+800N3+24
# O(N^3)
# b) 1/6N3
# O(N^3)
# c) 1/6N!+200N4
# O(N!)
# d) NlogN+1000
# O(NlogN)
# e) logN+N
# O(N)
# f) 1/2N(N-1)
# O(N^2)
# g) N2+220NlogN2+3N+9000
# O(N^2)
# h) N!+3N+2N+N3+N2
# O(N!)
