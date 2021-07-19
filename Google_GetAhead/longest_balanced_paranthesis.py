def longest_balanced(string):
    count = 0
    stack = [-1]

    for ele in range(len(string)):
        if (string[ele] == "("):
            stack.append(ele)
        else:
            if (stack) and (stack[-1] != -1) and (string[stack[-1]] == "("):
                stack.pop()
                count = max(count, ele - stack[-1])
            else:
                stack.append(ele)

    return count

test1 = longest_balanced("))(())())")
print(test1)