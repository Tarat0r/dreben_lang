# Generated from dreben_lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .dreben_langParser import dreben_langParser
else:
    from dreben_langParser import dreben_langParser

# This class defines a complete generic visitor for a parse tree produced by dreben_langParser.

class dreben_langVisitorComp(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}
        self.temp_counter = 0
        self.label_counter = 0 
        self.tac = []

    def new_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"
    
    def new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"
        
    # def visit(self, tree):
    #     print(f"Visiting node: {type(tree).__name__}")
    #     return super().visit(tree)

    # Visit a parse tree produced by dreben_langParser#program.
    def visitProgram(self, ctx:dreben_langParser.ProgramContext):
        for stmt in ctx.stmt():
            self.visit(stmt)
        return self.tac



    # Visit a parse tree produced by dreben_langParser#stmt.
    def visitStmt(self, ctx:dreben_langParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dreben_langParser#stringExpr.
    def visitStringExpr(self, ctx:dreben_langParser.StringExprContext):
        string_value = ctx.STRING().getText()  
        temp = self.new_temp()  
        self.tac.append(f'{temp} = {string_value}')  
        return temp


    # Visit a parse tree produced by dreben_langParser#idExp.
    def visitIdExp(self, ctx:dreben_langParser.IdExpContext):
        return ctx.ID().getText()

    # Visit a parse tree produced by dreben_langParser#compExpr.
    def visitCompExpr(self, ctx:dreben_langParser.CompExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = self.visit(ctx.compOperator())
        temp = self.new_temp()
        if operator == "е по-малко от":
            self.tac.append(f"{temp} = {left} < {right}") 
        elif operator == "е по-малко или равно от":
            self.tac.append(f"{temp} = {left} <= {right}") 
        elif operator == "е равно на":
            self.tac.append(f"{temp} = {left} == {right}") 
        elif operator == "НЕ е равно на":
            self.tac.append(f"{temp} = {left} != {right}") 
        elif operator == "е по-голямо от":
            self.tac.append(f"{temp} = {left} > {right}") 
        elif operator == "е по-голямо или равно от":
            self.tac.append(f"{temp} = {left} >= {right}") 
        else:
            raise ValueError(f"Неизвестен оператор за сравняване: {operator}")
        return temp


    # Visit a parse tree produced by dreben_langParser#plusMinusExpr.
    def visitPlusMinusExpr(self, ctx:dreben_langParser.PlusMinusExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        temp = self.new_temp()
        operator = ctx.op.text
        if operator == "плюс":
            self.tac.append(f"{temp} = {left} + {right}")
        elif operator == "минус":
            self.tac.append(f"{temp} = {left} - {right}")
        return temp
        

    # Visit a parse tree produced by dreben_langParser#boolExpr.
    def visitBoolExpr(self, ctx:dreben_langParser.BoolExprContext):
        return ctx.getText() == "Истина"


    # Visit a parse tree produced by dreben_langParser#parenthesisExpr.
    def visitParenthesisExpr(self, ctx:dreben_langParser.ParenthesisExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by dreben_langParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:dreben_langParser.MulDivExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = ctx.getChild(1).getText()
        temp = self.new_temp()
        if operator == "по":
            self.tac.append(f"{temp} = {left} * {right}")
        elif operator == "делено на":
            self.tac.append(f"{temp} = {left} / {right}")
        return temp


    # Visit a parse tree produced by dreben_langParser#numExpr.
    def visitNumExpr(self, ctx:dreben_langParser.NumExprContext):
        return int(ctx.NUM().getText())


    # Visit a parse tree produced by dreben_langParser#varDecl.
    def visitVarDecl(self, ctx:dreben_langParser.VarDeclContext):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            raise NameError(f"Променливата '{var_name}' вече е декларирана")  # Double declaration error
        value = self.visit(ctx.expr())
        self.tac.append(f"{var_name} = {value}")


    # Visit a parse tree produced by dreben_langParser#assignment.
    def visitAssignment(self, ctx:dreben_langParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.tac.append(f"{var_name} = {value}")


    # Visit a parse tree produced by dreben_langParser#compOperator.
    def visitCompOperator(self, ctx:dreben_langParser.CompOperatorContext):
        return ctx.op.text


    # Visit a parse tree produced by dreben_langParser#print.
    def visitPrint(self, ctx:dreben_langParser.PrintContext):
        value = self.visit(ctx.expr())
        self.tac.append(f"print {value}") 


    # Visit a parse tree produced by dreben_langParser#blockstmt.
    def visitBlockstmt(self, ctx:dreben_langParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by dreben_langParser#ifstmt.
    def visitIfstmt(self, ctx:dreben_langParser.IfstmtContext):
           # Generate labels
        L1 = self.new_label()  # Label for the if block
        L2 = self.new_label()  # Label for the else block (or end of if)
        L3 = self.new_label() if ctx.elsestmt() else None  # End label if there's an else block

        condition = self.visit(ctx.expr())  # Visit comparison
        self.tac.append(f"if {condition} goto {L1}")
        self.tac.append(f"goto {L3 if ctx.elsestmt() else L2}")  # Skip to else or end if false

        # If block
        self.tac.append(f"{L1}:")
        self.visit(ctx.stmt())  # Visit the first block (if block)

        # Else block (if present)
        if ctx.elsestmt():
            self.tac.append(f"goto {L2}")  # Skip end of else block after executing 'if'
            self.tac.append(f"{L3}:")
            self.visit(ctx.elsestmt().stmt())  # Visit the 'else' block

        # End of if-else statement
        self.tac.append(f"{L2}:")


    # Visit a parse tree produced by dreben_langParser#elsestmt.
    def visitElsestmt(self, ctx:dreben_langParser.ElsestmtContext):
        self.visit(ctx.stmt())


    # Visit a parse tree produced by dreben_langParser#whilestmt.
    def visitWhilestmt(self, ctx:dreben_langParser.WhilestmtContext):
        # Generate labels
        L1 = self.new_label()  # Label for the start of the loop
        L2 = self.new_label()  # Label for the loop body
        L3 = self.new_label()  # Label for the end of the loop

        # Start of the loop
        self.tac.append(f"{L1}:")

        # Evaluate the condition
        condition = self.visit(ctx.expr())
        self.tac.append(f"if {condition} goto {L2}")  # If condition is true, jump to L2
        self.tac.append(f"goto {L3}")  # If false, exit the loop

        # Loop body
        self.tac.append(f"{L2}:")
        self.visit(ctx.stmt())  # Visit the loop body
        self.tac.append(f"goto {L1}")  # Jump back to the start of the loop

        # End of the loop
        self.tac.append(f"{L3}:")



del dreben_langParser