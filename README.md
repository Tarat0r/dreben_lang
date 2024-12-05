## Описание

Интерпретатор и компилатор в триадресен код на езика за програмиране dreben-lang. dreben-lang е прост език, предназначен за учебни цели, който демонстрира основни концепции като променливи, аритметични операции, условни конструкции и цикли.

Интерпретаторът използва ANTLR4 за генериране на лексер, парсер и визитор, и е написан на Python3.

## Поддръжка на операциите в dreben-lang
---

### **Аритметични операции**

| Оператор       | Описание                   | Пример               | Резултат |
|----------------|----------------------------|----------------------|----------|
| **`плюс`**     | Събиране                  | `2 плюс 3`           | `5`      |
| **`минус`**    | Изваждане                 | `5 минус 2`          | `3`      |
| **`по`**       | Умножение                 | `3 по 4`             | `12`     |
| **`делено на`**| Деление (цялочислено)     | `10 делено на 3`     | `3`      |

### Оператори за сравнение

| Оператор                    | Описание                     | Пример                   | Резултат |
|-----------------------------|------------------------------|--------------------------|----------|
| **`е равно на`**            | Проверка за равенство        | `5 е равно на 5`         | `True`   |
| **`НЕ е равно на`**         | Проверка за неравенство      | `5 НЕ е равно на 3`      | `True`   |
| **`е по-голямо от`**        | Проверка за по-голяма стойност| `10 е по-голямо от 5`    | `True`   |
| **`е по-малко от`**         | Проверка за по-малка стойност| `5 е по-малко от 10`     | `True`   |
| **`е по-голямо или равно от`** | Проверка за ≥               | `5 е по-голямо или равно от 5` | `True`   |
| **`е по-малко или равно от`** | Проверка за ≤               | `3 е по-малко или равно от 5` | `True`   |


### Комбиниране на изрази
```
Променлива x равна (5 плюс 10);
Променлива y равна ((x минус 5) по 2);
Покажи y;  // Резултат: 20
```

### Условни оператори
```
Ако „x е по-голямо от 5“ {
    Покажи x;
} Иначе {
    Покажи 5;
}
```

### Цикли
```
Променлива x равна 0;
Докато x „е по-малко от“ 5 {
    Покажи x;
    x равна x плюс 1;
}
```
