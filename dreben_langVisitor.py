# Generated from dreben_lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .dreben_langParser import dreben_langParser
else:
    from dreben_langParser import dreben_langParser

# This class defines a complete generic visitor for a parse tree produced by dreben_langParser.

class dreben_langVisitor(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}

    # def visit(self, tree):
    #     print(f"Visiting node: {type(tree).__name__}")
    #     return super().visit(tree)

    # Visit a parse tree produced by dreben_langParser#program.
    def visitProgram(self, ctx:dreben_langParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dreben_langParser#stmt.
    def visitStmt(self, ctx:dreben_langParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dreben_langParser#stringExpr.
    def visitStringExpr(self, ctx:dreben_langParser.StringExprContext):
        return ctx.STRING().getText()[1:-1]  # Remove surrounding quotes


    # Visit a parse tree produced by dreben_langParser#idExp.
    def visitIdExp(self, ctx:dreben_langParser.IdExpContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        else:
            raise NameError(f"Променливата '{var_name}' не е определена")

    # Visit a parse tree produced by dreben_langParser#compExpr.
    def visitCompExpr(self, ctx:dreben_langParser.CompExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = self.visit(ctx.compOperator())
        if operator == "е по-малко от":
            return left < right
        elif operator == "е по-малко или равно от":
            return left <= right
        elif operator == "е равно на":
            return left == right
        elif operator == "НЕ е равно на":
            return left != right
        elif operator == "е по-голямо от":
            return left > right
        elif operator == "е по-голямо или равно от":
            return left >= right
        else:
            raise ValueError(f"Неизвестен оператор за сравняване: {operator}")


    # Visit a parse tree produced by dreben_langParser#plusMinusExpr.
    def visitPlusMinusExpr(self, ctx:dreben_langParser.PlusMinusExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = ctx.op.text
        if operator == "плюс":
            return left + right
        elif operator == "минус":
            return left - right


    # Visit a parse tree produced by dreben_langParser#boolExpr.
    def visitBoolExpr(self, ctx:dreben_langParser.BoolExprContext):
        return ctx.getText() == "Истина"


    # Visit a parse tree produced by dreben_langParser#parenthesisExpr.
    def visitParenthesisExpr(self, ctx:dreben_langParser.ParenthesisExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by dreben_langParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:dreben_langParser.MulDivExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        operator = ctx.getChild(1).getText()
        if operator == "по":
            return left * right
        elif operator == "делено на":
            return left // right


    # Visit a parse tree produced by dreben_langParser#numExpr.
    def visitNumExpr(self, ctx:dreben_langParser.NumExprContext):
        return int(ctx.NUM().getText())


    # Visit a parse tree produced by dreben_langParser#varDecl.
    def visitVarDecl(self, ctx:dreben_langParser.VarDeclContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            raise NameError(f"Променливата '{var_name}' вече е декларирана")
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return value


    # Visit a parse tree produced by dreben_langParser#assignment.
    def visitAssignment(self, ctx:dreben_langParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return value


    # Visit a parse tree produced by dreben_langParser#compOperator.
    def visitCompOperator(self, ctx:dreben_langParser.CompOperatorContext):
        return ctx.op.text


    # Visit a parse tree produced by dreben_langParser#print.
    def visitPrint(self, ctx:dreben_langParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return value


    # Visit a parse tree produced by dreben_langParser#blockstmt.
    def visitBlockstmt(self, ctx:dreben_langParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dreben_langParser#ifstmt.
    def visitIfstmt(self, ctx:dreben_langParser.IfstmtContext):
        condition = self.visit(ctx.expr())
        if condition:
            self.visit(ctx.stmt())
        elif ctx.elsestmt():
            self.visit(ctx.elsestmt())


    # Visit a parse tree produced by dreben_langParser#elsestmt.
    def visitElsestmt(self, ctx:dreben_langParser.ElsestmtContext):
        self.visit(ctx.stmt())


    # Visit a parse tree produced by dreben_langParser#whilestmt.
    def visitWhilestmt(self, ctx:dreben_langParser.WhilestmtContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmt())


del dreben_langParser