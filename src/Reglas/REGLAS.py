
def p_REGLA_0(p):
   '''
   Code : instruction 
   '''
   p[0] =(p[1] )
def p_REGLA_1(p):
   '''
   instruction : instruction instruction 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_2(p):
   '''
   instruction : ifelsestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_3(p):
   '''
   instruction : ifstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_4(p):
   '''
   instruction : forstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_5(p):
   '''
   instruction : incasestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_6(p):
   '''
   instruction : defstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_7(p):
   '''
   instruction : excecstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_8(p):
   '''
   instruction : printstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_9(p):
   '''
   instruction : metronomostatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_10(p):
   '''
   instruction : declarationstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_11(p):
   '''
   instruction : negationstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_12(p):
   '''
   instruction : tfstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_13(p):
   '''
   instruction : ffstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_14(p):
   '''
   instruction : abanicostatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_15(p):
   '''
   instruction : verticalstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_16(p):
   '''
   instruction : percutorstatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_17(p):
   '''
   instruction : golpestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_18(p):
   '''
   instruction : vribatoestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_19(p):
   '''
   instruction : typeestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_20(p):
   '''
   instruction : expressionestatement ENDLINE 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_21(p):
   '''
   ifelsestatement : ifstatement elsestatement 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_22(p):
   '''
   ifstatement : IF boolParam Scope 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_23(p):
   '''
   elsestatement : ELSE Scope 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_24(p):
   '''
   forstatement : FOR VAR TO numberParam STEP numberParam Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6], p[7] )
def p_REGLA_25(p):
   '''
   forstatement : FOR var TO numberParam STEP numberParam Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6], p[7] )
def p_REGLA_26(p):
   '''
   forstatement : FOR VAR TO numberParam Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_27(p):
   '''
   forstatement : FOR var TO numberParam Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_28(p):
   '''
   incasestatement : ENCASO whenestatement whenelseestatement FINCASO 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_29(p):
   '''
   incasestatement : ENCASO var whenEstatementIncompletebool whenelseestatement FINCASO 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_30(p):
   '''
   incasestatement : ENCASO var whenEstatementIncompletenum whenelseestatement FINCASO 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_31(p):
   '''
   defstatement : DEF VAR Parameters Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_32(p):
   '''
   defstatement : DEF PRINCIPAL LPAREN RPAREN Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_33(p):
   '''
   excecstatement : EXEC VAR Parameters 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_34(p):
   '''
   printstatement : PRINT Parameters 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_35(p):
   '''
   metronomostatement : METRONOMO LPAREN A COMMA numberParam RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6] )
def p_REGLA_36(p):
   '''
   metronomostatement : METRONOMO LPAREN D COMMA numberParam RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6] )
def p_REGLA_37(p):
   '''
   declarationstatement : SET var COMMA numberParam 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_38(p):
   '''
   declarationstatement : SET var COMMA boolParam 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_39(p):
   '''
   declarationstatement : SET var COMMA NUMBER 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_40(p):
   '''
   declarationstatement : SET var COMMA var 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_41(p):
   '''
   negationstatement : SET var DOT NEG 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_42(p):
   '''
   tfstatement : SET var DOT T 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_43(p):
   '''
   ffstatement : SET var DOT F 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_44(p):
   '''
   abanicostatement : ABANICO LPAREN A RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_45(p):
   '''
   abanicostatement : ABANICO LPAREN B RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_46(p):
   '''
   verticalstatement : VERTICAL LPAREN D RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_47(p):
   '''
   verticalstatement : VERTICAL LPAREN I RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_48(p):
   '''
   percutorstatement : PERCUTOR LPAREN D RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_49(p):
   '''
   percutorstatement : PERCUTOR LPAREN I RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_50(p):
   '''
   percutorstatement : PERCUTOR LPAREN A RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_51(p):
   '''
   percutorstatement : PERCUTOR LPAREN B RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_52(p):
   '''
   percutorstatement : PERCUTOR LPAREN DI RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_53(p):
   '''
   percutorstatement : PERCUTOR LPAREN AB RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_54(p):
   '''
   golpestatement : GOLPE LPAREN RPAREN 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_55(p):
   '''
   vribatoestatement : VIBRATO LPAREN numberParam RPAREN 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_56(p):
   '''
   typeestatement : LPAREN var RPAREN 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_57(p):
   '''
   expressionestatement : expression 
   '''
   p[0] =(p[1] )
def p_REGLA_58(p):
   '''
   Scope : LSCOPE Pre_Scope instruction RSCOPE 
   '''
   p[0] =(p[1], p[2], p[3], p[4] )
def p_REGLA_59(p):
   '''
   whenestatement : CUANDO var condition boolParam ENTONS Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6] )
def p_REGLA_60(p):
   '''
   whenestatement : CUANDO var condition numberParam ENTONS Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5], p[6] )
def p_REGLA_61(p):
   '''
   whenestatement : whenestatement whenestatement 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_62(p):
   '''
   whenelseestatement : SINO Scope 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_63(p):
   '''
   whenEstatementIncompletebool : CUANDO condition boolParam ENTONS Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_64(p):
   '''
   whenEstatementIncompletebool : whenEstatementIncompletebool whenEstatementIncompletebool 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_65(p):
   '''
   whenEstatementIncompletenum : CUANDO condition numberParam ENTONS Scope 
   '''
   p[0] =(p[1], p[2], p[3], p[4], p[5] )
def p_REGLA_66(p):
   '''
   whenEstatementIncompletenum : whenEstatementIncompletenum whenEstatementIncompletenum 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_67(p):
   '''
   Parameters : ParameterIncomplete RPAREN 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_68(p):
   '''
   Parameters : LPAREN RPAREN 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_69(p):
   '''
   ParameterIncomplete : ParameterIncomplete COMMA numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_70(p):
   '''
   ParameterIncomplete : ParameterIncomplete COMMA var 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_71(p):
   '''
   ParameterIncomplete : ParameterIncomplete COMMA boolParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_72(p):
   '''
   ParameterIncomplete : ParameterIncomplete COMMA TEXT 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_73(p):
   '''
   ParameterIncomplete : LPAREN numberParam 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_74(p):
   '''
   ParameterIncomplete : LPAREN var 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_75(p):
   '''
   ParameterIncomplete : LPAREN boolParam 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_76(p):
   '''
   ParameterIncomplete : LPAREN TEXT 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_77(p):
   '''
   var : VAR 
   '''
   p[0] =(p[1] )
def p_REGLA_78(p):
   '''
   numberParam : var 
   '''
   p[0] =(p[1] )
def p_REGLA_79(p):
   '''
   numberParam : NUMBER 
   '''
   p[0] =(p[1] )
def p_REGLA_80(p):
   '''
   boolParam : bool 
   '''
   p[0] =(p[1] )
def p_REGLA_81(p):
   '''
   boolParam : var 
   '''
   p[0] =(p[1] )
def p_REGLA_82(p):
   '''
   bool : BOOLEAN 
   '''
   p[0] =(p[1] )
def p_REGLA_83(p):
   '''
   bool : numberParam condition numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_84(p):
   '''
   bool : boolParam condition boolParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_85(p):
   '''
   condition : LESS 
   '''
   p[0] =(p[1] )
def p_REGLA_86(p):
   '''
   condition : GREAT 
   '''
   p[0] =(p[1] )
def p_REGLA_87(p):
   '''
   condition : EQUAL 
   '''
   p[0] =(p[1] )
def p_REGLA_88(p):
   '''
   condition : LESSEQUAL 
   '''
   p[0] =(p[1] )
def p_REGLA_89(p):
   '''
   condition : GREATEEQUAL 
   '''
   p[0] =(p[1] )
def p_REGLA_90(p):
   '''
   condition : DIFFERENT 
   '''
   p[0] =(p[1] )
def p_REGLA_91(p):
   '''
   Pre_Scope : 
   '''
   p[0] =()
def p_REGLA_92(p):
   '''
   numberParam : expression 
   '''
   p[0] =(p[1] )
def p_REGLA_93(p):
   '''
   expression : numberParam PLUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_94(p):
   '''
   expression : numberParam MINUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_95(p):
   '''
   expression : numberParam TIMES numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_96(p):
   '''
   expression : numberParam DIVIDE numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_97(p):
   '''
   expression : numberParam INTDIVIDE numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_98(p):
   '''
   expression : numberParam MODULUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_99(p):
   '''
   expression : numberParam POWER numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_100(p):
   '''
   expression : LPAREN expression RPAREN 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_101(p):
   '''
   expression : expression PLUS expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_102(p):
   '''
   expression : expression MINUS expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_103(p):
   '''
   expression : expression TIMES expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_104(p):
   '''
   expression : expression DIVIDE expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_105(p):
   '''
   expression : expression INTDIVIDE expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_106(p):
   '''
   expression : expression MODULUS expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_107(p):
   '''
   expression : expression POWER expression 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_108(p):
   '''
   expression : expression PLUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_109(p):
   '''
   expression : expression MINUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_110(p):
   '''
   expression : expression TIMES numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_111(p):
   '''
   expression : expression DIVIDE numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_112(p):
   '''
   expression : expression INTDIVIDE numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_113(p):
   '''
   expression : expression MODULUS numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_114(p):
   '''
   expression : expression POWER numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )
def p_REGLA_115(p):
   '''
   numberParam : MINUS numberParam 
   '''
   p[0] =(p[1], p[2] )
def p_REGLA_116(p):
   '''
   numberParam : numberParam DOT numberParam 
   '''
   p[0] =(p[1], p[2], p[3] )