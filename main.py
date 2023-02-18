import streamlit as st
from typing import Optional
from random import choice

from src.bomb import Bomb


def create_bomb():
    st.session_state.bomb = Bomb()


start_button = st.button(label='Start!', on_click=create_bomb)

if 'bomb' not in st.session_state:
    st.session_state.bomb = None

bomb: Optional[Bomb] = st.session_state.bomb
if bomb:
    st.write(f'{bomb.strikes} / {bomb.max_strikes} strikes, {bomb.get_remaining_time()} seconds')

    for i, module in enumerate(bomb.modules):
        module_text = module.show()
        guess = st.text_input(label=('[OK!] ' if module.disarmed else '') + module_text, key=i)
        st.button(label='Guess!', key=-1 - i, on_click=bomb.guess, args=(module, guess))

    if bomb.exploded:
        st.write('Congratulations! You successfully blew yourself up!')
    elif bomb.solved:
        st.write('Congratulations! Unfortunately, you successfully solved the bomb!')
        st.write('If you are DAVID:')
        st.write('    Happy birthday, DAVID!')
    else:
        s = choice(
            [
                'Just solve this freaking bomb!',
                'Dude, why this bomb is still not solved?',
                'David mox',
                'I am pretty sure you will lose with guesses like that'
            ]
        )
