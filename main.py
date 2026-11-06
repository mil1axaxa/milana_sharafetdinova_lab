from __future__ import annotations
from menu import select_mode
from validation import input_number
from operations import (
    calculate_gear_ratio,
    calculate_output_speed,
    calculate_input_torque,
    calculate_output_torque,
    classify_transmission
)
from constans import Z1_MIN, Z1_MAX, Z2_MIN, Z2_MAX, P_MIN, P_MAX, N1_MIN, N1_MAX

def main() -> None:
    is_running = True
    
    while is_running:
        eta = select_mode()
        
        if eta == 0.0:
            print("Выход из программы. До свидания!")
            is_running = False
        else:
            print(f"\nВыбран КПД передачи: {eta}")
            
            z1 = input_number(f"Введите число зубьев ведущего z1 ({Z1_MIN}..{Z1_MAX}): ", Z1_MIN, Z1_MAX)
            
            while True:
                z2 = input_number(f"Введите число зубьев ведомого z2 ({Z2_MIN}..{Z2_MAX}), причем z2 > z1: ", Z2_MIN, Z2_MAX)
                if z2 > z1:
                    break
                print(f"Ошибка: число зубьев ведомого z2 ({z2}) должно быть больше числа зубьев ведущего z1 ({z1}). Повторите ввод.")
            
            p = input_number(f"Введите мощность на входе p, кВт ({P_MIN}..{P_MAX}): ", P_MIN, P_MAX)
            n1 = input_number(f"Введите частоту вращения входного вала n1, об/мин ({N1_MIN}..{N1_MAX}): ", N1_MIN, N1_MAX)
            
            u = calculate_gear_ratio(z1, z2)
            n2 = calculate_output_speed(n1, u)
            t1 = calculate_input_torque(p, n1)
            t2 = calculate_output_torque(t1, u, eta)
            classification = classify_transmission(u, z2)
            
            print("\n" + "="*40)
            print(" РЕЗУЛЬТАТЫ РАСЧЕТА (ВАРИАНТ 9)")
            print("="*40)
            print(f"Передаточное отношение (u): {u:.2f}")
            print(f"Классификация передачи: {classification}")
            print(f"Частота вращения ведомого вала (n2): {n2:.2f} об/мин")
            print(f"Крутящий момент на входном валу (T1): {t1:.2f} Н*м")
            print(f"Крутящий момент на выходном валу (T2): {t2:.2f} Н*м")
            print("="*40 + "\n")

if __name__ == "__main__":
    main()