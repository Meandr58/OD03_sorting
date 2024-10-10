class Queue:
    def __init__(self):  # Исправлено __init__
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # Используем append для добавления в конец

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Удаляем из начала списка
        else:
            raise IndexError("Очередь пуста, нечего удалять.")

    def size(self):
        return len(self.items)

# Пример использования
queue = Queue()

print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())