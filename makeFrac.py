# TeXworksScript
# Title: Frac
# Shortcut: Ctrl+Shift+f
# Description: 
# Author: danilo
# Version: 0.1
# Date: 2016
# Script-Type: standalone
# Context: TeXDocument

txt = TW.target.selection
if txt == None:
	txt = ""
TW.target.insertText("\\frac{" + txt + "}{}")
TW.target.selectRange(TW.target.selectionStart - len(txt) - 3, len(txt))
