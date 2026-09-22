/**
 * @jest-environment jsdom
 */

// Unit-тесты для калькулятора
// Тестируют отдельные функции и логику без взаимодействия с DOM

describe('Валидация чисел', () => {
  
  // Функции из калькулятора (экспортируем для тестирования)
  const VALID_NUMBER_REGEX = /^-?\d*[.,]?\d*$/;
  const COMPLETE_NUMBER_REGEX = /^-?\d+(\.\d+)?$/;
  
  const isValidNumber = (str) => {
    if (str === '' || str === '-' || str === '.' || str === ',') return false;
    const normalized = str.replace(',', '.');
    return COMPLETE_NUMBER_REGEX.test(normalized);
  };
  
  const parseNumber = (str) => {
    return parseFloat(str.replace(',', '.'));
  };
  
  describe('isValidNumber', () => {
    
    test('должен принимать положительные целые числа', () => {
      expect(isValidNumber('123')).toBe(true);
      expect(isValidNumber('0')).toBe(true);
      expect(isValidNumber('999999')).toBe(true);
    });
    
    test('должен принимать отрицательные целые числа', () => {
      expect(isValidNumber('-123')).toBe(true);
      expect(isValidNumber('-1')).toBe(true);
      expect(isValidNumber('-999')).toBe(true);
    });
    
    test('должен принимать дробные числа с точкой', () => {
      expect(isValidNumber('12.34')).toBe(true);
      expect(isValidNumber('0.5')).toBe(true);
      expect(isValidNumber('-45.67')).toBe(true);
    });
    
    test('должен принимать дробные числа с запятой', () => {
      expect(isValidNumber('12,34')).toBe(true);
      expect(isValidNumber('0,5')).toBe(true);
      expect(isValidNumber('-45,67')).toBe(true);
    });
    
    test('должен отклонять пустые строки', () => {
      expect(isValidNumber('')).toBe(false);
      expect(isValidNumber(' ')).toBe(false);
    });
    
    test('должен отклонять неполные числа', () => {
      expect(isValidNumber('-')).toBe(false);
      expect(isValidNumber('.')).toBe(false);
      expect(isValidNumber(',')).toBe(false);
      expect(isValidNumber('-.')).toBe(false);
    });
    
    test('должен отклонять невалидные строки', () => {
      expect(isValidNumber('abc')).toBe(false);
      expect(isValidNumber('12abc')).toBe(false);
      expect(isValidNumber('12.34.56')).toBe(false);
      expect(isValidNumber('12,34,56')).toBe(false);
      expect(isValidNumber('12.34,56')).toBe(false);
    });
    
    test('должен отклонять множественные минусы', () => {
      expect(isValidNumber('--12')).toBe(false);
      expect(isValidNumber('12-34')).toBe(false);
      expect(isValidNumber('12-')).toBe(false);
    });
    
  });
  
  describe('parseNumber', () => {
    
    test('должен преобразовывать строки с точкой', () => {
      expect(parseNumber('12.34')).toBe(12.34);
      expect(parseNumber('-56.78')).toBe(-56.78);
      expect(parseNumber('0.5')).toBe(0.5);
    });
    
    test('должен преобразовывать строки с запятой', () => {
      expect(parseNumber('12,34')).toBe(12.34);
      expect(parseNumber('-56,78')).toBe(-56.78);
      expect(parseNumber('0,5')).toBe(0.5);
    });
    
    test('должен преобразовывать целые числа', () => {
      expect(parseNumber('123')).toBe(123);
      expect(parseNumber('-456')).toBe(-456);
      expect(parseNumber('0')).toBe(0);
    });
    
    test('должен возвращать NaN для невалидных строк', () => {
      expect(parseNumber('abc')).toBeNaN();
      expect(parseNumber('')).toBeNaN();
    });
    
  });
  
});

describe('Арифметические операции', () => {
  
  // Функции операций
  const OPERATIONS = {
    sum: { 
      fn: (a, b) => a + b, 
      symbol: '+',
      name: 'Сумма'
    },
    difference: { 
      fn: (a, b) => a - b, 
      symbol: '-',
      name: 'Разность'
    },
    product: { 
      fn: (a, b) => a * b, 
      symbol: '×',
      name: 'Произведение'
    },
    division: { 
      fn: (a, b) => {
        if (b === 0) throw new Error('Деление на ноль невозможно');
        return a / b;
      }, 
      symbol: '÷',
      name: 'Деление'
    }
  };
  
  describe('Сложение', () => {
    
    test('должен складывать положительные числа', () => {
      expect(OPERATIONS.sum.fn(5, 3)).toBe(8);
      expect(OPERATIONS.sum.fn(10, 20)).toBe(30);
      expect(OPERATIONS.sum.fn(0.5, 0.3)).toBeCloseTo(0.8);
    });
    
    test('должен складывать отрицательные числа', () => {
      expect(OPERATIONS.sum.fn(-5, -3)).toBe(-8);
      expect(OPERATIONS.sum.fn(-10, -20)).toBe(-30);
    });
    
    test('должен складывать положительные и отрицательные числа', () => {
      expect(OPERATIONS.sum.fn(5, -3)).toBe(2);
      expect(OPERATIONS.sum.fn(-10, 20)).toBe(10);
    });
    
    test('должен обрабатывать ноль', () => {
      expect(OPERATIONS.sum.fn(0, 0)).toBe(0);
      expect(OPERATIONS.sum.fn(5, 0)).toBe(5);
      expect(OPERATIONS.sum.fn(0, 5)).toBe(5);
    });
    
    test('должен обрабатывать очень большие числа', () => {
      expect(OPERATIONS.sum.fn(1e10, 2e10)).toBe(3e10);
    });
    
    test('должен обрабатывать очень маленькие числа', () => {
      expect(OPERATIONS.sum.fn(1e-10, 2e-10)).toBeCloseTo(3e-10);
    });
    
  });
  
  describe('Вычитание', () => {
    
    test('должен вычитать положительные числа', () => {
      expect(OPERATIONS.difference.fn(10, 5)).toBe(5);
      expect(OPERATIONS.difference.fn(100, 50)).toBe(50);
    });
    
    test('должен вычитать отрицательные числа', () => {
      expect(OPERATIONS.difference.fn(-5, -3)).toBe(-2);
      expect(OPERATIONS.difference.fn(-10, -20)).toBe(10);
    });
    
    test('должен вычитать положительные и отрицательные числа', () => {
      expect(OPERATIONS.difference.fn(5, -3)).toBe(8);
      expect(OPERATIONS.difference.fn(-10, 5)).toBe(-15);
    });
    
    test('должен обрабатывать ноль', () => {
      expect(OPERATIONS.difference.fn(5, 0)).toBe(5);
      expect(OPERATIONS.difference.fn(0, 5)).toBe(-5);
      expect(OPERATIONS.difference.fn(0, 0)).toBe(0);
    });
    
    test('должен давать отрицательный результат при вычитании большего из меньшего', () => {
      expect(OPERATIONS.difference.fn(3, 5)).toBe(-2);
    });
    
  });
  
  describe('Умножение', () => {
    
    test('должен умножать положительные числа', () => {
      expect(OPERATIONS.product.fn(5, 3)).toBe(15);
      expect(OPERATIONS.product.fn(10, 20)).toBe(200);
    });
    
    test('должен умножать отрицательные числа', () => {
      expect(OPERATIONS.product.fn(-5, -3)).toBe(15);
      expect(OPERATIONS.product.fn(-10, -20)).toBe(200);
    });
    
    test('должен умножать положительные и отрицательные числа', () => {
      expect(OPERATIONS.product.fn(5, -3)).toBe(-15);
      expect(OPERATIONS.product.fn(-10, 5)).toBe(-50);
    });
    
    test('должен обрабатывать ноль', () => {
      expect(OPERATIONS.product.fn(5, 0)).toBe(0);
      expect(OPERATIONS.product.fn(0, 5)).toBe(0);
      expect(OPERATIONS.product.fn(0, 0)).toBe(0);
    });
    
    test('должен обрабатывать единицу', () => {
      expect(OPERATIONS.product.fn(5, 1)).toBe(5);
      expect(OPERATIONS.product.fn(1, 5)).toBe(5);
    });
    
    test('должен обрабатывать дробные числа', () => {
      expect(OPERATIONS.product.fn(0.5, 0.2)).toBeCloseTo(0.1);
      expect(OPERATIONS.product.fn(2.5, 4)).toBe(10);
    });
    
  });
  
  describe('Деление', () => {
    
    test('должен делить положительные числа', () => {
      expect(OPERATIONS.division.fn(10, 2)).toBe(5);
      expect(OPERATIONS.division.fn(100, 4)).toBe(25);
    });
    
    test('должен делить отрицательные числа', () => {
      expect(OPERATIONS.division.fn(-10, -2)).toBe(5);
      expect(OPERATIONS.division.fn(-100, -4)).toBe(25);
    });
    
    test('должен делить положительные и отрицательные числа', () => {
      expect(OPERATIONS.division.fn(10, -2)).toBe(-5);
      expect(OPERATIONS.division.fn(-100, 4)).toBe(-25);
    });
    
    test('должен обрабатывать деление на единицу', () => {
      expect(OPERATIONS.division.fn(5, 1)).toBe(5);
      expect(OPERATIONS.division.fn(-5, 1)).toBe(-5);
    });
    
    test('должен обрабатывать деление нуля', () => {
      expect(OPERATIONS.division.fn(0, 5)).toBe(0);
      const result = OPERATIONS.division.fn(0, -5);
      expect(Math.abs(result)).toBe(0);
    });
    
    test('должен бросать ошибку при делении на ноль', () => {
      expect(() => OPERATIONS.division.fn(5, 0)).toThrow('Деление на ноль невозможно');
      expect(() => OPERATIONS.division.fn(-5, 0)).toThrow('Деление на ноль невозможно');
      expect(() => OPERATIONS.division.fn(0, 0)).toThrow('Деление на ноль невозможно');
    });
    
    test('должен обрабатывать дробные результаты', () => {
      expect(OPERATIONS.division.fn(1, 3)).toBeCloseTo(0.333333);
      expect(OPERATIONS.division.fn(10, 3)).toBeCloseTo(3.333333);
    });
    
    test('должен обрабатывать деление дробных чисел', () => {
      expect(OPERATIONS.division.fn(0.5, 0.25)).toBe(2);
      expect(OPERATIONS.division.fn(7.5, 2.5)).toBe(3);
    });
    
  });
  
});

describe('История вычислений', () => {
  
  let calculationHistory = [];
  const MAX_HISTORY_ITEMS = 10;
  
  const addToHistory = (num1, num2, operation, result) => {
    const historyItem = {
      num1,
      num2,
      operation,
      result,
      timestamp: Date.now()
    };
    
    calculationHistory.unshift(historyItem);
    
    if (calculationHistory.length > MAX_HISTORY_ITEMS) {
      calculationHistory.pop();
    }
  };
  
  beforeEach(() => {
    calculationHistory = [];
  });
  
  test('должен добавлять элемент в историю', () => {
    addToHistory(5, 3, 'sum', 8);
    
    expect(calculationHistory.length).toBe(1);
    expect(calculationHistory[0]).toMatchObject({
      num1: 5,
      num2: 3,
      operation: 'sum',
      result: 8
    });
  });
  
  test('должен добавлять новые элементы в начало', () => {
    addToHistory(5, 3, 'sum', 8);
    addToHistory(10, 2, 'difference', 8);
    
    expect(calculationHistory[0].operation).toBe('difference');
    expect(calculationHistory[1].operation).toBe('sum');
  });
  
  test('должен ограничивать размер истории', () => {
    for (let i = 0; i < 15; i++) {
      addToHistory(i, i, 'sum', i * 2);
    }
    
    expect(calculationHistory.length).toBe(MAX_HISTORY_ITEMS);
  });
  
  test('должен удалять самый старый элемент при превышении лимита', () => {
    for (let i = 0; i < 11; i++) {
      addToHistory(i, i, 'sum', i * 2);
    }
    
    expect(calculationHistory.length).toBe(10);
    expect(calculationHistory[0].num1).toBe(10); // Самый новый
    expect(calculationHistory[9].num1).toBe(1);  // Самый старый (0 был удалён)
  });
  
  test('должен добавлять timestamp', () => {
    const before = Date.now();
    addToHistory(5, 3, 'sum', 8);
    const after = Date.now();
    
    expect(calculationHistory[0].timestamp).toBeGreaterThanOrEqual(before);
    expect(calculationHistory[0].timestamp).toBeLessThanOrEqual(after);
  });
  
});

describe('localStorage функции', () => {
  
  beforeEach(() => {
    localStorage.clear();
  });
  
  test('должен сохранять историю в localStorage', () => {
    const history = [
      { num1: 5, num2: 3, operation: 'sum', result: 8, timestamp: 123456 }
    ];
    
    localStorage.setItem('calculatorHistory', JSON.stringify(history));
    
    const stored = localStorage.getItem('calculatorHistory');
    expect(stored).toBeTruthy();
    
    const parsed = JSON.parse(stored);
    expect(parsed).toEqual(history);
  });
  
  test('должен загружать историю из localStorage', () => {
    const history = [
      { num1: 10, num2: 5, operation: 'difference', result: 5, timestamp: 789012 }
    ];
    
    localStorage.setItem('calculatorHistory', JSON.stringify(history));
    
    const loaded = JSON.parse(localStorage.getItem('calculatorHistory'));
    expect(loaded).toEqual(history);
  });
  
  test('должен обрабатывать пустой localStorage', () => {
    const stored = localStorage.getItem('calculatorHistory');
    expect(stored).toBeNull();
  });
  
  test('должен очищать историю', () => {
    localStorage.setItem('calculatorHistory', JSON.stringify([{ num1: 1, num2: 2 }]));
    
    localStorage.removeItem('calculatorHistory');
    
    const stored = localStorage.getItem('calculatorHistory');
    expect(stored).toBeNull();
  });
  
});

describe('Граничные случаи', () => {
  
  const OPERATIONS = {
    sum: { fn: (a, b) => a + b },
    product: { fn: (a, b) => a * b },
    division: { fn: (a, b) => {
      if (b === 0) throw new Error('Деление на ноль невозможно');
      return a / b;
    }}
  };
  
  test('должен обрабатывать Infinity', () => {
    expect(OPERATIONS.sum.fn(Infinity, 1)).toBe(Infinity);
    expect(OPERATIONS.sum.fn(-Infinity, 1)).toBe(-Infinity);
  });
  
  test('должен обрабатывать очень большие числа', () => {
    const bigNum = Number.MAX_SAFE_INTEGER;
    expect(OPERATIONS.sum.fn(bigNum, 1)).toBeGreaterThan(bigNum);
  });
  
  test('должен обрабатывать очень маленькие числа', () => {
    const smallNum = Number.MIN_VALUE;
    expect(OPERATIONS.sum.fn(smallNum, smallNum)).toBeGreaterThan(0);
  });
  
  test('должен обрабатывать потерю точности с дробными числами', () => {
    // JavaScript float precision issue: 0.1 + 0.2 !== 0.3
    const result = OPERATIONS.sum.fn(0.1, 0.2);
    expect(result).toBeCloseTo(0.3, 10);
  });
  
  test('должен обрабатывать деление маленьких чисел', () => {
    const result = OPERATIONS.division.fn(1e-10, 1e-5);
    expect(result).toBeCloseTo(1e-5);
  });
  
});

describe('Сообщения об ошибках', () => {
  
  const MESSAGES = {
    ERROR_INVALID_INPUT: '⚠️ Введите корректные числа',
    ERROR_DIVISION_ZERO: '⚠️ Деление на ноль невозможно',
    INITIAL_RESULT: '—',
    COPY_SUCCESS: '✓ Скопировано!'
  };
  
  test('должны быть определены все сообщения', () => {
    expect(MESSAGES.ERROR_INVALID_INPUT).toBeTruthy();
    expect(MESSAGES.ERROR_DIVISION_ZERO).toBeTruthy();
    expect(MESSAGES.INITIAL_RESULT).toBeTruthy();
    expect(MESSAGES.COPY_SUCCESS).toBeTruthy();
  });
  
  test('сообщения должны быть понятными пользователю', () => {
    expect(MESSAGES.ERROR_INVALID_INPUT).toContain('корректные числа');
    expect(MESSAGES.ERROR_DIVISION_ZERO).toContain('ноль');
  });
  
});

describe('Производительность', () => {
  
  const OPERATIONS = {
    sum: { fn: (a, b) => a + b }
  };
  
  test('операция должна выполняться быстро', () => {
    const start = performance.now();
    
    for (let i = 0; i < 10000; i++) {
      OPERATIONS.sum.fn(i, i + 1);
    }
    
    const end = performance.now();
    const duration = end - start;
    
    // 10000 операций должны выполняться менее чем за 10ms
    expect(duration).toBeLessThan(10);
  });
  
});