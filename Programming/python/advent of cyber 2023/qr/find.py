
# hubs.la/Q02btlld0
# found at https://twitter.com/RealTryHackMe/status/1730184898365767880
lower_right = "https://assets.tryhackme.com/additional/aoc2023/2f7f8/0f93a.png?utm_content=272759922&utm_medium=social&utm_source=twitter&hss_channel=tw-1059140424625991680"

# https://hubs.la/Q02bklp30
# found at https://www.linkedin.com/posts/tryhackme_can-you-help-elf-mcskidy-and-her-team-tackle-activity-7135598321280188416-5wnQ?utm_source=share&utm_medium=member_desktop
lower_left = "https://assets.tryhackme.com/additional/aoc2023/5d60a/809cd.png?utm_content=272032783&utm_medium=social&utm_source=linkedin&hss_channel=lcp-14055650"

# found at https://tryhackme.com/room/adventofcyber23sidequest
upper_left = "https://assets.tryhackme.com/additional/aoc2023/6d156/50af2.png"

common_part = "https://assets.tryhackme.com/additional/aoc2023/"
lr = "2f7f8/0f93a.png"
ll = "5d60a/809cd.png"
ul = "6d156/50af2.png"

# all characters are hex 0-f

# assume the same format for last image

# first download the images here


# simple loop

for i in range(0x10000, 0x100000):
    # Convert the integer to hexadecimal and remove the '0x' prefix
    hex_number = hex(i)[2:]
    print(hex_number)
