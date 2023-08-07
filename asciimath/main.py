from py_asciimath.translator.translator import ASCIIMath2MathML

# python main.py > test.html

asciiml = """
(del L)/(del w_1) = 1/m sum_(i=1)^m (a_i - y_i)x_1
(del L)/(del w_2) = 1/m sum_(i=1)^m (a_i - y_i)x_2
(del L)/(del b)   = 1/m sum_(i=1)^m (a_i - y_i)
"""
mathml = ""
for line in asciiml.strip().splitlines():
    if mathml:
        mathml += "<br>\n"
    mathml += f"<!-- {line} -->\n"
    mathml += ASCIIMath2MathML().translate(line, displaystyle=True, xml_pprint=False)

mathml = mathml.replace("<mtable>", '<mtable columnalign="left">')
mathml = mathml.replace("<msubsup><mrow><mo>", "<munderover><mrow><mo>")
mathml = mathml.replace("</mi></mrow></msubsup>", "</mi></mrow></munderover>")
print(mathml.strip())
