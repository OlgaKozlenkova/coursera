n = list(map(int, input().split()))
ann_colors = set()
bob_colors = set()
for i in range(n[0]):
    a_colors = int(input())
    ann_colors.add(a_colors)
for j in range(n[1]):
    b_colors = int(input())
    bob_colors.add(b_colors)
both = ann_colors & bob_colors
ann_cub_colors = ann_colors - bob_colors
bob_cube_colors = bob_colors - ann_colors
print(len(both))
print(*sorted(both))
print(len(ann_cub_colors))
print(*sorted(ann_cub_colors))
print(len(bob_cube_colors))
print(*sorted(bob_cube_colors))
