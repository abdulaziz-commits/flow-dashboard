# -------------------
# LEADERSHIP MODE
# -------------------
st.header("Leadership Mode")

lead_summary = (
    f"The system '{system}' is currently assessed at the '{flow_state}' level "
    f"during the '{stage}' stage. The main issue identified is '{constraint}'."
)

if constraint == "No Constraint":
    strategic_note = (
        "The system is functioning within acceptable parameters. "
        "The priority is to preserve continuity, maintain synchronization, "
        "and monitor for early signs of degradation."
    )
elif "Multiplicity" in constraint:
    strategic_note = (
        "The system is exposed to structural vulnerability due to limited alternatives. "
        "Its current configuration increases exposure to disruption if one path or source fails."
    )
elif "Synchronization" in constraint:
    strategic_note = (
        "The system is structurally present, but alignment across assets or decision layers is incomplete. "
        "This creates inefficiency, delay, and rising risk despite available capacity."
    )
else:
    strategic_note = (
        "The system is approaching critical instability and requires immediate executive attention."
    )

leader_recommendation = action

st.subheader("Executive Summary")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#111827;color:white;">
    {lead_summary}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.subheader("Strategic Note")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#374151;color:white;">
    {strategic_note}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

st.subheader("Leader Recommendation")
st.markdown(
    f"""
    <div style="padding:14px;border-radius:12px;background-color:#7c3aed;color:white;">
    {leader_recommendation}
    </div>
    """,
    unsafe_allow_html=True
)
