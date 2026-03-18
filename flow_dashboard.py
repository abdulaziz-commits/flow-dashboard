import streamlit as st

st.set_page_config(page_title="Flow System Dashboard", layout="centered")

st.title("🧠 Flow System Dashboard")

# Inputs
st.header("Inputs")

system = st.text_input("System Name", "Duqm Logistics")
flow_type = st.selectbox("Flow Type", ["Energy", "Knowledge", "Logistics", "Capital"])
stage = st.selectbox("Stage", ["Production", "Transfer", "Synchronization"])

multiplicity = st.selectbox("Multiplicity", [0, 1, 2, 3])
sync = st.selectbox("Synchronization", ["Full", "Partial", "None"])

# Logic
if multiplicity == 0 or sync == "None":
    flow_state = "🔴 Collapse"
elif multiplicity == 1 and sync == "Full":
    flow_state = "🟡 Stable Scarcity"
elif multiplicity == 1:
    flow_state = "🟠 Disturbed Scarcity"
elif multiplicity > 1 and sync == "Full":
    flow_state = "🟢 Stable Abundance"
else:
    flow_state = "🟡 Disturbed Abundance"

# Output
st.header("System Output")

st.subheader("Flow State")
st.write(flow_state)
