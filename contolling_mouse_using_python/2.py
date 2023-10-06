from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print((x,y))
    
    if not pressed:
        # Stop listener
        return False

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

listener=mouse.Listener(
    on_click=on_click
    )
listener.start()
