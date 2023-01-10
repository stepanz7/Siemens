"""
This program serves a purpose of simplifing given code.
"""
import sys

# Original code:
def foo1(items):
    result = []
    for i in range(len(items)):

        flag = False
        for j in range(len(result)):

            if items[i] == result[j]:
                flag = True
                break

        if not flag:
            result.append(items[i])
    return result

# Simplified version
def foo2(items):
    result = []
    for i in range(len(items)):
        if not items[i] in result:
            result.append(items[i])
    return result

def main():
    word = sys.argv[1]
    print(foo1(word))
    print(foo2(word))

if __name__ == '__main__':
    main()
