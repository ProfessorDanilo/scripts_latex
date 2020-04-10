# TeXworksScript
# Title: Graph
# Shortcut: Ctrl+Shift+g
# Description: 
# Author: danilo
# Version: 0.1
# Date: 2016
# Script-Type: standalone
# Context: TeXDocument

txt = TW.target.selection
if txt == None:
	txt = ""
TW.target.insertText("\\begin{figure}[!h]\\centering\\includegraphics[scale=0.7]{aula/fig.pdf}\\caption{titulo}\\end{figure}")
TW.target.selectRange(TW.target.selectionStart - len(txt) - 33, len(txt))
