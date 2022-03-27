
box, dup, temp = [4, 1, 8, 9, 13, 8, 34, 2, 13, 0, 8], [], []
print('Original List:', box)

for i in range(len(box)):
    for j in range(i+1, len(box)):
        if box[i] == box[j]:
            if i not in dup: temp.append(box[i])
            if j not in dup: temp.append(box[j])
            dup.append(i), dup.append(j)
            
for i in temp:
    box.remove(i)

print('New List:', box)