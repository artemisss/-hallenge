from typing import Dict, Optional


def Parser(cond_str: str) -> Dict[str, Optional[str]]:
    result = {
        "type": None,
        "field": None,
        "condition": None,
        "value": None,
    }

    if cond_str:
        result["type"] = cond_str[0]

        # Находим первое вхождение двоеточия, отделяющего тип и поле от условия и значения
        colon_index = cond_str.find(":")
        if colon_index != -1:
            result["field"] = cond_str[1:colon_index]

            # Пытаемся идентифицировать условие и значение после двоеточия
            condition_value_str = cond_str[colon_index + 1:]
            for op in [">=", "<=", "!=", ">", "<", "="]:  # Учитываем все поддерживаемые операторы
                if condition_value_str.startswith(op):
                    result["condition"] = op
                    result["value"] = condition_value_str[len(op):]  # Значение - это все, что после оператора
                    break
            if result["condition"] is None:
                # Если оператор не найден, считаем, что условие равно "=" и все остальное - значение
                result["condition"] = "="
                result["value"] = condition_value_str
        else:
            # Если двоеточие не найдено, все, что после символа типа, является полем
            result["field"] = cond_str[1:]
            result["condition"] = "="

    return result
