import streamlit as st
import google.generativeai as genai

# 1. نفس الألوان الهادئة الباستيل اللي اختاريتيها
COLORS = {
    "bg_color": "#FFF9F2",       # Off-white
    "primary": "#A9D9E8",        # Sky blue
    "accent": "#C7B9E8"          # Lavender
}

# إعدادات صفحة الويب
st.set_page_config(page_title="ClearMind AI", page_icon="🧠", layout="centered")

# تطبيق الألوان الهادئة ف الموقع
st.markdown(f"""
    <style>
    .stApp {{ background-color: {COLORS['bg_color']}; }}
    h1 {{ color: {COLORS['accent']}; }}
    </style>
""", unsafe_allow_html=True)

st.title("🧠 ClearMind AI")
st.write("مرحباً بك في فضائك الآمن لإدارة التوتر والصحة النفسية مع تطبيق ClearMind.")

api_key = "AQ.Ab8RN6JCEMuQzqyhhllQmIJVxZBSUIWKJ-UwZ3IFM77gtpFQwg"

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# صندوق المحادثة الذكي
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة ف الشاشة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# استقبال رسالة جديدة من المستخدم
user_input = st.chat_input("بماذا تشعرين الآن؟...")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # طلب الرد من Gemini
    try:
        prompt = f"You are ClearMind, a compassionate, supportive, and kind AI mental health companion. Respond to the user with deep empathy. User: {user_input}"
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = "أنا هنا ديما باش نسمع ليك ونمسح عليك. قولي ليا كثر على شنو حاسة بيه دابا؟"
        
    with st.chat_message("assistant"):
        st.write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
