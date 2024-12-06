
def find_best_split(zeros, crosses):
    lin = False
    zeros = sorted(zeros)
    crosses = sorted(crosses)
    all_points = sorted(zeros + crosses)
    max_accuracy = best_point = result = left_zeros = 0

    right_crosses = len(crosses)
    accuracy = (left_zeros + right_crosses) / (len(zeros) + len(crosses))
    if accuracy > max_accuracy:
        best_point = float('-inf')
    for point in all_points:
        left_zeros = sum(1 for x in zeros if x <= point)
        right_zeros = sum(1 for x in zeros if x > point)
        right_crosses = sum(1 for x in crosses if x > point)
        left_crosses = sum(1 for x in crosses if x <= point)
        accuracy = max((left_zeros + right_crosses) / (len(zeros) + len(crosses)), (right_zeros + left_crosses) / (len(zeros) + len(crosses)))

        if accuracy > max_accuracy:
            max_accuracy = accuracy
            if max_accuracy == 1:
                lin = True

            best_point = point

            left_max = max([x for x in zeros if x <= point], default=None)

            right_min = min([x for x in crosses if x > point], default=None)

            if left_max is not None and right_min is not None:
                result = (left_max + right_min) / 2

    return result, max_accuracy, lin

r1 = [int(x) for x in input('введите массив с ноликами: ').split()]
r2 = [int(x) for x in input('введите массив с крестиками: ').split()]

if find_best_split(r1, r2)[1] == True:
    print('Линейно разделимы')
else:
    print('Линейно не разделимы')
print(f'Точка - {find_best_split(r1, r2)[0]}')
print(f'accuracy - {find_best_split(r1, r2)[1]}')



