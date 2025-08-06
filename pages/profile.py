import json
import streamlit as st

from app.config import JSON_DIR
from app.profile.profile import generate_profile_from_text

st.title("🧠 Interactive Profile Builder")
st.subheader("🔍 Generate Profile from Text or CV")


raw_text = st.text_area("Paste your existing CV or descriptive text")


profile = None
if raw_text:
    profile = generate_profile_from_text(raw_text)

elif st.button("Generate Profile"):
    if raw_text:
        profile = generate_profile_from_text(raw_text)


if profile:
    st.subheader("Generated Profile")

    json_bytes = json.dumps(profile, indent=2, ensure_ascii=False).encode("utf-8")
    st.session_state.profile = profile

    st.download_button(
        label="💾 Download JSON",
        data=json_bytes,
        file_name="profile.json",
        mime="application/json"
    )





# Save to abilities.json in the data folder
with open(JSON_DIR, 'w', encoding='utf-8') as f:
    json.dump(profile, f, indent=2, ensure_ascii=False)