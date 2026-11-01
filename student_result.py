import streamlit as st

st.title("Student Result System")

s_name = st.text_input("Student Name")
enrollment = st.text_input("Enrollment No")

b_marks = st.number_input("BCQ Marks", min_value=0.0, max_value=70.0)
s_marks = st.number_input("SEQ Marks", min_value=0.0, max_value=30.0)
viva_marks = st.number_input("Viva Marks", min_value=0.0, max_value=100.0)
spe_marks = st.number_input("SPE Marks", min_value=0.0, max_value=100.0)
ca_marks = st.number_input("CA Marks", min_value=0.0, max_value=50.0)

if st.button("Calculate Result"):

    written_total = b_marks + s_marks
    practical_total = viva_marks + spe_marks

    adjusted_written = written_total / 100 * 85
    adjusted_practical = practical_total / 200 * 85

    grand_written = adjusted_written + ca_marks / 2
    grand_practical = adjusted_practical + ca_marks / 2
    grand_total = grand_written + grand_practical

    st.subheader("Student Result")

    st.write("Student Name:", s_name)
    st.write(f"Enrollment No: {enrollment}")
    st.write(f"Grand Written: {grand_written:.0f}")
    st.write(f"Grand Practical: {grand_practical:.0f}")
    st.write(f"Marks Obtained: {grand_total:.0f}")

    if grand_total >= 100 and grand_written >= 50 and grand_practical >= 50:
        st.success("PASS")
    else:
        st.error("FAIL")