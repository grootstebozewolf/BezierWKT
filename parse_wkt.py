# parse_wkt.py

from antlr4 import InputStream, CommonTokenStream
from wkt_parser.wktLexer import wktLexer
from wkt_parser.wktParser import wktParser
from wkt_visitor import WKTVisitor

def parse_wkt(wkt_string):
    input_stream = InputStream(wkt_string)
    lexer = wktLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = wktParser(stream)
    tree = parser.geometry()
    visitor = WKTVisitor()
    result = visitor.visit(tree)
    return result

# Example usage
if __name__ == "__main__":
    wkt_input = 'CIRCULARSTRING (1 0, 0 1, -1 0)'
    geometry_data = parse_wkt(wkt_input)
    print(geometry_data)
