import streamlit as st

# App title
st.set_page_config(page_title="Mood Measurement")

# Sidebar for Mood Measurement
st.sidebar.title("Mood Measurement")
st.sidebar.write("Please rate your mood on a scale from 1 to 10.")

# Mood sliders
mood_slider_1 = st.sidebar.slider("Mood 1", min_value=1, max_value=10, value=5)
mood_slider_2 = st.sidebar.slider("Mood 2", min_value=1, max_value=10, value=5)

# Display average mood
average_mood = (mood_slider_1 + mood_slider_2) / 2
st.sidebar.subheader("Average Mood")
st.sidebar.write(f"The average mood is {average_mood:.1f}")

# Display mood interpretation
st.sidebar.subheader("Mood Interpretation")
if average_mood <= 3:
    st.sidebar.write("Feeling low. Reach out for support.")
elif 3 < average_mood <= 7:
    st.sidebar.write("Feeling okay, but there's room for improvement.")
else:
    st.sidebar.write("Feeling great! Keep up the positive vibes!")

# Main content
st.title("Mood Measurement App")
st.write("Use the sidebars to measure and interpret your mood.")
