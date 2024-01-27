import queue
from collections import deque
def task_1():

    #Створити чергу заявок
    q = queue.Queue()

    """Функція generate_request():
    Створити нову заявку
    Додати заявку до черги"""

    def generate_request(request_id):
        
        q.put(request_id)
        print(f"Заявка {request_id} додана до черги.")

    """Функція process_request():
        Якщо черга не пуста:
            Видалити заявку з черги
            Обробити заявку
        Інакше:
            Вивести повідомлення, що черга пуста"""

    def process_request():
        if not q.empty():
            request = q.get()
            print(f"Заявка {request} оброблена.")
        else:
            print("Черга пуста.")

    """Головний цикл програми:
        Поки користувач не вийде з програми:
            Виконати generate_request() для створення нових заявок
            Виконати process_request() для обробки заявок"""

    def main():
        request_id = 1

        while True:
            user_input = input("Натисніть Enter, щоб продовжити або 'q' для виходу: ")
            if user_input.lower() == 'q':
                break

            generate_request(request_id)
            request_id += 1

            process_request()

    if __name__ == "__main__":
        main()

def task_2():
    
    def is_palindrome(s):
        cleaned_string = ''.join(c.lower() for c in s if c.isalnum())
        char_deque = deque(cleaned_string)

        while len(char_deque) > 1:
            if char_deque.popleft() != char_deque.pop():
                return False
        return True
    print(is_palindrome(input("Enter string: ")))

#Run tasks:
    
task_1()
#task_2()