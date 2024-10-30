def read_matrix():
    rows = int(input("Введіть кількість рядків матриці: "))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Введіть рядок {i + 1} (елементи через пробіл): ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrix_by_scalar(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]

def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            value = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(value)
        result.append(row)
    return result

def main():
    print("Матриця A:")
    A = read_matrix()
    
    print("Матриця B:")
    B = read_matrix()
    
    while True:
        print("\nОберіть операцію:")
        print("1. Додавання матриць")
        print("2. Віднімання матриць")
        print("3. Множення матриці на число")
        print("4. Множення двох матриць")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            if len(A) == len(B) and len(A[0]) == len(B[0]):
                result = add_matrices(A, B)
                print("Результат (A + B):")
                print_matrix(result)
            else:
                print("Матриці мають різні розміри для додавання.")

        elif choice == '2':
            if len(A) == len(B) and len(A[0]) == len(B[0]):
                result = subtract_matrices(A, B)
                print("Результат (A - B):")
                print_matrix(result)
            else:
                print("Матриці мають різні розміри для віднімання.")

        elif choice == '3':
            scalar = float(input("Введіть число для множення: "))
            result = multiply_matrix_by_scalar(A, scalar)
            print(f"Результат (A * {scalar}):")
            print_matrix(result)

        elif choice == '4':
            if len(A[0]) == len(B):
                result = multiply_matrices(A, B)
                print("Результат (A * B):")
                print_matrix(result)
            else:
                print("Кількість стовпців A повинна дорівнювати кількості рядків B.")

        elif choice == '5':
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")