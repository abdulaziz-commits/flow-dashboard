Synchronization", ["Full", "Partial", "None"])

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
