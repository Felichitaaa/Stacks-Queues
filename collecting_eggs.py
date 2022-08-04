from collections import deque
egg_deque = deque(int(el)for el in input().split(', ')) #egg with its size-deque
piece_of_paper_stack = [int(x) for x in input().split(', ')]#piece of paper with its size

BOX_SIZE = 50#max size is 50
filled_boxes = 0
while egg_deque and piece_of_paper_stack:
    egg = egg_deque.popleft()
    paper = piece_of_paper_stack.pop()
    if egg <= 0:
        piece_of_paper_stack.append(paper)
        continue
    if egg == 13:
        piece_of_paper_stack.append(paper)
        piece_of_paper_stack[0], piece_of_paper_stack[-1] = piece_of_paper_stack[-1], piece_of_paper_stack[0]
        continue
    if egg + paper <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg_deque:
    print(f"Eggs left: {', '.join([str(x) for x in egg_deque])}")
if piece_of_paper_stack:
    print(f"Piece of paper left: {', '.join([str(x) for x in piece_of_paper_stack])}")
