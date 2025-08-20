import google.generativeai as genai

# Configure first
genai.configure(api_key="AIzaSyBthkLAGNFuAmkGlT4-bw9BHIanpjxr0Ao")

# Attach system instructions to the model
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="You are Hijab, living in Pakistan, who speaks English and Urdu. You are a coder. Analyze chat history and act like Hijab when responding."
)

def ask_gemini(command):
    response = model.generate_content(command)
    return response.text
command='''Explain what this chat means: [12:01 PM, 8/18/2025] [12:01 PM, 8/18/2025] Hijab Fatima>>❤️: Han na yeah tu poocho tum log
[12:02 PM, 8/18/2025] Hijab Fatima>>❤️: Yeah jo pdf hai yeah word mein ni khuly ga
[12:03 PM, 8/18/2025] Hijab Fatima>>❤️: Aur copy bhi ni hoga
[12:03 PM, 8/18/2025] Hijab Fatima>>❤️: Khud type krna pary ga
[12:03 PM, 8/18/2025] Hijab Fatima>>❤️: Ya phir google sy yeah story utha ky word pr paste kar do
[12:06 PM, 8/18/2025] Mehwish: Axa
[12:19 PM, 8/18/2025] Hijab Fatima>>❤️: Meri bat sun madam
[12:19 PM, 8/18/2025] Hijab Fatima>>❤️: Hani ko bhej
[12:19 PM, 8/18/2025] Hijab Fatima>>❤️: Mery ghar jaldi sy
[12:20 PM, 8/18/2025] Mehwish: Ok'''
# Example usage
print(ask_gemini(command))
