width_cake = int(input())
length_cake = int(input())
number_pieces = width_cake * length_cake * 1
taken_pieces = 0
pieces_left = 0
while taken_pieces < number_pieces:
    command = input()
    if command == "STOP":
        pieces_left = number_pieces - taken_pieces
        print(f"{pieces_left} pieces are left.")
        break
    else:
        piece = int(command)
        taken_pieces += piece
    if taken_pieces >= number_pieces:
        break
if taken_pieces >= number_pieces:
    needed_piece = taken_pieces - number_pieces
    print(f"No more cake left! You need {needed_piece} pieces more.")


