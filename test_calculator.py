from calculator import add, subtract, multiply, divide

def main():
    test_add()

def test_add():
    try:
        assert add(1, 2) == 3
    except AssertionError:
        print("1 + 2 is not 3")

if __name__ == "__main__":
    main()