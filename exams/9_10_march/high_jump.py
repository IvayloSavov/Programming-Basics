from sys import maxsize
record_beam = int(input())
current_beam = record_beam - 30
count_jump = 0
is_fail = False
fail_jump = 0
while not is_fail:
    jump = int(input())
    count_jump += 1
    if jump <= current_beam:
        fail_jump += 1
        if fail_jump == 3:
            is_fail = True
    else:
        if current_beam >= record_beam:
            break
        current_beam += 5
        fail_jump = 0

if is_fail:
    print(f"Tihomir failed at {current_beam}cm after {count_jump} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {current_beam}cm after {count_jump} jumps.")