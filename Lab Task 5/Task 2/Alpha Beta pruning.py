def search_alphabeta(tree, alpha, beta, maximizing):
    global count

    if type(tree) == int:
        count += 1
        return tree

    if maximizing:
        value = float('-inf')

        for child in tree:
            result = search_alphabeta(child, alpha, beta, False)
            value = max(value, result)
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in tree:
            result = search_alphabeta(child, alpha, beta, True)
            value = min(value, result)
            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


tree = [[[4, 7], [2, 6]], [[8, 3], [5, 9]]]

count = 0
result = search_alphabeta(tree, float('-inf'), float('inf'), True)

print("Alpha-Beta Value:", result)
print("Leaf Evaluations:", count)