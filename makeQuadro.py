# TeXworksScript
# Title: Quadro
# Shortcut: Ctrl+Shift+q
# Description: 
# Author: danilo
# Version: 0.1
# Date: 2016
# Script-Type: standalone
# Context: TeXDocument

txt = TW.target.selection
if txt == None:
	txt = ""
TW.target.insertText("\\begin{center}{Q. 01 -- TITULO}\\end{center}\\framebox(270,100){}")
TW.target.selectRange(TW.target.selectionStart - len(txt) - 1, len(txt))
