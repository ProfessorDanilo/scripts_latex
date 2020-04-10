# TeXworksScript
# Title: Targeta
# Shortcut: Ctrl+Shift+t
# Description: 
# Author: danilo
# Version: 0.1
# Date: 2016
# Script-Type: standalone
# Context: TeXDocument

txt = TW.target.selection
if txt == None:
	txt = ""
TW.target.insertText("\\begin{center}\\begin{tabular}{>{\\columncolor[gray]{.8}}c}\\multicolumn{1}{>{\\columncolor[gray]{.8}}p{9cm}}{\\centering \\textbf{TITULO}}\\end{tabular}\\end{center}")
TW.target.selectRange(TW.target.selectionStart - len(txt) - 1, len(txt))
