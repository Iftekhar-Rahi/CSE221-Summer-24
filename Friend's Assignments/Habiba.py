def findGroups(amounts, fare):
    groups = []
    ungrouped = []
    used = [False] * len(amounts)
    for i in range(len(amounts)):
        if used[i]:
            continue
        found_group = False
        for j in range(i + 1, len(amounts)):
            if used[j]:
                continue
            if amounts[i] + amounts[j] == fare:
                groups.append((amounts[i], amounts[j]))
                used[i] = True
                used[j] = True
                found_group = True
                break
        if not found_group and amounts[i] == fare:
            groups.append((amounts[i],))
            used[i] = True
    for i in range(len(amounts)):
        if not used[i]:
            ungrouped.append(amounts[i])
    for idx, group in enumerate(groups):
        print(f"Group {idx + 1} : {', '.join(map(str, group))}")
    if len(ungrouped)!=0:
        print(f"Ungrouped : {' '.join(map(str, ungrouped))}")
findGroups([120, 100, 150, 50, 30], 150)
findGroups([60, 150, 60, 30, 120, 30], 180)
findGroups([30, 150, 150], 180)
