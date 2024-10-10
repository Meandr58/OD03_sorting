class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self.items = []

    def is_empty(self):
        """Проверка, пуст ли стек."""
        return not self.items

    def push(self, item):
        """Добавление элемента на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат элемента с вершины стека."""
        return self.items.pop()

    def peek(self):
        """Возврат элемента на вершине стека без его удаления."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# Создание экземпляра стека
stack = Stack()

# Проверка, пуст ли стек
print(stack.is_empty())  # Ожидается True

# Добавление элементов на стек
stack.push(1)
stack.push(2)
stack.push(3)

# Проверка, пуст ли стек
print(stack.is_empty())  # Ожидается False