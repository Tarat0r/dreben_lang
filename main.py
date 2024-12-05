#!./myenv/bin/python3
import sys
import argparse
from antlr4 import *
from dreben_langLexer import dreben_langLexer
from dreben_langParser import dreben_langParser
from dreben_langVisitor import dreben_langVisitor
from dreben_langVisitorComp import dreben_langVisitorComp

# Аргументи
parser = argparse.ArgumentParser(description="Интерпретатор и компилатор на dreben_lang в триадресен код.")
parser.add_argument("input_file", help="Въвеждане на файл с изходния код на програмата")
parser.add_argument("-c", "--compile", help="Изходен файл за съхраняване на триадресения код", metavar="OUTPUT_FILE")
parser.add_argument("-v", "--verbose", action="store_true", help="Включване на подробен резултат")
args = parser.parse_args()


with open(args.input_file, "r", encoding="utf-8") as file:
    input_code = file.read()

lexer = dreben_langLexer(InputStream(input_code))
stream = CommonTokenStream(lexer)
parser = dreben_langParser(stream)
tree = parser.program()

if args.verbose:
    print(tree.toStringTree(recog=parser))


if args.compile:
    tac = dreben_langVisitorComp().visit(tree)

    with open(args.compile, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(tac))
        output_file.write("\n")
        print(f"Триадресеният код е готов и съхранен в {args.compile}")
 
    if args.verbose:
        for line in tac:
            print(line)
else:
    try:
        print()
        dreben_langVisitor().visit(tree)
    except Exception as e:
        print(f"Грешка при изпълняването: {e}")