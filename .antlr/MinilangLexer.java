// Generated from /home/v/Documents/Университет/Магистър/1 Курс/Языки программирования/lab2/minilang.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MinilangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, ID=11, NUM=12, ASTERISK=13, SLASH=14, PLUS=15, MINUS=16, ASSIGN=17, 
		EQUAL=18, NOT_EQUAL=19, LESS=20, LESS_OR_EQUAL=21, GREATER=22, GREATER_OR_EQUAL=23, 
		SPACE=24, LINE_COMMENT=25;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "ID", "NUM", "ASTERISK", "SLASH", "PLUS", "MINUS", "ASSIGN", 
			"EQUAL", "NOT_EQUAL", "LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", 
			"SPACE", "LINE_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'var'", "';'", "'print'", "'{'", "'}'", "'if'", 
			"'else'", "'while'", null, null, "'*'", "'/'", "'+'", "'-'", "'='", "'=='", 
			"'!='", "'<'", "'<='", "'>'", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "ID", 
			"NUM", "ASTERISK", "SLASH", "PLUS", "MINUS", "ASSIGN", "EQUAL", "NOT_EQUAL", 
			"LESS", "LESS_OR_EQUAL", "GREATER", "GREATER_OR_EQUAL", "SPACE", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MinilangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "minilang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33\u008f\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\f\3\f\7\fZ\n\f\f\f\16\f]\13\f\3\r\6\r`\n\r\r\r\16"+
		"\ra\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3"+
		"\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\6"+
		"\31\177\n\31\r\31\16\31\u0080\3\31\3\31\3\32\3\32\3\32\3\32\7\32\u0089"+
		"\n\32\f\32\16\32\u008c\13\32\3\32\3\32\2\2\33\3\3\5\4\7\5\t\6\13\7\r\b"+
		"\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26"+
		"+\27-\30/\31\61\32\63\33\3\2\7\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13"+
		"\f\17\17\"\"\4\2\f\f\17\17\2\u0092\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2"+
		"\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3"+
		"\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2"+
		"\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2"+
		"\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\3\65\3\2"+
		"\2\2\5\67\3\2\2\2\79\3\2\2\2\t=\3\2\2\2\13?\3\2\2\2\rE\3\2\2\2\17G\3\2"+
		"\2\2\21I\3\2\2\2\23L\3\2\2\2\25Q\3\2\2\2\27W\3\2\2\2\31_\3\2\2\2\33c\3"+
		"\2\2\2\35e\3\2\2\2\37g\3\2\2\2!i\3\2\2\2#k\3\2\2\2%m\3\2\2\2\'p\3\2\2"+
		"\2)s\3\2\2\2+u\3\2\2\2-x\3\2\2\2/z\3\2\2\2\61~\3\2\2\2\63\u0084\3\2\2"+
		"\2\65\66\7*\2\2\66\4\3\2\2\2\678\7+\2\28\6\3\2\2\29:\7x\2\2:;\7c\2\2;"+
		"<\7t\2\2<\b\3\2\2\2=>\7=\2\2>\n\3\2\2\2?@\7r\2\2@A\7t\2\2AB\7k\2\2BC\7"+
		"p\2\2CD\7v\2\2D\f\3\2\2\2EF\7}\2\2F\16\3\2\2\2GH\7\177\2\2H\20\3\2\2\2"+
		"IJ\7k\2\2JK\7h\2\2K\22\3\2\2\2LM\7g\2\2MN\7n\2\2NO\7u\2\2OP\7g\2\2P\24"+
		"\3\2\2\2QR\7y\2\2RS\7j\2\2ST\7k\2\2TU\7n\2\2UV\7g\2\2V\26\3\2\2\2W[\t"+
		"\2\2\2XZ\t\3\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\30\3\2\2\2"+
		"][\3\2\2\2^`\t\4\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\32\3\2\2"+
		"\2cd\7,\2\2d\34\3\2\2\2ef\7\61\2\2f\36\3\2\2\2gh\7-\2\2h \3\2\2\2ij\7"+
		"/\2\2j\"\3\2\2\2kl\7?\2\2l$\3\2\2\2mn\7?\2\2no\7?\2\2o&\3\2\2\2pq\7#\2"+
		"\2qr\7?\2\2r(\3\2\2\2st\7>\2\2t*\3\2\2\2uv\7>\2\2vw\7?\2\2w,\3\2\2\2x"+
		"y\7@\2\2y.\3\2\2\2z{\7@\2\2{|\7?\2\2|\60\3\2\2\2}\177\t\5\2\2~}\3\2\2"+
		"\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3"+
		"\2\2\2\u0082\u0083\b\31\2\2\u0083\62\3\2\2\2\u0084\u0085\7\61\2\2\u0085"+
		"\u0086\7\61\2\2\u0086\u008a\3\2\2\2\u0087\u0089\n\6\2\2\u0088\u0087\3"+
		"\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b"+
		"\u008d\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e\b\32\2\2\u008e\64\3\2\2"+
		"\2\7\2[a\u0080\u008a\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}