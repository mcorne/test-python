from py_asciimath.translator.translator import ASCIIMath2MathML

# python main.py > test.html

asciiml = """
a(z) = 1/(1 + e^(-z))
"""
mathml = ""
for line in asciiml.strip().splitlines():
    if mathml:
        mathml += "<br>\n"
    mathml += f"<!-- {line} -->\n"
    mathml += ASCIIMath2MathML().translate(line, displaystyle=True, xml_pprint=False)
print(mathml.strip())
