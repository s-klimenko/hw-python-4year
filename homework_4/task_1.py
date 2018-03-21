import unittest


def poly_hash(s, x=31, p=997):
    h = 0
    for j in range(len(s)-1, -1, -1):
        h = (h * x + ord(s[j]) + p) % p
    return h

def search_rabin_multi(text, patterns, x=31, p=997):
    """
    text - строка, в которой выполняется поиск
    patterns = [pattern_1, pattern_2, ..., pattern_n] - массив паттернов, которые нужно найти в строке text
    По аналогии с оригинальным алгоритмом, функция возвращает массив [indices_1, indices_2, ... indices_n]
    При этом indices_i - массив индексов [pos_1, pos_2, ... pos_n], с которых начинаетй pattern_i в строке text.
    Если pattern_i ни разу не встречается в строке text, ему соотвествует пустой массив, т.е. indices_i = []
    """
    if not patterns:
        return 'Patterns list is empty'

    all_inds = []

    for pattern in patterns:
        indices = []

        if not isinstance(pattern, str):
            print('Pattern is not string, skipping')
            continue

        if len(pattern) == 0:
            print('Pattern is empty')
            all_inds.append([])
            continue

        if len(text) < len(pattern):
            print('Pattern is too long')
            all_inds.append([])
            continue

        # precompute hashes
        precomputed = [0] * (len(text) - len(pattern) + 1)
        precomputed[-1] = poly_hash(text[-len(pattern):], x, p)

        factor = 1
        for i in range(len(pattern)):
            factor = (factor * x + p) % p

        for i in range(len(text) - len(pattern) - 1, -1, -1):
            precomputed[i] = (precomputed[i + 1] * x + ord(text[i]) - factor * ord(text[i + len(pattern)]) + p) % p

        pattern_hash = poly_hash(pattern, x, p)
        for i in range(len(precomputed)):
            if precomputed[i] == pattern_hash:
                if text[i: i + len(pattern)] == pattern:
                    indices.append(i)

        all_inds.append(indices)

    if not all_inds:
        return 'No string patterns'
    return all_inds

class TestRabin(unittest.TestCase):


    def test_normal(self, text='hello hello world'):
        self.assertEqual(search_rabin_multi(text, ['wor']), [[12]])  # 1 раз
        self.assertEqual(search_rabin_multi(text, ['hell']), [[0, 6]])  # несколько раз
        self.assertEqual(search_rabin_multi(text, ['hell', 'wor']), [[0, 6], [12]])  # несколько паттернов
        self.assertEqual(search_rabin_multi(text, ['hell', 'hello']), [[0, 6], [0, 6]])  # несколько паттернов включающие друг друга

    def test_absent(self, text='hello hello world'):
        self.assertEqual(search_rabin_multi(text, ['bor']), [[]])  # отсутствует
        self.assertEqual(search_rabin_multi(text, ['hell', 'bor']), [[0, 6], []])  # отсутствует один из паттернов
        self.assertEqual(search_rabin_multi(text, ['bell', 'bor']), [[], []])  # отсутствуют все паттерны

    def test_problem(self, text='hello hello world'):
        self.assertEqual(search_rabin_multi(text, []), 'Patterns list is empty')  # пустой запрос
        self.assertEqual(search_rabin_multi(text, [1]), 'No string patterns')  # паттерн не str
        self.assertEqual(search_rabin_multi(text, ['hello hello world world']), [[]])  # слишком длинный паттерн

if __name__ == '__main__':
    unittest.main()

# для оригинального алгоритма сложность была O(T + nP), где T - длинна текста, P - паттерн, n - кол-во
# встречаемости паттерна в тексте, значит для решения через цикл сложность возрастет
# до O(T + n1P1 + ... + niPi), где i - количество паттернов