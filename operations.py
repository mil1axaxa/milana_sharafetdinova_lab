from __future__ import annotations
from typing import Annotated

def calculate_gear_ratio(z1: Annotated[float, "число зубьев ведущего"], 
                           z2: Annotated[float, "число зубьев ведомого"]) -> float:
    """Рассчитать передаточное отношение u = z2 / z1[cite: 3]."""
    return z2 / z1

def calculate_output_speed(n1: Annotated[float, "частота входного вала, об/мин"], 
                           u: Annotated[float, "передаточное отношение"]) -> float:
    """Рассчитать частоту вращения ведомого вала n2 = n1 / u[cite: 3]."""
    return n1 / u

def calculate_input_torque(p: Annotated[float, "мощность, кВт"], 
                           n1: Annotated[float, "частота вращения, об/мин"]) -> float:
    """Рассчитать момент на входном валу T1 = 9550 * P / n1[cite: 3]."""
    return (9550 * p) / n1

def calculate_output_torque(t1: Annotated[float, "момент на входе"], 
                            u: Annotated[float, "передаточное отношение"], 
                            eta: Annotated[float, "КПД передачи"]) -> float:
    """Рассчитать момент на выходе редуктора T2 = T1 * u * η[cite: 3]."""
    return t1 * u * eta

def classify_transmission(u: Annotated[float, "передаточное отношение"], 
                          z2: Annotated[float, "число зубьев z2"]) -> str:
    """Классифицировать передачу по правилам Варианта 9[cite: 3]."""
    if u < 2:
        u_type = "малая"
    elif 2 <= u <= 8:
        u_type = "нормальная"
    else:
        u_type = "большая"
        
    return f"u — {u_type}; класс передаточного числа"