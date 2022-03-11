
# import keyboard

# selected = 1

# def show_menu():
#     global selected
#     print("\n" * 30)
#     print("Choose an option:")
#     for i in range(1, 5):
#         print("{1} {0}. Do something {0} {2}".format(i, ">" if selected == i else " ", "<" if selected == i else " "))

# def up():
#     global selected
#     if selected == 1:
#         return
#     selected -= 1
#     show_menu()

# def down():
#     global selected
#     if selected == 4:
#         return
#     selected += 1
#     show_menu()

# show_menu()
# keyboard.add_hotkey('up', up)
# keyboard.add_hotkey('down', down)
# keyboard.wait()

import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
keyboard.wait()
