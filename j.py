def get_ints():
    return map(int, input().strip().split())

t, n = get_ints()

cables = []
for i in range(n):
    time_taken, impact = map(int, input().strip().split())
    cables.append((time_taken, impact))

def permutate_cuts(cables, cable_index, running_time_taken, running_impact):
    if cable_index >= n:
        return running_impact
    time_taken, impact = cables[cable_index]
    next_index = cable_index + 1

    best_without = permutate_cuts(cables, next_index, running_time_taken, running_impact)

    time_taken_with = running_time_taken + time_taken
    if time_taken_with > t:
        return best_without
    impact_with = running_impact + impact
    best_with = permutate_cuts(cables, next_index, time_taken_with, impact_with)

    return max(best_with, best_without)

print(permutate_cuts(cables, 0, 0, 0))