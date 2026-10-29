def value_minimax(current_node, maximizing, count):
    if type(current_node) == int:
        count[0] += 1
        return current_node

    values = []
    for child in current_node:
        values.append(value_minimax(child, not maximizing, count))

    if maximizing:
        return max(values)
    else:
        return min(values)


tree = [[[4, 7], [2, 6]],[[8, 3], [5, 9]]]

count = [0]
final_result = value_minimax(tree, True, count)

print("Minimax Value is:", final_result)
print("The Leaf Evaluation is:", count[0])