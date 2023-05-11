from py_asciimath.translator.translator import ASCIIMath2MathML

if __name__ == "__main__":
    asciimath2mathml = ASCIIMath2MathML(log=False, inplace=True)
    parsed = asciimath2mathml.translate(
        r"e^x > 0 forall x in RR",
        displaystyle=True,
        dtd="mathml2",
        dtd_validation=True,
        from_file=False,
        output="string",
        network=True,
        pprint=False,
        to_file=None,
        xml_declaration=False,
        xml_pprint=False,
    )

    print(parsed)
