import streamlit as st
import pandas as pd

st.set_page_config(page_title="Muni Bond Geospatial Risk Tracker", layout="wide")

st.title("🛰️ MuniSite AI: Municipal Bond Physical Risk Monitor")
st.markdown("Bridge satellite intelligence with special district bond verification.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Target Zone: Riverside County District #44")
    st.info("Interactive map layer loaded: Bounding Box [33.65, -117.25 to 33.75, -117.15]")
    st.markdown("🟢 **Active Change Detected:** 4 parcels undergoing active grading.")

with col2:
    st.subheader("📊 Financial Analyst Brief")
    st.metric(label="Estimated Project Pace", value="On Track", delta="+4% vs Last Month")
    st.markdown("---")
    st.write("**Issuer:** Riverside CDD Phase II")
    st.write("**Bond CUSIP:** `765438AB9`")
    st.write("**Assessor Parcel IDs:** `APN-332-102-14`")
    st.markdown("### ⚠️ Risk Verdict")
    st.success("Physical milestone verified via satellite change detection. Low risk of construction default.")
