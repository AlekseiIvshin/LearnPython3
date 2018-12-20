visual_mode = False

if visual_mode:
  import draw_visual as draw
else:
  import draw_textual as draw

from foo import bar;

def play_game():
  return "Game is not implemented yet"

bar.func_bar()

def main():
  result = play_game()
  draw.draw_game(result)

found_members = []
for member in dir(bar):
  if "func" in member:
    found_members.append(member)

print(found_members)


if __name__ == "__main__":
  main()
