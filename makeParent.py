# TeXworksScript
# Title: Parentesis
# Shortcut: Ctrl+Shift+p
# Description: 
# Author: danilo
# Version: 0.1
# Date: 2016
# Script-Type: standalone
# Context: TeXDocument

txt = TW.target.selection
if txt == None:
	txt = ""
TW.target.insertText("\\left(" + txt +"\\right)")
TW.target.selectRange(TW.target.selectionStart - len(txt) - 1, len(txt))
