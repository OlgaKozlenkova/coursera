archive_us = list(map(int, input().split()))
archive_size = archive_us[0]
users = archive_us[1]
user_disks = []
read_users = 0
pukUser = 0

while read_users < users:
    user_disk = int(input())
    user_disks.append(user_disk)
    read_users += 1

user_disks.sort()

all_size = 0

for i in range(len(user_disks)):
    if all_size < archive_size:
        all_size += user_disks[i]
        if all_size <= archive_size:
            pukUser += 1
print(pukUser)

# if sum(user_disks) <= archive_size:
# for i, disk in enumerate(user_disks):
#    if all_size >= archive_size:
#        break
#    else:
#        all_size += disk
# print(i)
#
