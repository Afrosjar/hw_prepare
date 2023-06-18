class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if self.stack:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        item = self.stack.pop()
        return item

    def peek(self):
        item = self.stack[-1]
        return item

    def size(self):
        return len(self.stack)


def main():
    spisok = Stack()  # Создаем экземпляр класса Стэк с пустым списком
    # test_string = '{{[(])]}}'
    test_string = input('Введите тестовую строку для проверки: ')
    flag = True  # Будем считать, что строка сразу сбалансированная
    for i in test_string:
        if i in '[({':  # если элемент проверочной строки является открывающим - добавляем в стэк методом push
            spisok.push(i)
        elif i in '])}':  # Если он закрывающий - и если Стэк не пустой - берем его и сравниваем с верхним элементом стэка
            if not spisok.size():
                flag = False
                break
            item = spisok.pop()

            if item == '(' and i == ')':  # Если закрывающий элемент списка соответствует верхнему из стека - удаляем верхний
                continue  # и идем дальше до конца строки. Если все элементы зеркальны: flag = True
            if item == '[' and i == ']':
                continue
            if item == '{' and i == '}':
                continue
            flag = False  # Если скобка не отзеркалилась - flag = False , прекращаем программу
            break
    if flag and not spisok.size():  # Если flag == True и стэк пустой ( значит у всех скобок нашлась пара), выводим ответ
        print('Сбалансированно')
    else:
        print('Несбалансированно')


if __name__ == '__main__':
    main()
