# Generated from dreben_lang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,48,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,60,8,2,10,2,12,2,63,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,5,7,84,8,7,10,7,12,7,
        87,9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,97,8,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,0,1,4,11,0,2,4,6,8,10,12,14,16,18,20,0,3,
        1,0,14,15,1,0,16,17,1,0,19,24,109,0,25,1,0,0,0,2,36,1,0,0,0,4,47,
        1,0,0,0,6,64,1,0,0,0,8,70,1,0,0,0,10,75,1,0,0,0,12,77,1,0,0,0,14,
        81,1,0,0,0,16,90,1,0,0,0,18,98,1,0,0,0,20,101,1,0,0,0,22,24,3,2,
        1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,
        1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,37,3,6,3,0,31,
        37,3,8,4,0,32,37,3,12,6,0,33,37,3,16,8,0,34,37,3,14,7,0,35,37,3,
        20,10,0,36,30,1,0,0,0,36,31,1,0,0,0,36,32,1,0,0,0,36,33,1,0,0,0,
        36,34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,6,2,-1,0,39,40,5,
        1,0,0,40,41,3,4,2,0,41,42,5,2,0,0,42,48,1,0,0,0,43,48,5,25,0,0,44,
        48,5,26,0,0,45,48,5,27,0,0,46,48,5,28,0,0,47,38,1,0,0,0,47,43,1,
        0,0,0,47,44,1,0,0,0,47,45,1,0,0,0,47,46,1,0,0,0,48,61,1,0,0,0,49,
        50,10,7,0,0,50,51,7,0,0,0,51,60,3,4,2,8,52,53,10,6,0,0,53,54,7,1,
        0,0,54,60,3,4,2,7,55,56,10,5,0,0,56,57,3,10,5,0,57,58,3,4,2,6,58,
        60,1,0,0,0,59,49,1,0,0,0,59,52,1,0,0,0,59,55,1,0,0,0,60,63,1,0,0,
        0,61,59,1,0,0,0,61,62,1,0,0,0,62,5,1,0,0,0,63,61,1,0,0,0,64,65,5,
        3,0,0,65,66,5,26,0,0,66,67,5,4,0,0,67,68,3,4,2,0,68,69,5,5,0,0,69,
        7,1,0,0,0,70,71,5,26,0,0,71,72,5,18,0,0,72,73,3,4,2,0,73,74,5,5,
        0,0,74,9,1,0,0,0,75,76,7,2,0,0,76,11,1,0,0,0,77,78,5,6,0,0,78,79,
        3,4,2,0,79,80,5,5,0,0,80,13,1,0,0,0,81,85,5,7,0,0,82,84,3,2,1,0,
        83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,
        0,0,0,87,85,1,0,0,0,88,89,5,8,0,0,89,15,1,0,0,0,90,91,5,9,0,0,91,
        92,5,10,0,0,92,93,3,4,2,0,93,94,5,11,0,0,94,96,3,2,1,0,95,97,3,18,
        9,0,96,95,1,0,0,0,96,97,1,0,0,0,97,17,1,0,0,0,98,99,5,12,0,0,99,
        100,3,2,1,0,100,19,1,0,0,0,101,102,5,13,0,0,102,103,3,4,2,0,103,
        104,3,2,1,0,104,21,1,0,0,0,7,25,36,47,59,61,85,96
    ]

class dreben_langParser ( Parser ):

    grammarFileName = "dreben_lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\u041F\\u0440\\u043E\\u043C\\u0435\\u043D\\u043B\\u0438\\u0432\\u0430'", 
                     "'\\u0440\\u0430\\u0432\\u043D\\u0430'", "';'", "'\\u041F\\u043E\\u043A\\u0430\\u0436\\u0438'", 
                     "'{'", "'}'", "'\\u0410\\u043A\\u043E'", "'\\u201E'", 
                     "'\\u201C'", "'\\u0418\\u043D\\u0430\\u0447\\u0435'", 
                     "'\\u0414\\u043E\\u043A\\u0430\\u0442\\u043E'", "'\\u043F\\u043E'", 
                     "'\\u0434\\u0435\\u043B\\u0435\\u043D\\u043E \\u043D\\u0430'", 
                     "'\\u043F\\u043B\\u044E\\u0441'", "'\\u043C\\u0438\\u043D\\u0443\\u0441'", 
                     "'\\u0440\\u0430\\u0432\\u043D\\u043E'", "'\\u0435 \\u0440\\u0430\\u0432\\u043D\\u043E \\u043D\\u0430'", 
                     "'\\u041D\\u0415 \\u0435 \\u0440\\u0430\\u0432\\u043D\\u043E \\u043D\\u0430'", 
                     "'\\u0435 \\u043F\\u043E-\\u043C\\u0430\\u043B\\u043A\\u043E \\u043E\\u0442'", 
                     "'\\u0435 \\u043F\\u043E-\\u043C\\u0430\\u043B\\u043A\\u043E \\u0438\\u043B\\u0438 \\u0440\\u0430\\u0432\\u043D\\u043E \\u043E\\u0442'", 
                     "'\\u0435 \\u043F\\u043E-\\u0433\\u043E\\u043B\\u044F\\u043C\\u043E \\u043E\\u0442'", 
                     "'\\u0435 \\u043F\\u043E-\\u0433\\u043E\\u043B\\u044F\\u043C\\u043E \\u0438\\u043B\\u0438 \\u0440\\u0430\\u0432\\u043D\\u043E \\u043E\\u0442'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ASTERISK", "SLASH", "PLUS", 
                      "MINUS", "ASSIGN", "EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", 
                      "GREATER", "GREATER_OR_EQUAL", "BOOL", "ID", "NUM", 
                      "STRING", "LINE_COMMENT", "COMMENT", "SPACE" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_varDecl = 3
    RULE_assignment = 4
    RULE_compOperator = 5
    RULE_print = 6
    RULE_blockstmt = 7
    RULE_ifstmt = 8
    RULE_elsestmt = 9
    RULE_whilestmt = 10

    ruleNames =  [ "program", "stmt", "expr", "varDecl", "assignment", "compOperator", 
                   "print", "blockstmt", "ifstmt", "elsestmt", "whilestmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    ASTERISK=14
    SLASH=15
    PLUS=16
    MINUS=17
    ASSIGN=18
    EQUAL=19
    NOT_EQUAL=20
    LESS=21
    LESS_OR_EQUAL=22
    GREATER=23
    GREATER_OR_EQUAL=24
    BOOL=25
    ID=26
    NUM=27
    STRING=28
    LINE_COMMENT=29
    COMMENT=30
    SPACE=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(dreben_langParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dreben_langParser.StmtContext)
            else:
                return self.getTypedRuleContext(dreben_langParser.StmtContext,i)


        def getRuleIndex(self):
            return dreben_langParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = dreben_langParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67117768) != 0):
                self.state = 22
                self.stmt()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(dreben_langParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(dreben_langParser.VarDeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(dreben_langParser.AssignmentContext,0)


        def print_(self):
            return self.getTypedRuleContext(dreben_langParser.PrintContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(dreben_langParser.IfstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(dreben_langParser.BlockstmtContext,0)


        def whilestmt(self):
            return self.getTypedRuleContext(dreben_langParser.WhilestmtContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = dreben_langParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.varDecl()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.assignment()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.print_()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.ifstmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.blockstmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.whilestmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return dreben_langParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(dreben_langParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(dreben_langParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExp" ):
                return visitor.visitIdExp(self)
            else:
                return visitor.visitChildren(self)


    class CompExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def compOperator(self):
            return self.getTypedRuleContext(dreben_langParser.CompOperatorContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dreben_langParser.ExprContext)
            else:
                return self.getTypedRuleContext(dreben_langParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompExpr" ):
                return visitor.visitCompExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dreben_langParser.ExprContext)
            else:
                return self.getTypedRuleContext(dreben_langParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(dreben_langParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(dreben_langParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusMinusExpr" ):
                return visitor.visitPlusMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(dreben_langParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisExpr" ):
                return visitor.visitParenthesisExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dreben_langParser.ExprContext)
            else:
                return self.getTypedRuleContext(dreben_langParser.ExprContext,i)

        def ASTERISK(self):
            return self.getToken(dreben_langParser.ASTERISK, 0)
        def SLASH(self):
            return self.getToken(dreben_langParser.SLASH, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a dreben_langParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(dreben_langParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumExpr" ):
                return visitor.visitNumExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = dreben_langParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = dreben_langParser.ParenthesisExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 39
                self.match(dreben_langParser.T__0)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(dreben_langParser.T__1)
                pass
            elif token in [25]:
                localctx = dreben_langParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(dreben_langParser.BOOL)
                pass
            elif token in [26]:
                localctx = dreben_langParser.IdExpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(dreben_langParser.ID)
                pass
            elif token in [27]:
                localctx = dreben_langParser.NumExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(dreben_langParser.NUM)
                pass
            elif token in [28]:
                localctx = dreben_langParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(dreben_langParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = dreben_langParser.MulDivExprContext(self, dreben_langParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = dreben_langParser.PlusMinusExprContext(self, dreben_langParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = dreben_langParser.CompExprContext(self, dreben_langParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        self.compOperator()
                        self.state = 57
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(dreben_langParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = dreben_langParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(dreben_langParser.T__2)
            self.state = 65
            self.match(dreben_langParser.ID)
            self.state = 66
            self.match(dreben_langParser.T__3)
            self.state = 67
            self.expr(0)
            self.state = 68
            self.match(dreben_langParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(dreben_langParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(dreben_langParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = dreben_langParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(dreben_langParser.ID)
            self.state = 71
            self.match(dreben_langParser.ASSIGN)
            self.state = 72
            self.expr(0)
            self.state = 73
            self.match(dreben_langParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def LESS(self):
            return self.getToken(dreben_langParser.LESS, 0)

        def LESS_OR_EQUAL(self):
            return self.getToken(dreben_langParser.LESS_OR_EQUAL, 0)

        def EQUAL(self):
            return self.getToken(dreben_langParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(dreben_langParser.NOT_EQUAL, 0)

        def GREATER(self):
            return self.getToken(dreben_langParser.GREATER, 0)

        def GREATER_OR_EQUAL(self):
            return self.getToken(dreben_langParser.GREATER_OR_EQUAL, 0)

        def getRuleIndex(self):
            return dreben_langParser.RULE_compOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOperator" ):
                return visitor.visitCompOperator(self)
            else:
                return visitor.visitChildren(self)




    def compOperator(self):

        localctx = dreben_langParser.CompOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33030144) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_print

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = dreben_langParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(dreben_langParser.T__5)
            self.state = 78
            self.expr(0)
            self.state = 79
            self.match(dreben_langParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(dreben_langParser.StmtContext)
            else:
                return self.getTypedRuleContext(dreben_langParser.StmtContext,i)


        def getRuleIndex(self):
            return dreben_langParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = dreben_langParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(dreben_langParser.T__6)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67117768) != 0):
                self.state = 82
                self.stmt()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(dreben_langParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(dreben_langParser.StmtContext,0)


        def elsestmt(self):
            return self.getTypedRuleContext(dreben_langParser.ElsestmtContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = dreben_langParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(dreben_langParser.T__8)
            self.state = 91
            self.match(dreben_langParser.T__9)
            self.state = 92
            self.expr(0)
            self.state = 93
            self.match(dreben_langParser.T__10)
            self.state = 94
            self.stmt()
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 95
                self.elsestmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(dreben_langParser.StmtContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_elsestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




    def elsestmt(self):

        localctx = dreben_langParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(dreben_langParser.T__11)
            self.state = 99
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(dreben_langParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(dreben_langParser.StmtContext,0)


        def getRuleIndex(self):
            return dreben_langParser.RULE_whilestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhilestmt" ):
                return visitor.visitWhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def whilestmt(self):

        localctx = dreben_langParser.WhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whilestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(dreben_langParser.T__12)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




