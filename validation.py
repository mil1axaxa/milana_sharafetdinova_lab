from __future__ import annotations
from constans import Z1_MIN, Z1_MAX, Z2_MIN, Z2_MAX, P_MIN, P_MAX, N1_MIN, N1_MAX
from logger import log_error

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """Проверка попадания value в [low, high] через if-elif-else."""
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""

def input_number(prompt: str, low: float, high: float) -> float:
    """Циклически запрашивает число, пока не будет корректного."""
    while True:
        try:
            raw = input(prompt).strip()
            value = float(raw)
        except ValueError as e:
            msg = f"Ошибка: введено не число ('{raw}'). {e}"
            print(msg)
            log_error(msg)
            continue
        
        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        
        print(msg + " Повторите ввод.")
        log_error(msg)
