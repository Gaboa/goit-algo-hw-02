from collections import deque


def is_palindrome(s):
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True

def main():
    test_strings = ["radar", "hello", "level", "world", "dima"]
    for s in test_strings:
        print(f"Is '{s}' a palindrome? {is_palindrome(s)}")

if __name__ == "__main__":
    main()