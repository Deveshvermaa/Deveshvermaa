import streamlit as st

# Page Configuration
st.set_page_config(page_title="Pehla Kadam - Baby Care", page_icon="👶", layout="wide")

# Custom CSS for Pink/Blue Theme
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1 { color: #D81B60; text-align: center; font-family: 'Arial'; }
    .stAlert { border-radius: 20px; }
    .stButton>button { background-color: #F06292; color: white; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🍼 Pehla Kadam: Nayi Mummy ka Digital Saathi")
st.markdown("<h4 style='text-align: center;'>Bacche ke 0-2 saal tak ka poora nutrition aur health guide</h4>", unsafe_allow_html=True)

# Daily Reminder Section
st.info("🌟 **Aaj ki Tip:** Har roz bacche ko thodi der dhoop mein lekar baithein (Vitamin D), lekin halki dhoop mein.")

# Sidebar Navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9368/9368307.png", width=100)
age_group = st.sidebar.selectbox("Bacche ki Umra Chunein:", ["0-3 Mahine", "3-6 Mahine", "6-12 Mahine", "1-2 Saal"])

# Main Content Logic
if age_group == "0-3 Mahine":
    st.header("🤱 Shuruati Dekhbhal (0-3 Mahine)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🥣 Nutrition")
        st.write("- **Sirf Maa ka Doodh:** 6 mahine tak kuch aur na dein.")
        st.write("- **Feeding Time:** Har 2-3 ghante mein feed karayein.")
        st.image("https://images.pexels.com/photos/3760205/pexels-photo-3760205.jpeg?auto=compress&w=400")
    with col2:
        st.subheader("📹 Care Video")
        st.video("https://www.youtube.com/watch?v=R9U0X8H6V8I")
        st.subheader("💉 Vaccines")
        st.checkbox("BCG (At Birth)")
        st.checkbox("Polio (OPV-0)")
        st.checkbox("Hepatitis B")

elif age_group == "3-6 Mahine":
    st.header("👶 Vikas ki Shuruat (3-6 Mahine)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🥣 Nutrition")
        st.write("- Abhi bhi sirf breastfeeding hi best hai.")
        st.write("- Bacche ko 'Tummy Time' (pet ke bal) dein.")
        st.image("https://images.pexels.com/photos/3845492/pexels-photo-3845492.jpeg?auto=compress&w=400")
    with col2:
        st.subheader("📹 Massage & Care")
        st.video("https://www.youtube.com/watch?v=q60h7FvQ-00")
        st.subheader("💉 Vaccines")
        st.checkbox("Pentavalent 1, 2, 3")
        st.checkbox("Rotavirus")

elif age_group == "6-12 Mahine":
    st.header("🥣 Naya Khana (6-12 Mahine)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🍎 Nutrition Chart")
        st.write("- **Start Solids:** Dal ka paani, Mashed Banana, Suji halwa.")
        st.write("- Din mein 2 baar solid aur baaki time doodh.")
        st.image("https://images.pexels.com/photos/5623861/pexels-photo-5623861.jpeg?auto=compress&w=400")
    with col2:
        st.subheader("📹 Feeding Guide")
        st.video("https://www.youtube.com/watch?v=FjC2X94i8w8")
        st.subheader("💉 Vaccines")
        st.checkbox("Measles/MR 1st Dose")
        st.checkbox("Vitamin A")

elif age_group == "1-2 Saal":
    st.header("🏃 नटखट Bachpan (1-2 Saal)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🍛 Family Diet")
        st.write("- Ab baccha ghar ka sab kuch kha sakta hai.")
        st.write("- Dahi, Paneer aur Phal rozana dein.")
        st.image("https://images.pexels.com/photos/5691079/pexels-photo-5691079.jpeg?auto=compress&w=400")
    with col2:
        st.subheader("📹 Learning Video")
        st.video("https://www.youtube.com/watch?v=26I-a0Z5Dpw")
        st.subheader("💉 Vaccines")
        st.checkbox("DPT Booster")
        st.checkbox("MMR 2nd Dose")

# Footer Tool
st.divider()
st.subheader("🚑 Emergency Contact")
doc_num = st.text_input("Apne Doctor ka number yahan save karein:")
if st.button("Save Number"):
    st.success(f"Number {doc_num} save ho gaya hai!")

st.markdown("<p style='text-align: center; margin-top: 50px;'>Made with ❤️ for Mummies</p>", unsafe_allow_html=True)
