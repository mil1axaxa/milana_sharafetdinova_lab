from __future__ import annotations
from validation import input_number

def show_menu() -> None:
    """Вывести меню выбора типа передачи для Варианта 9[cite: 3]."""
    print("\n--- Меню: 9. Передаточное отношение и момент на выходе редуктора ---")
    print("1 — цилиндрическая передача (η = 0.97)")
    print("2 — коническая передача (η = 0.95)")
    print("3 — червячная передача (η = 0.80)")
    print("0 — выход")

def select_mode() -> float:
    """Использует match-case для маршрутизации. Возвращает КПД или код выхода."""
    while True:
        show_menu()
        choice = input_number("Введите номер режима (от 0 до 3): ", 0, 3)
        
        match int(choice):
            case 1:
                return 0.97
            case 2:
                return 0.95
            case 3:
                return 0.80
            case 0:
                return 0.0
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")