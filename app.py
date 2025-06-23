import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Agent Shimronz", layout="centered")

# Title
st.title("🕵️ Agent Shimronz - Real Estate Skip Tracing Assistant")

# Description
st.markdown("""
**Agent Shimronz** is designed to perform:
- 🧩 Skip tracing on eager real estate sellers  
- 📊 SLOP report generation  
- 🏡 Property value estimation based on city and state  

**Automation includes:**
- Up to **200 searches/day** (adjustable up to **1,000**)  
- Search runs daily between **12:00 AM and 5:00 AM**  
- CSV report delivered by **7:00 AM** via email  
- Works **365 days a year**
""")

# Adjustable search count
max_searches = st.slider("Select number of skip traces to perform today", min_value=100, max_value=1000, step=50, value=200)

# Simulated skip trace data
def simulate_skip_trace(n):
    return pd.DataFrame({
        "Name": [f"Seller {i}" for i in range(1, n+1)],
        "Phone": [f"(555) 010-{str(i).zfill(4)}" for i in range(1, n+1)],
        "Email": [f"brendarmster@gmail.com" for i in range(1, n+1)],
        "City": ["City A"]*n,
        "State": ["State X"]*n,
        "Estimated Property Value": [round(100000 + i*500, 2) for i in range(n)],
        "SLOP Rating": ["Hot" if i % 3 == 0 else "Warm" for i in range(n)]
    })

data = simulate_skip_trace(max_searches)

st.success(f"✅ {max_searches} skip traces completed successfully.")
st.dataframe(data.head(10))

# Download CSV
csv = data.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Full CSV Report", data=csv, file_name="shimronz_skip_trace.csv", mime="text/csv")

# Time and schedule section
now = datetime.now()
next_run = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
email_delivery = next_run + timedelta(hours=7)

st.markdown(f"""
#### 🕑 Next Scheduled Run
- Search Window: **{next_run.strftime('%I:%M %p')} to {(next_run + timedelta(hours=5)).strftime('%I:%M %p')}**
- Report emailed by: **{email_delivery.strftime('%I:%M %p')}**
""")
