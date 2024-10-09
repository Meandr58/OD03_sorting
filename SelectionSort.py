def selection_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]

# Пример использования
numbers = [64, -3, 0, -18, 25, 12, 22, 17]
selection_sort(numbers)
print(numbers)
