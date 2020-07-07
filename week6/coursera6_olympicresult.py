class Participant:
    name = " "
    balls = 0


def __str__(self):
    return self.name


num_part = int(input())
part_list = []
for i in range(num_part):
    part_data = input().split()
    part = Participant()
    part.name = part_data[0]
    part.balls = int(part_data[1])
    part_list.append(part)
part_list.sort(key=lambda part_data: part_data.balls, reverse=True)
for part in part_list:
    print(part.name)
