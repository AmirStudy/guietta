# -*- coding: utf-8 -*-

from guietta import B,  _, Gui, Quit

gui = Gui(
    
  [  'Enter expression:', '__expr__'  , B('Eval!') ],
  [  'Result:'          , 'result'    , _          ],
  [  _                  , _           , Quit       ] )

while True:
    name, signal, *args = gui.get()

    if name == 'Eval':
        try:
            result = eval(gui.expr.text())
            gui.result.setText(str(result))
        except Exception as e:
            gui.result.setText('Error: '+str(e))

    elif name == None:
        break

