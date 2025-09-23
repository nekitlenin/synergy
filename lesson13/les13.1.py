import random

def create_matrix(rows, cols, min_val=-200, max_val=200):
    """Создает матрицу заданного размера со случайными значениями"""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def print_matrix(matrix, name="Матрица"):
    """Выводит матрицу в читаемом формате"""
    print(f"{name}:")
    for row in matrix:
        print(row)
    print()

def add_matrices(matrix1, matrix2):
    """Складывает две матрицы одинаковой размерности"""
    # Проверяем, что матрицы одинакового размера
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Основная программа
def main():
    # Размерность матриц
    rows = 10
    cols = 10
    
    print("Генерация матриц 10x10:")
    print("=" * 50)
    
    # Создаем первую матрицу
    matrix_1 = create_matrix(rows, cols)
    print_matrix(matrix_1, "matrix_1")
    
    # Создаем вторую матрицу
    matrix_2 = create_matrix(rows, cols)
    print_matrix(matrix_2, "matrix_2")
    
    # Складываем матрицы
    matrix_3 = add_matrices(matrix_1, matrix_2)
    print_matrix(matrix_3, "matrix_3 (matrix_1 + matrix_2)")
    
    # Демонстрация с другими размерами
    print("\n" + "=" * 50)
    print("Демонстрация с матрицами 4x3:")
    print("=" * 50)
    
    # Матрицы 4x3
    small_matrix_1 = create_matrix(4, 3)
    small_matrix_2 = create_matrix(4, 3)
    
    print_matrix(small_matrix_1, "small_matrix_1")
    print_matrix(small_matrix_2, "small_matrix_2")
    
    small_matrix_3 = add_matrices(small_matrix_1, small_matrix_2)
    print_matrix(small_matrix_3, "small_matrix_3 (сумма)")

# Проверка на примере из задания
def test_with_given_matrices():
    """Тестирование на примерах из задания"""
    print("Проверка на примерах из задания:")
    print("=" * 50)
    
    matrix_1 = [
        [0, -2, -1, -6, -6, 0, -9, -8, -30, -9],
        [5, 12, 4, -16, -4, -9, -16, -15, 1, -26],
        [13, 39, 14, 23, -4, 40, 32, 6, -8, 23],
        [13, -8, 34, 49, 30, 18, 47, 11, -24, 11],
        [21, 73, 71, 61, -1, 79, -34, 22, 69, 67],
        [75, 25, 25, 39, 100, -12, -21, 81, -10, 87],
        [81, 63, 102, 104, 53, -44, 71, -36, -36, -9],
        [7, 98, 26, -3, 128, 94, 18, -26, 14, 21],
        [65, 128, 80, 124, 27, -32, 73, 59, 19, 34],
        [43, 111, 38, 149, 5, 112, 79, 53, 15, 92]
    ]
    
    matrix_2 = [
        [0, 4, 6, 11, 15, 6, 9, 26, 15, 21],
        [-5, 4, -15, -9, -4, 2, -8, 19, -4, -1],
        [-2, -39, -19, 14, 22, 5, -34, 15, 16, -9],
        [-22, -52, 11, -11, -3, 16, -11, -6, -32, -2],
        [-61, -47, -5, -58, 16, -13, 28, -36, -64, 2],
        [-29, 23, 19, 2, -14, -87, 7, -88, 39, 7],
        [-6, 18, -97, 26, -64, 0, -72, -34, -68, -92],
        [-120, -117, -72, -129, -139, 16, -61, 36, -137, -29],
        [-112, -83, 7, -119, -132, -129, -143, -154, -23, -34],
        [32, -67, -75, -92, 15, -163, 18, 31, -162, -16]
    ]
    
    matrix_3 = add_matrices(matrix_1, matrix_2)
    
    print_matrix(matrix_1, "matrix_1 (из задания)")
    print_matrix(matrix_2, "matrix_2 (из задания)")
    print_matrix(matrix_3, "matrix_3 (результат сложения)")
    
    # Проверка правильности сложения
    expected_result = [
        [0, 2, 5, 5, 9, 6, 0, 18, -15, 12],
        [0, 16, -11, -25, -8, -7, -24, 4, -3, -27],
        [11, 0, -5, 37, 18, 45, -2, 21, 8, 14],
        [-9, -60, 45, 38, 27, 34, 36, 5, -56, 9],
        [-40, 26, 66, 3, 15, 66, -6, -14, 5, 69],
        [46, 48, 44, 41, 86, -99, -14, -7, 29, 94],
        [75, 81, 5, 130, -11, -44, -1, -70, -104, -101],
        [-113, -19, -46, -132, -11, 110, -43, 10, -123, -8],
        [-47, 45, 87, 5, -105, -161, -70, -95, -4, 0],
        [75, 44, -37, 57, 20, -51, 97, 84, -147, 76]
    ]
    
    # Проверяем корректность
    if matrix_3 == expected_result:
        print("✅ Сложение выполнено правильно!")
    else:
        print("❌ Ошибка в сложении матриц")

# Интерактивный режим
def interactive_mode():
    """Интерактивный режим для работы с матрицами произвольного размера"""
    print("\n" + "=" * 50)
    print("Интерактивный режим:")
    print("=" * 50)
    
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        
        if rows <= 0 or cols <= 0:
            print("Размеры матриц должны быть положительными числами!")
            return
        
        print(f"\nСоздание матриц размером {rows}x{cols}:")
        
        # Создаем матрицы
        mat1 = create_matrix(rows, cols)
        mat2 = create_matrix(rows, cols)
        
        print_matrix(mat1, "Матрица 1")
        print_matrix(mat2, "Матрица 2")
        
        # Складываем
        result = add_matrices(mat1, mat2)
        print_matrix(result, "Результат сложения")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск программы
if __name__ == "__main__":
    # Тестирование на примерах из задания
    test_with_given_matrices()
    
    # Основная демонстрация
    main()
    
    # Интерактивный режим
    interactive_mode()