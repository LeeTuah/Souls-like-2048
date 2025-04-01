import time
import os
import pygame.mixer as mixer

mixer.init()
mixer.music.load('intro_sound_2048.MP3')

python = """
    py py py py py py p     py py py                           py py py   
    py py py       py py       py py py                     py py py 
    py py py          py p        py py py               py py py 
    py py py          py p           py py py         py py py 
    py py py       py py                py py py    py py py 
    py py py py py py p                  y py py py py py p
    py py py py py p                       py py py py py   
    py py py p                              y py py py p
    py py py                                  py py py 
    py py py                                  py py py 
    py py py                                  py py py 
    py py py                                  py py py 
    py py py                                  py py py 
    py py py                                  py py py  
"""

lee = """
    lee lee lee                            lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee                            lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee                            lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee                            lee lee lee                              lee lee lee
    lee lee lee                            lee lee lee                              lee lee lee
    lee lee lee                            lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee                            lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee                            lee lee lee                              lee lee lee
    lee lee lee lee lee lee lee lee lee    lee lee lee                              lee lee lee
    lee lee lee lee lee lee lee lee lee    lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee 
    lee lee lee lee lee lee lee lee lee    lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
    lee lee lee lee lee lee lee lee lee    lee lee lee lee lee lee lee lee lee      lee lee lee lee lee lee lee lee lee
"""

deb = """
    deb deb deb deb d                deb deb deb deb deb deb deb deb deb    deb deb deb deb deb deb de
    deb deb  eb deb deb d            deb deb deb deb deb deb deb deb deb    deb deb deb     deb deb deb d
    deb deb      eb deb deb d        deb deb deb deb deb deb deb deb deb    deb deb deb         deb deb de  
    deb deb           b deb deb      deb deb deb                            deb deb deb             deb deb 
    deb deb              eb deb d    deb deb deb                            deb deb deb             deb de  
    deb deb               b deb de   deb deb deb deb deb deb deb deb deb    deb deb deb     deb deb deb d   
    deb deb               b deb de   deb deb deb deb deb deb deb deb deb    deb deb deb deb deb deb d 
    deb deb              eb deb d    deb deb deb                            deb deb deb     deb deb deb d
    deb deb             deb deb      deb deb deb                            deb deb deb         deb deb de
    deb deb           b deb de       deb deb deb deb deb deb deb deb deb    deb deb deb             deb deb
    deb deb      eb deb deb d        deb deb deb deb deb deb deb deb deb    deb deb deb         deb deb de
    deb deb  eb deb deb d            deb deb deb deb deb deb deb deb deb    deb deb deb     deb deb deb d    
    deb deb deb deb d                deb deb deb deb deb deb deb deb deb    deb deb deb deb deb deb de
"""

game_over_text = """
        g g g g g               a a a a a a           m m m m           m m m m    e e e e e e e e e e 
      g g g   g g g            a a a a a a a          m m m m m       m m m m m    e e e e e e e e e e 
    g g g       g g g         a a a     a a a         m m m   m m   m m   m m m    e e e 
    g g g                    a a a       a a a        m m m     m m m     m m m    e e e 
    g g g                   a a a a a a a a a a       m m m       m       m m m    e e e e e e e e e e 
    g g g     g g g g      a a a a a a a a a a a      m m m               m m m    e e e 
      g g g g g   g g     a a a             a a a     m m m               m m m    e e e 
        g g g g   g g    a a a               a a a    m m m               m m m    e e e e e e e e e e 
          g g     g g   a a a                 a a a   m m m               m m m    e e e e e e e e e e 


        o o o o o       v v v               v v v    e e e e e e e e e e    r r r r r 
      o o o   o o o      v v v             v v v     e e e e e e e e e e    r r r   r r 
    o o o       o o o     v v v           v v v      e e e                  r r r     r r 
    o o           o o      v v v         v v v       e e e                  r r r   r r 
    o               o       v v v       v v v        e e e e e e e e e e    r r r r r 
    o o           o o        v v v     v v v         e e e                  r r r r r r   
    o o o       o o o         v v v   v v v          e e e                  r r r   r r r 
      o o o   o o o            v v v v v v           e e e e e e e e e e    r r r     r r r 
        o o o o o               v v v v v            e e e e e e e e e e    r r r       r r r 
"""

gg = """
        g g g g g             g g g g g 
      g g g   g g g         g g g   g g g 
    g g g       g g g     g g g       g g g 
    g g g                 g g g 
    g g g                 g g g 
    g g g     g g g g     g g g     g g g g  
      g g g g g   g g       g g g g g   g g 
        g g g g   g g         g g g g   g g 
          g g     g g           g g     g g s
"""

sword = """
 __-----_________________{]__________________________________________________
{&&&&&&&#%%&#%&%&%&%&%#%&|]__________________________________________________\\
                         {]

                            2 2 2 2                         0 0 0 0
                        2 2 2   2 2 2 2                   0 0 0 0 0 0
                      2 2 2       2 2 2 2               0 0 0     0 0 0
                                2 2 2 2               0 0 0         0 0 0
                              2 2 2 2               0 0 0             0 0 0
                            2 2 2 2               0 0 0                 0 0 0 
                          2 2 2 2                 0 0 0                 0 0 0
                        2 2 2 2                     0 0 0             0 0 0
                      2 2 2 2 2 2 2                   0 0 0         0 0 0 
                    2 2 2 2 2 2 2 2 2                   0 0 0     0 0 0 
                    2 2 2 2 2 2 2 2 2 2                   0 0 0 0 0 0 
                      2 2 2 2 2 2 2 2 2                     0 0 0 0 


                    4 4 4 4       4 4 4 4 4                 8 8 8 8 
                    4 4 4 4       4 4 4 4 4               8 8     8 8 
                    4 4 4 4       4 4 4 4 4             8 8         8 8 
                    4 4 4 4       4 4 4 4 4           8 8             8 8 
                    4 4 4 4       4 4 4 4 4             8 8         8 8 
                    4 4 4 4 4 4 4 4 4 4 4 4               8 8     8 8 
                      4 4 4 4 4 4 4 4 4 4 4                 8 8 8 8 
                        4 4 4 4 4 4 4 4 4 4               8 8     8 8 
                                  4 4 4 4 4             8 8         8 8 
                                  4 4 4 4 4           8 8             8 8 
                                  4 4 4 4 4         8 8                 8 8 
                                  4 4 4 4 4           8 8             8 8 
                                  4 4 4 4 4             8 8         8 8 
                                  4 4 4 4 4               8 8 8 8 8 8 

                        .______________________________________________________|_._._._._._._._._._.
                        \\______________________________________________________|_#_#_#_#_#_#_#_#_#_|
                                                                               l

"""

def slow_print(text, delay=50):
    for i in text:
        print(end=i, flush=True)
        time.sleep(delay/1000)

def clear():
    os.system('cls')

def intro_screen():
    mixer.music.play()
    clear()
    slow_print('Made in...', 200)
    slow_print(python, 7)
    time.sleep(2.5)

    clear()
    slow_print('An original product of....', 120)
    slow_print(lee, 4)
    time.sleep(1)

    clear()
    slow_print('And....', 250)
    slow_print(deb, 4)
    slow_print('##### ###### living at ######, ########## with IP Address ###.###.###.###\n', 45)
    slow_print('who is the 5th runner-up for Jerkmate Champion League 2024, and a notorious nutter.', 45)
    time.sleep(1)

    clear()
    slow_print(sword, 0.5)
    print('\n\nPress any key to start the game....')

if __name__ == '__main__':
    intro_screen()
