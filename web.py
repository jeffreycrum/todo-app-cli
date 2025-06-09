import streamlit as st
import util

todos = util.read_todos()

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add a new todo...")


print("Hello")