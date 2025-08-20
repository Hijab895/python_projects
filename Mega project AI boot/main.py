import pyautogui
import pyperclip
import time
import google.generativeai as genai
genai.configure(api_key="AIzaSyBthkLAGNFuAmkGlT4-bw9BHIanpjxr0Ao")
def is_last_message_from_sender(chat_log, sender_name="Mehwish"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
# Small delay before execution so you can prepare the screen
time.sleep(3)
# Step 1: Click on icon
pyautogui.click(813,1068)

time.sleep(1)  # wait a bit for the window/app to open
while True:
# Step 2: Drag to select text
    pyautogui.moveTo(1885,199, duration=0.5)   # move to start point
    pyautogui.dragTo(1440,1006, duration=1, button='left')  # drag to end

# Step 3: Copy to clipboard (Ctrl+C)
    pyautogui.hotkey("ctrl", "c")

    time.sleep(0.5)  # wait for clipboard to update
    pyautogui.click(1504,756)

# Step 4: Get clipboard text
    chat_history = pyperclip.paste()

    print( chat_history)
    if is_last_message_from_sender(chat_history):
        model = genai.GenerativeModel(
        "gemini-1.5-flash",
        system_instruction="You are Hijab, living in Pakistan, who speaks  Urdu. Analyze chat history and act like Hijab when responding.Output should be next chat response from Hijab.Dont write urdu text but write in a way sender is sending the text.Respond only in one language and dont write time date and name of yours at start of reply."
)

# Generate response
        response = model.generate_content(chat_history)

# Print result
        pyperclip.copy(response.text)


        pyautogui.click(1788, 993)

        time.sleep(0.5)

# Step 2: Paste (Ctrl+V)
        pyautogui.hotkey("ctrl", "v")

        time.sleep(0.5)

# Step 3: Press Enter
        pyautogui.press("enter")

