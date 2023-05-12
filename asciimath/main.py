from py_asciimath.translator.translator import ASCIIMath2MathML

# python main.py > test.html

asciiml = """
(del L)/(del a) = -1/m sum_(i=1)^m y_i/a_i - (1 - y_i)/(1 - a_i)
 = -1/m sum_(i=1)^m (y_i(1 - a_i) - (1 - y_i)a_i)/(a_i(1 - a_i))
 = -1/m sum_(i=1)^m (y_i - a_i) / (a_i(1 - a_i))
"""
mathml = ""
for line in asciiml.strip().splitlines():
    mathml += f"<!-- {line} -->\n"
    mathml += "<div>" + ASCIIMath2MathML().translate(line, displaystyle=True, xml_pprint=False) + "</div>\n"
print(mathml)
