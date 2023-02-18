from typing import Optional
from random import choice

import streamlit as st

from src.bomb import Bomb, BombState


def create_bomb():
    st.session_state.bomb = Bomb()


if 'bomb' not in st.session_state:
    st.session_state.bomb = None
bomb: Optional[Bomb] = st.session_state.bomb

start_button = st.button(label='Restart!' if bomb else 'Start!', on_click=create_bomb)


if bomb:
    bomb.check_if_exploded()

    info_link = 'Look at this! ' + r'https://github.com/KingAArtur/text-ktane/blob/master/manual.md'
    info_strikes = f'{bomb.strikes} / {bomb.max_strikes} strikes'
    info_time = f'{bomb.get_remaining_time():.1f} seconds'
    info_result = '**[Solved!]**' if bomb.state == BombState.SOLVED else (
        '**[Exploded!]**' if bomb.state == BombState.EXPLODED else ''
    )

    with st.sidebar:
        st.write(info_strikes)
        st.write(info_time)
        st.write(info_result)

    st.write(info_link)
    refresh_button = st.button(label='Refresh time')

    for i, module in enumerate(bomb.modules):
        module_title = '**[OK!]**' if module.disarmed else ''
        with st.expander(label=module_title, expanded=True):
            module_text = module.show()
            guess = st.text_input(label=module_text, key=i).strip()
            st.button(label='Guess!', key=-1 - i, on_click=bomb.guess, args=(module, guess))

    if bomb.state == BombState.EXPLODED:
        st.write('Congratulations! You successfully blew yourself up!')
    elif bomb.state == BombState.SOLVED:
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
        st.write(s)
