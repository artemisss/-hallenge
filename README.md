У нас есть набор строк которые в себе содержат логику построения фильтрации для дальнейшей передачи в storage

# Пример строк:

```
@id:22
@id:>30
@id:>=100
@id:!=100

#office
#office:1010
#office:>101010
#office:>=101011
#office:!=101010
```

# Спец. символы

```
@ - смивол начала условия для **поля**
# - символ начала условия для **тега**
: - разделитель поля/тега и условия
> < >= <= != - операторы сравнения/условия
Если опартора сравнения нет это эквиваентно **=**
```

# Задача:

Распарсить строки и собрать из них структуру данных

```go
type Cond struct {
	Type string
	Field string
	Condition string
	Value any
}
```

Пример:

```go
var cond Cond = Cond{
	Type: "@",
	Field: "id",
	Condition: "="
	Value: nil
}

var cond1 Cond = Cond{
	Type: "@",
	Field: "id",
	Condition: ">="
	Value: 122
}
```

# Как должен выглядеть результат для GO

Нужно реализовать тело функции `Parse`  , в которой стоит учесть быстродействие и лаконичность кода

```go
type Cond struct {
	Type      string
	Field     string
	Condition string
	Value     any
}

func Parser(condStr string) (*Cond, error) {
	// Realisation code
}
```

Тест для тестирования полученной функции **GO**:
```
package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParser(t *testing.T) {
	assert.New(t)

	testCases := []struct {
		Value    string
		Expected *Cond
	}{
		{
			Value: "@id:22",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: "=",
				Value:     "22",
			},
		},
		{
			Value: "@id:>30",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: ">",
				Value:     "30",
			},
		},
		{
			Value: "@id:>=100",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: ">=",
				Value:     "100",
			},
		},
		{
			Value: "@id:<30",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: "<",
				Value:     "30",
			},
		},
		{
			Value: "@id:<=100",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: "<=",
				Value:     "100",
			},
		},
		{
			Value: "@id:!=100",
			Expected: &Cond{
				Type:      "@",
				Field:     "id",
				Condition: "!=",
				Value:     "100",
			},
		},
		{
			Value: "#office",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: "=",
				Value:     nil,
			},
		},
		{
			Value: "#office:1010",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: "=",
				Value:     "1010",
			},
		},
		{
			Value: "#office:>101010",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: ">",
				Value:     "101010",
			},
		},
		{
			Value: "#office:>=101011",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: ">=",
				Value:     "101011",
			},
		},
		{
			Value: "#office:<101010",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: "<",
				Value:     "101010",
			},
		},
		{
			Value: "#office:<=101011",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: "<=",
				Value:     "101011",
			},
		},
		{
			Value: "#office:!=101010",
			Expected: &Cond{
				Type:      "#",
				Field:     "office",
				Condition: "!=",
				Value:     "101010",
			},
		},
	}

	for _, tc := range testCases {
		actual, err := Parser(tc.Value)
		if !assert.NoError(t, err) {
			continue
		}

		assert.Equal(t, tc.Expected, actual)
	}
}
```
Тест для тестирования полученной функции GO на скорость выполнения:
func BenchmarkParser(b *testing.B) {
	str := "#office:>=101011"

	for i := 0; i < b.N; i++ {
		_, _ = Parser(str)
	}
}
​
Команда запуска
go test -bench=. -benchtime=10000000x -benchmem
​
Ожидаемый ввод:
BenchmarkParser-8       10000000               xxx.x ns/op           xxx B/op          xx allocs/op
PASS
ok      go-scripts/parser       x.xxxs

# Как должен выглядеть результат для PYTHON

Нужно реализовать тело функции `Parse`  , в которой стоит учесть быстродействие и лаконичность кода, так же по возможность избегать использование сторонних пакетов 

```python
from typing import Dict

def Parser(cond_str: str) -> Dict[str, str | None]:
    result = {
        "type": None,
        "field": None,
        "condition": None,
        "value": None,
    }
    
    # body of func

    return result

```

Тест для тестирования полученной функции **PYTHON**:

```
import unittest
import main

test_case_data = [
    {
        "value": "@id:22",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "=",
            "value": "22",
        },
    },
    {
        "value": "@id:>30",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": ">",
            "value": "30",
        },
    },
    {
        "value": "@id:>=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": ">=",
            "value": "100",
        },
    },
    {
        "value": "@id:<30",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "<",
            "value": "30",
        },
    },
    {
        "value": "@id:<=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "<=",
            "value": "100",
        },
    },
    {
        "value": "@id:!=100",
        "expected": {
            "type": "@",
            "field": "id",
            "condition": "!=",
            "value": "100",
        },
    },
    {
        "value": "#office",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "=",
            "value": None,
        },
    },
    {
        "value": "#office:1010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "=",
            "value": "1010",
        },
    },
    {
        "value": "#office:>101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": ">",
            "value": "101010",
        },
    },
    {
        "value": "#office:>=101011",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": ">=",
            "value": "101011",
        },
    },
    {
        "value": "#office:<101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "<",
            "value": "101010",
        },
    },
    {
        "value": "#office:<=101011",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "<=",
            "value": "101011",
        },
    },
    {
        "value": "#office:!=101010",
        "expected": {
            "type": "#",
            "field": "office",
            "condition": "!=",
            "value": "101010",
        },
    },
]


class ParserTestCase(unittest.TestCase):
    def test_parser(self):
        for t in test_case_data:
            result = main.Parser(t['value'])
            self.assertEqual(t['expected'], result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
```

Тест для тестирования полученной функции PYTHON на скорость выполнения:
python -m timeit -n 10000000 -s "import main" -v "main.Parser('#office:>=101011')"
​
Ожидаемый ввод:
raw times: x.xx sec, x.xx sec, x.xx sec, x.xx sec, x.xx sec

10000000 loops, best of 5: xxx nsec per loop







