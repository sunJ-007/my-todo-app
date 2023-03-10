import streamlit as sl
import functions
todos = functions.get_todos()

def add_todo():
    todo = sl.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

sl.title('My Todo App')
sl.subheader('This is my todo app')

for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sl.session_state[todo]


sl.text_input(label='', placeholder='Add new todo',
              on_change=add_todo, key='new_todo')
print('hello')
