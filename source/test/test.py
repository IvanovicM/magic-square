from ..utils.magic import MagicSquare

if __name__ == '__main__':
    ms = MagicSquare(5)
    ms.init_random()
    print(ms['matrix'])