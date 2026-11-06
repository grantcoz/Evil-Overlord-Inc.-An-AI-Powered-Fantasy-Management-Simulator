"""Run with: streamlit run scene_demo.py"""
import streamlit as st
from ui.scenes import render_scene

st.set_page_config(page_title='Evil Overlord Inc.', layout='wide')
st.title('Evil Overlord Inc. — Wizard’s Tower')
st.image(
    render_scene(x_position=0.01),
    use_container_width=True,
)
st.subheader('Archibald')
st.write('Ah, my new Overlord! What brings you to my humble tower?')
choice = st.selectbox('Ask Archibald', ['Tell me about the crown heist.', 'What happened to the Dark Lord?', 'Can you help with magic?'])
if st.button('Ask'):
    replies = {
        'Tell me about the crown heist.': 'A crown? A simple matter! Provided the guards are not immune to frogs.',
        'What happened to the Dark Lord?': 'A mystery! I have seventeen theories. Only three contradict each other directly.',
        'Can you help with magic?': 'Certainly! I merely require a laboratory, a wand, and a legally binding waiver.'
    }
    st.info(replies[choice])
