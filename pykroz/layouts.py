from levels import Level, Convert_Format

def Level1(level: Level):
    level.Fp[1]  = '        1    1     1  1     1     1   1      1        1         '
    level.Fp[2]  = '   ---#######   1        1     1          1      1#######---   1'
    level.Fp[3]  = '   #        #1      1     1        1    1      1  #+ + + + #    '
    level.Fp[4]  = '1  #   TT   #     1   1      1   1          1     # + + + +#1   '
    level.Fp[5]  = '   #        #  1        1       1     1         1 #+ + + + #    '
    level.Fp[6]  = '   ##########       1     1         1     1   1   ##########  1 '
    level.Fp[7]  = '1   1       1     1    1      1         1       1      1       1'
    level.Fp[8]  = '  1      1      1                         1       1     1    1  '
    level.Fp[9]  = '   1    1   1      1   XXXXXXXXXXXXXXX     1   1     1        1 '
    level.Fp[10] = '      1      1   1     XXXXX  I  XXXXX   1      1   1    1      '
    level.Fp[11] = '1   1    1    1    1   XXXX+     +XXXX    1   1       1        1'
    level.Fp[12] = ' 1      1  1    1      XXXX+  P  +XXXX   1      1      1    1   '
    level.Fp[13] = '    1     1  1     1   XXXX+     +XXXX     1      1  1    1    1'
    level.Fp[14] = ' 1   1     1     1     XXXXX  S  XXXXX   1    1       1      1  '
    level.Fp[15] = '1      1 1    1        XXXXXXXXXXXXXXX      1   1       1     1 '
    level.Fp[16] = '  1     1  1      1                      1     1    1      1    '
    level.Fp[17] = '    1       1    1     1     1     1    1     1       1 1      1'
    level.Fp[18] = '1  ##########1    1   1    1    1     1      1   1########## 1  '
    level.Fp[19] = ' 1 # W W W W# 1        1    1     1      1 1      #        #    '
    level.Fp[20] = '1  #W W W W #   1   1    1     1     1         1  #   LL   #  1 '
    level.Fp[21] = '   # W W W W#1       1    1        1   1     1    #        #    '
    level.Fp[22] = '1  ---#######    1     1    1 1     1     1     1 #######---    '
    level.Fp[23] = '        1    1     1            1  1     1     1        1      1'
    Convert_Format(level)

def Level3(level: Level):
    level.Fp[1]  = '+++##############RRRRRRR###         ##sm######TVVVVT##K-        '
    level.Fp[2]  = '+C+D       +    K#RRRRRRR##    C    ##was#### VVVVVV ###      # '
    level.Fp[3]  = '+++######## ####1#RRRRRRR##         ##here## VVV++VVV ##333333# '
    level.Fp[4]  = '########### #####1#RRRRRRR#####T########### VVV++++VVV1######## '
    level.Fp[5]  = '         +# #2####1#RRRRRRR######+# #K# #3#1VVV++++VVV       2KC'
    level.Fp[6]  = ' # ######## ##+####+#RRRRRRR###....# # # ### VVV++VVVV #X###### '
    level.Fp[7]  = '3# #######  ###+#####RRRRRRR## ############## VVVVVVV ##X##C### '
    level.Fp[8]  = ' # ###### # ####+#####RRRRRRR##  ##+:   :+#### VVVVV ###X##X### '
    level.Fp[9]  = '.# #T### ## #####+####XRRRRRRRX## #   :  :#####     ###TTT#X### '
    level.Fp[10] = '.# # ##+### ######+###XXXXXXXXX# ## ::::: ####### # #######X### '
    level.Fp[11] = '.# # # ###                          :+K+:         # #XXXXXXX###+'
    level.Fp[12] = '.# # C###   P  ###### ###XXXXXXXXX# ::;:: ####### # #XXXXXX####D'
    level.Fp[13] = '.# #3#### ////####### ###XRRRRRRRX#:: :   ###VW## # #XXXXX##WWWW'
    level.Fp[14] = '.# ###////\\\\\\//###### ####RRRRRRR##+ :  :+###TV## # #XXXX##KWWWW'
    level.Fp[15] = '.# ##//\\\\\\\\C\//////## ##T##RRRRRRR###########V+## #     ####WWWW'
    level.Fp[16] = '.# ##///\\\\\\1\\////###+ #+-+##RRRRRRR##cavern## V## ###///########'
    level.Fp[17] = ' # ###///\\\\\\//#####+# #---###RRRRRRR##of#####V ## #222222222\\###'
    level.Fp[18] = ' #  Q###//// #####+## #-C-#Z#RRRRRRR#tunnels# V## #222222222\\1 #'
    level.Fp[19] = ' ########### ####+### #---#3##RRRRRRR########V ## #222222222\\#D#'
    level.Fp[20] = '          I  ###2#### #2-2# ##RRRRRRR####  ## V## #222222222##D#'
    level.Fp[21] = '##################### ##/## ###RRRRRRR## ## #V ## #222222222##D#'
    level.Fp[22] = '22222222222222222222#       ####RRRRRRR# ###X V## #222222222##D#'
    level.Fp[23] = 'K + + + + + + + + +   ###########RRRRRRR#++##V    \\---------##L#'
    Convert_Format(level)

def Level5(level: Level):
    level.Fp[1]  = '//1////////\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\11111\\C\\1111111\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\XXCCC'
    level.Fp[2]  = '/////////1//\\\\\\\\1\\\\\\\\\\\\\\\\\\\\\\\\111\\\\\\111111\\\\XXX\\\\\\1\\\\\\\\\\\\\\/1XXCCC'
    level.Fp[3]  = '///RRR///////\\\\\\\\\\\\\\\\\\\\\\\\\\\\Z\\\\111111111\\\\\\\\XLX\\\\\\\\\\\\\\\\\\\\///XXXXX'
    level.Fp[4]  = '//RRRRRR//////\\\\\\\\\\\\U\\\\\\\\1\\\\\\\\\\\\11111\\\\\\\\\\\\XXX\\\\\\\\\\/////////////'
    level.Fp[5]  = '///RRRR///////\\\\\\1\\W W\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////1//////////'
    level.Fp[6]  = '/1//RR//XXXX/1//\\\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\\\\\\\\\\\\\//1/////////////////1////'
    level.Fp[7]  = '////////XCCX1//1////\\\\\\\\\\\\\\\\\\\\\\\\///////////////1////////////////'
    level.Fp[8]  = '////////XXXX/////////////////1////////////////////////XXXXXXXXXX'
    level.Fp[9]  = 'XXXX///////////////1///////////////XXXXXXXXXXXXXXXXXXXX========='
    level.Fp[10] = '===XXXXXXXXXXX/////////XXXXXXXXXXXXX============================'
    level.Fp[11] = '=============XXXXXXXXXXX========================================'
    level.Fp[12] = '======================================================  1     ; '
    level.Fp[13] = 'K11 111===============================W       1  W        W   : '
    level.Fp[14] = '1 1111 11 1    1       W        1         RR                  : '
    level.Fp[15] = '111 1111 11 1              W            RRRRR       W         : '
    level.Fp[16] = '1 1111 1111       1               W      +RRRRR               : '
    level.Fp[17] = '111 1111 1   1            1              RRRRRRRR1         W  : '
    level.Fp[18] = '1 1111 1111   B         W                 +RRRRRRR           1: '
    level.Fp[19] = '111 1111 111 1                      W     RRRRRRR    W        : '
    level.Fp[20] = '11 11 1111       1          W        1   RRRRRR         1     : '
    level.Fp[21] = ' 111111 1    1      W                     RRR1           W    : '
    level.Fp[22] = '111 11 111 1    1         P                      W            :`'
    level.Fp[23] = '1 11111 111  1       W            W                   W      I:U'
    Convert_Format(level)

def Level7(level: Level):
    level.Fp[1]  = ' I                3+             3+             3+             3'
    level.Fp[2]  = 'PI                3+             3+             3+             3'
    level.Fp[3]  = ' I                3+             3+             3+             3'
    level.Fp[4]  = '############################################################### '
    level.Fp[5]  = '+      ;K ##33333 33333##2 222 22222##111111 1111##..  ..     . '
    level.Fp[6]  = ';;; ;; ;; ##3 33333 333##222222 2222##1 111111 11##  .. .....   '
    level.Fp[7]  = 'U;;  ;  ; ##33 33U333 3## 2222U22 22##11111U1111 ## ....########'
    level.Fp[8]  = '  ;; ;; ; ##3333 333333##222 2222222##11 1111 111##. .. U    3..'
    level.Fp[9]  = '; I  ;;   ##3 3333333 3## 2222222 22##1 11 111111##.    #     .C'
    level.Fp[10] = ' ###############################################################'
    level.Fp[11] = '                     W;33333333333333333333333333333333333333333'
    level.Fp[12] = '  ###########################################W         K    ++++'
    level.Fp[13] = 'Z                                T                             1'
    level.Fp[14] = '  ##############################################################'
    level.Fp[15] = '    # #+# #1# #+# #1# # #E#+# # #1# # #1# #;# #1# # # #+# #;# ##'
    level.Fp[16] = '  ## # #E# # #1# # # #;# # # # # # #E# #+#1# # #;# #1# #1#E# #T#'
    level.Fp[17] = '  # # # #;# # # #1# #+#1# # #1# # # # #1# # # # # #E# # # #;#Q##'
    level.Fp[18] = '  ## #1# #+# # # #E# # # #1#;# #+# # #;# # #1#E#+# # #;# # #E#T#'
    level.Fp[19] = '    # # # # #1# # # #1# # # # # # #1# # #E# # #1# #1# # #1# # ##'
    level.Fp[20] = '  ##############################################################'
    level.Fp[21] = '  ###K     ;      3    +:    3     :+3       +: 3    :+     +  3'
    level.Fp[22] = '  ##########  ##   :+  3  +    :+      :+     3  +:+     3  ::::'
    level.Fp[23] = '              ##3         3 +:    3 +   3  :+      3   :+  :D`DL'
    Convert_Format(level)
    
def Level9(level: Level):
    level.Fp[1]  = 'K            3-      33333VVVVVVVVVVVV    .         .       .  Z'
    level.Fp[2]  = '     3-     ---     33VVVVVVVVVVVVVVZ          .                '
    level.Fp[3]  = '3-  ---           333VVVVVVVVVVVVVVVVVV  .        U   .      .  '
    level.Fp[4]  = '--              333VVVVVVVVVVVVVVVVVVVVVW    .           .      '
    level.Fp[5]  = '          3-   33VVVVVVVV\\\\\\\\\\\\\\\\VVVVVVVVVV         .        VVV'
    level.Fp[6]  = '   3-    ---  33VVVVVVV\\\\++++W+++\\\\VVVVVVVVVV   .    ZVVVVVVVVVV'
    level.Fp[7]  = '  ---        33VVVVVVV\\++\\\\RRRR\\\\+++\\\\VVVVVVVVVVVVVVVVVVVVVVVVVV'
    level.Fp[8]  = '3-       U  33VVVVVV\\\\+\\\\RRRRRRRRRR\\++\\\\VVVVVVVVVVVVVVVVVVVVVVVC'
    level.Fp[9]  = '--         33VVVVVV\\\\+\\RRRRRR////RRRR\\+\\\\\\VVVVVVVVVVVVVVV1111111'
    level.Fp[10] = '      333333VVVVVV\\\\+\\RRRR////11///RRR\\++\\\\VVVVVVVVV111111111111'
    level.Fp[11] = '  33333VVVVVVVVVV\\\\+\\\\RRR///11   1//RRRR\\+\\\\VVVV1111111111111111'
    level.Fp[12] = '333VVVVVVVVVVVVV\\\\\\W\\RRR//C111 P 11//RRR\\W\\\\\\VVV1111111---111111'
    level.Fp[13] = 'VVVVVVVVVVVVVVVVV\\\\\\+\\RRR//111   11//RRR\\+\\\\VVVV1111111-B-111111'
    level.Fp[14] = 'VVVVVVVVVVVVVVVVVV\\\\\\+\\RRR//111U11//RRR\\\\+\\VVVVVV111111---111111'
    level.Fp[15] = 'VVVVV3 .  3  VVVVVVV\\\\+\\RRR////////RRRR\\+\\\\VVVVV1111111111111111'
    level.Fp[16] = '3-.     -- .  VVVVVV\\\\\\+RRRR//////RRRR\\+\\\\VVVVV11111111111111---'
    level.Fp[17] = '--   - .3- --- VVVVVVV\\\\+\\RRRRRRRRRRR\\+\\\\VVVVV111111111111111- U'
    level.Fp[18] = '  - 3-  --.-3-. VVVVVVVV\\++\\RRRRRR\\\\++\\VVVVVV1111111111111111---'
    level.Fp[19] = ' 3.        ---   VVVVVVVVV\\++++W++++\\\\VVVVVV111111---11111111111'
    level.Fp[20] = '       U  3   3-  .VVVVVVVV\\\\\\\\\\\\\\\\VVVVVVVV1111111-B-11111111111'
    level.Fp[21] = '.  --.      - --.  - VVVVVVVVVVVVVVVVVVVVV11111111---11111111111'
    level.Fp[22] = '   3 --    3   -- 3-  ##VVVVVVVVVVVVVVVVV11111111111111111111111'
    level.Fp[23] = ' .   3  .    . 3-   . D+DLVVTTCCCTTVVVCC11111111111111111111111K'
    Convert_Format(level)

def Level11(level: Level):
    level.Fp[1]  = '                                                        WWWW  3S'
    level.Fp[2]  = 'U################# #################################`###########'
    level.Fp[3]  = ' :3; \\3+#3 W    K#3  #  W  W  W  W  W  W  W  W  W  #   3     3  '
    level.Fp[4]  = 'Z:+: \\3+# 3      #3  #  /////////////////////////  #      3     '
    level.Fp[5]  = ' :3; \\3+#    3   #3  #  /+//////+/////T///////+//  #            '
    level.Fp[6]  = ' :+: \\3+#        #3  #  ////T/////////////+////// 3#  3 ::;:  3 '
    level.Fp[7]  = ' :3; \\3+# 3  3   #3  # 3//////////W//////////////  #    :CC:    '
    level.Fp[8]  = ' :+: \\3+# W      #3  #  //+//////////////////+///  #    ;:::    '
    level.Fp[9]  = ' :3; \\3+#      3 #3  #  ///////+///////+/////////3 #3         3 '
    level.Fp[10] = ' :+: \\3+#3       #3  #3 /////////////////////////  #       3    '
    level.Fp[11] = ' :3; \\3+#W   3   #3  #  ///+//////XXXXX////W/////  #  3       3 '
    level.Fp[12] = 'P:C: \\3K#       3#3  #  ////////+/XXKXX+/////////  #############'
    level.Fp[13] = ' :3; \\3+# 3      #3  #  //////////XXXXX////////+/ 3#3         ++'
    level.Fp[14] = ' :+: \\3+#     3  #3  # 3/+////////+///////T//////  #3+        ++'
    level.Fp[15] = ' :3; \\3+#  3W    #3  #  /////////////////////////  #3+          '
    level.Fp[16] = ' :+: \\3+#        #3  #  /////T//////+////////+///  #3+      ::::'
    level.Fp[17] = ' :3; \\3+# 3    3 #3  #3 /////////////////////////3 #3+      ```L'
    level.Fp[18] = ' :+: \\3+#        #3  #  //W//////////////+///////  #3+      ::::'
    level.Fp[19] = ' :3; \\3+#W   3   #3  #  /////+////+///////////+//  #3+          '
    level.Fp[20] = 'S:+: \\3+#3       #3  #  /////////////////////////  #3+        ++'
    level.Fp[21] = ' :3; \\3+#        #3 K#                             #3         ++'
    level.Fp[22] = 'U### ####I########################## ###############E###########'
    level.Fp[23] = '                                                        ++++  3S'
    Convert_Format(level)

def Level13(level: Level):
    level.Fp[1]  = 'KKKKDE EI .  I  E    2  I   E  RRCC211///////// ////////////T//K'
    level.Fp[2]  = 'VVVVVE     2    I    .     .   RR22211//////// / ///////////2// '
    level.Fp[3]  = '  E  I .    E  .     E  .    2 RR11111///   / ///      /////2// '
    level.Fp[4]  = '2  . 2  E .     E2  . I    I   RR//////// // ////////// ////2// '
    level.Fp[5]  = '  I   .    I   I .        .    RR//////// /////222////// ///2// '
    level.Fp[6]  = 'E .   I E  .2  E    E .    E   RR/////T// /////2P2/   /// //2// '
    level.Fp[7]  = ' 2   E  . I    .   I   I .    ERRC/////// /////222/ // /// / // '
    level.Fp[8]  = 'I   .    2 E.  E     .      I  RR//////// ////// // // ////  // '
    level.Fp[9]  = '.E I    .    I    2   E     .2 RR//////// ///////  ///I///// // '
    level.Fp[10] = '   . 2     .      . I          RR//      1/ ////////// ////// / '
    level.Fp[11] = '2I   . E   I  2.I  E      I.  \\\\\\\\ /////// /           ///////  '
    level.Fp[12] = 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\\ZZ\\RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR'
    level.Fp[13] = '22--2-2--2--2-+--22----2-2---2\\\\\\\\VVVVVVVVVVVTVVV W VVVVVVTVVVVV'
    level.Fp[14] = '--2-2--2-2-2---2---2-2-+2---2--RR   .VVVVVVVVV + VVVTVVVV V VVVV'
    level.Fp[15] = '+2-2--2---2-2---22---2---2----2RRV     . VVVVVVVVVVVV VV VVV   V'
    level.Fp[16] = '2--+-2--2--+--22---2--+-2---2-+RRVV.  .     .VVVVVVVV V VVVVVV V'
    level.Fp[17] = '-2--2-2--2---2-+-22----2--2----RRVVVV    .       .VVVV  VVVV TVV'
    level.Fp[18] = '2-2--2--2-+2--B-2---2-+-2--+-2-RRVVVVVV  .   .      VVVVVVV VVVV'
    level.Fp[19] = '2+-2---2--2--2-2--2---2--2-----RRVVVVVVVV         .   .VVVVV VVV'
    level.Fp[20] = '-22-+-2--2-2---22--+-2--2-2-2--RRVVVVVVVVVV .            .V VVVV'
    level.Fp[21] = '2---2---2-2--2-+-2----2----2--+RRVVVVLDVVVVVV  .    .     . VVVV'
    level.Fp[22] = 'VVVV2--2-+-2-2----2--2-2-2-2---RRCCVVVVDVDDVD                VVV'
    level.Fp[23] = 'KKKD-2---2-2--2-2---2-+-2--2--2RRCCVVVVVDVVDVV222222222222222DKK'
    Convert_Format(level)

def Level15(level: Level):
    level.Fp[1]  = '+*****#3#L#+ \\    2    \\ 2   2   W#CCCC#=C;=====    ====        '
    level.Fp[2]  = '+**Q**# #D#     \\/  2 \\\\     //   ##33##=;;===== === == ======= '
    level.Fp[3]  = '+*****# #D#\\\\  //\\/   \\     \\\\// 2#\\33\\#===I=.  === ==== ===== ='
    level.Fp[4]  = '2###### #X#2  2 ///     2    //   #\\33\\#====  .=== ====== === =='
    level.Fp[5]  = '2D33V  ##X#\\\\       2   \\/     2  #\\33\\#===. .=== ======= == ==='
    level.Fp[6]  = '2#33#C##X##\\/\\  2 /\\     2   /\\   #\\33\\#==.  ==== ==  S  == ===='
    level.Fp[7]  = '2#33#.##X#W\\/\\\\      2  \\\\\\   //  #\\;;\\#== ====== == ======11111'
    level.Fp[8]  = '2#33#.##X#/\\B      \\/  \\\\/   2  2 #\\  \\#== ====== === =====11111'
    level.Fp[9]  = '2#33#.###X\\///  ///   2 \\\\        #X  X#=== ===== ==== ====11111'
    level.Fp[10] = '2#33#.#####+\\//2/\\//         \\\\ 2 #X  X#=    ==== ===== =======;'
    level.Fp[11] = '2#33#.##X##++\\////   2\\  \\  //\\\\  #X  X#= ======= W  : ======= ='
    level.Fp[12] = '2#33#.##XX##         \\/\\ 2   \\\\2  #X  X#== ====== 2    ====== =='
    level.Fp[13] = '2#XX#.##XXX######## 2          ---#X  X#= ================ W ==='
    level.Fp[14] = '2#XX#.##XRRRRRRRRR##########2  - U#X  X# ====    ===1==== ======'
    level.Fp[15] = ';#XX#.##XRRRRRRRRRRRRRRRRRR########X  X#= == ==== == ==== ======'
    level.Fp[16] = ' #XX#.##XXRRRRRRRRRRRRRRRRRRRRRRRR#X  X#=K==    ==   =====   ==='
    level.Fp[17] = ' #XX#.##X##11RRRRRRRRRRRRRRRRRRRRR##  ########== ==== ======= =='
    level.Fp[18] = 'Z#XX#.####11111111111111RRRRRRRRR##  ##RRRRRR###= ==== ======= ='
    level.Fp[19] = ' #XX#.###11111111111111111111RRR##  ##RRRRRRRRR#== === ======== '
    level.Fp[20] = ' #XX#.##11111111111111111111111##  ##RRRRRRRRRR##== == ======== '
    level.Fp[21] = ' #CK#.##11111111B111111111B11111111##RRRRRRRRRRR#   == ======= ='
    level.Fp[22] = 'P####X##111111111111111111111111111111RRRRRRRRRRU#====   ==== =='
    level.Fp[23] = '       /-------------C----------------URRRRRRRRRRR#======      T'
    Convert_Format(level)

def Level17(level: Level):
    level.Fp[1]  = '     2    KRR++                P RRRRRRRRRRRR                   '
    level.Fp[2]  = ' RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR      -         RRRRRRRRRRRRRRR  '
    level.Fp[3]  = '                    ++++++C 3RR  RRRRR1 RRRRR  RRCE             '
    level.Fp[4]  = ' RRRRRRRRRRRRRRRRRRRRRRRRRR  RR  RRC1RRRR 1RR  RRRRRRRRRRRRRRRRR'
    level.Fp[5]  = '2222222222           ZRRTRRRRRR  RR  -     -       XXXXXXXXXXXKR'
    level.Fp[6]  = '--RRRR--RRRRRRRRRRRRRRRR     RR33RRRRRRRRRRRR  RR  RRRRRRRRRRRRR'
    level.Fp[7]  = '  RR-----------..*****RRRRR    **         +RR  RR             RR'
    level.Fp[8]  = '  RR--RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--RRRRRRRRRRRRR  RR'
    level.Fp[9]  = '  RR--RR11111111----------D+DWD+DWD+DWLLRR333          2CBRR  RR'
    level.Fp[10] = '  RR--RR11111111RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR  RR'
    level.Fp[11] = '  RR--RR--RRRRRRRR  DT+*W*+TCRRZ1                             RR'
    level.Fp[12] = '  RR--RR--RRII.KRR  RRRRRRRRRRRRRRRRRRRR  RRRRRRRRRRRRRRRRRRRRRR'
    level.Fp[13] = '  RR--RR--RRIIRRRR                        RRU1-------XXXXXXXXX  '
    level.Fp[14] = '  RR--RR--RRIIRRRRRRRRRRRRRRRRRRRRRR  RR  RRRRRRRRRRRRRRRRRRRR  '
    level.Fp[15] = '  RR--RR--RR..RR 1RR 1RR 1RRR         RR                        '
    level.Fp[16] = '  RR--RR--RRIIRR  -   -   -    RRRRRRRRR  RRRRRRRRRRRRRRRRRRRRRR'
    level.Fp[17] = '  RR------RRIIRR  RRRRRRRRRRR  RR  ;W;W;           22222222CRRK '
    level.Fp[18] = '  RRRRRRRRRRIIRR         2KRRWWRR  RRRRRRRRRRRRRRRRRRRRRRRRRRR--'
    level.Fp[19] = '         -    RRRRRRRRRRRRRRRRRRR  RRXXXXXXXXXXXXXC3333333333333'
    level.Fp[20] = '  RRRRR 1RRR          1            RR--RRRRRRRRRRRRRRRRRRRRRRR- '
    level.Fp[21] = '  X  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--URRCCRRCCRRXXXXXX333333  '
    level.Fp[22] = '--RR              RRRRRRRR    2   KRR- RRR..RR..RR**RR**RR**RR  '
    level.Fp[23] = '33RRRRRRRRRRRRRR   *    *   RRRRRRRRR--E.E******RRK*RR**RR**RR  '
    Convert_Format(level)

def Level19(level: Level):
    level.Fp[1]  = '1  C  1      +   1   +        +  1      +     + 1 RRR++++++RRRRL'
    level.Fp[2]  = '--   ---  1     ---        1    ---  1         ---RRRR++++++RRRD'
    level.Fp[3]  = ' 1       ---RRRRRR    1   ---       ---    W      RRRR;;;;;;RRR1'
    level.Fp[4]  = '---  *  1 RRRRRRRRRR1---       1       1       1  RRRR111111RRR1'
    level.Fp[5]  = '1      RRRRR#####RRRRRR 1     ---     ---   1 ---RRRRR111111RRR1'
    level.Fp[6]  = '--1   RRRRRR#U K#RRRRR ---  1      T       ---  RRRRRR11111RRRR1'
    level.Fp[7]  = ' ---   RRRRR#####RRR       ---           1    #RRRRRR#11111RRRR1'
    level.Fp[8]  = '    1    RRRRRRRRRR  1           1      ---   ########11111RRRR1'
    level.Fp[9]  = ' * ---    RRRRRRRR  ---         ---   1       D--Z---`11B11RRRR1'
    level.Fp[10] = '      1    RRRRR            W        ---      ########111111RRR1'
    level.Fp[11] = '     ---                                      #RRRRRR#111111RRR1'
    level.Fp[12] = '               ;;;;;;;;;;;;;;;;;;;;;;;;;;;;; FFRRRRRR1111111RRR1'
    level.Fp[13] = '#############################################;;;RRRRR11111111RR1'
    level.Fp[14] = '    #++#W3#* #  # *##::::::+::::K:::::::::::#1111RRRRR1111111RR1'
    level.Fp[15] = ' #  #3 #3 #        ##:3::::::::-::::::3:::::#11111RRRRR111111RR1'
    level.Fp[16] = 'P#  #  #  #3 #  #  ##:::::::::-:::3:::::::::#11111RRRRR111111RR1'
    level.Fp[17] = ' #3 #  K  #  #  #3 ##::::::::-::::::::::::::#11111RRRRR11B111RR1'
    level.Fp[18] = 'I#  #  #  #  # 3#  ##:::3:::-:::::::::::3:::#11111RRRRR11111RRR1'
    level.Fp[19] = ' #  #  #  #  #  #  ##::::::;::::::::*:::::::#1111RRRRRR11111RRR1'
    level.Fp[20] = 'Z#  #  # 3# 3#  #  ##///////////////////////#1111RRRRR11111RRRR1'
    level.Fp[21] = ' #     #  #  #3 #                           #EEERRRRRR11111RRRR1'
    level.Fp[22] = 'C# 3#  #  #  #**#  ##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#+++RRRRR;;;;;;RRRR '
    level.Fp[23] = '3#+ #3*#3    #**#+3##33333333333333333333333#CCRRRRRRR*-U-*RRRRU'
    Convert_Format(level)

def Level21(level: Level):
    level.Fp[1]  = 'LVVVVVVVVVVVVVVVVVVVVVV333333333333333333VVVVVVVVVVVVVVVVVVVVVVK'
    level.Fp[2]  = 'DVVVVVVVVVVVVVVVVVVVV333                333VVVVVVVVVVVVVVVVVVVVI'
    level.Fp[3]  = '.VVVVVVVVVVVVVVVVVV333         ***        333VVVVVVVVVVVVVVVVVV-'
    level.Fp[4]  = 'DVVVVVVVVVVVVVVVV333         *******        333VVVVVVVVVVVVVVVV-'
    level.Fp[5]  = '.VV+VVVVVVVVVVV333          ****F****         333VVVVVVVVVVV+VV-'
    level.Fp[6]  = 'DVQ+VVVVVVVVV333   +         *******         +  333VVVVVVVVV+CV-'
    level.Fp[7]  = '-VV+VVVVVVV333        +        ***        +       333VVVVVVV+VV-'
    level.Fp[8]  = '-VVVVVVVV333             +             +            333VVVVVVVV-'
    level.Fp[9]  = '-VVVVVV333      Z                              T      333VVVVVV-'
    level.Fp[10] = '-VVVV333                     -------                    333VVVV-'
    level.Fp[11] = '-VV333                      ---------                     333VV-'
    level.Fp[12] = 'E33C3         +    +    +  -----P-----  +    +    +        3C33E'
    level.Fp[13] = '-VV333                      ---------                     333VV-'
    level.Fp[14] = '-VVVV333                     -------                    333VVVV-'
    level.Fp[15] = '-VVVVVV333      T                              Z      333VVVVVV-'
    level.Fp[16] = '-VVVVVVVV333             +             +            333VVVVVVVV-'
    level.Fp[17] = '-VV+VVVVVVV333        +        ***        +       333VVVVVVV+VV-'
    level.Fp[18] = '-VC+VVVVVVVVV333   +         *******         +  333VVVVVVVVV+CV-'
    level.Fp[19] = '-VV+VVVVVVVVVVV333          ****F****         333VVVVVVVVVVV+VV-'
    level.Fp[20] = '-VVVVVVVVVVVVVVVV333         *******        333VVVVhelp!VVVVVVV-'
    level.Fp[21] = '-VVVVVVVVVVVVVVVVVV333         ***        333VVVVVVVVVVVVVVVVVV-'
    level.Fp[22] = '.VVVVVVVVVVVVVVVVVVVV333                333VVVVVVVVVVVVVVVVVVVVF'
    level.Fp[23] = 'KVVVVVVVVVVVVVVVVVVVVVV333333333333333333VVVVVVVVVVVVVVVVVVVVVVK'
    Convert_Format(level)

def Level23(level: Level):
    level.Fp[1]  = 'L UD*D*D*D*D------------------------;;;;;;;;;;;;;;;;;;;;;;;;;;;;'
    level.Fp[2]  = '############-----------------##-####                           S'
    level.Fp[3]  = '+2222K2222+#11111111111111111##-22X# XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    level.Fp[4]  = '+222222222+#-----------------##-22X# XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    level.Fp[5]  = '+222222222+#22222222222222222##-2XX#                            '
    level.Fp[6]  = '2/////////2#-----------------##-2XK#----------------------------'
    level.Fp[7]  = '2/W--W--W/2#33333333333333333##-22X#2222222222222222222222222222'
    level.Fp[8]  = '2/-------/2#-----------------##-22X#2222222222222222222222222222'
    level.Fp[9]  = '2/---P---/2#22222222222222222##-2XX#2222222222222222222222222222'
    level.Fp[10] = '2/---B---/2#-----------------##-2X+#----------------------------'
    level.Fp[11] = '2/-------/2#1111111-K-1111111##-22X#3333333333333333333333333---'
    level.Fp[12] = '2/-------/2####################-22X#333333333333333333333333----'
    level.Fp[13] = '2/W--W--W/2#--1111111111111-+##-2XX#3333------33333-------------'
    level.Fp[14] = '2/////////2#Q-------------------2X+#333--------333----------I--3'
    level.Fp[15] = '2222#Z#2222################# ##-22X#33----------3--------------3'
    level.Fp[16] = '2222#-#2222#=------======K==-##-22X#3-----33---------33333333333'
    level.Fp[17] = '#####-######*-=====-====-=-=-##-2XX#3----3333-------333333333333'
    level.Fp[18] = 'C222/-/2222#==----==--==-==--##-2X+#3---333333-----3333333333333'
    level.Fp[19] = '2222/-/////#=====-====-=-====##-22X#3---3333333333333333--------'
    level.Fp[20] = '2222/-;;;;;;-==---==--==-=---##-22X#3---333333333333333--*+*+*+K'
    level.Fp[21] = '///////////#=-=-===-=====-==-##-2XX#---------------------#######'
    level.Fp[22] = 'C2222222222#W---====-----===S##-2XC#+--------------------##22222'
    level.Fp[23] = '####################################:::::::::::::;:::::::##X222U'
    Convert_Format(level)

def Level25(level: Level):
    level.Fp[1]  = 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVVVVVVVVVVVVVVVVVVVVVVCC'
    level.Fp[2]  = 'VRRRRRVVVVVVVVV VVVVV VVVVVVVVVVVVVVV V VVV**VVVVVV*****VVVVVVCC'
    level.Fp[3]  = 'VRU KRVVV**VVV V VVV VIVVV*****VVVVV VVV V**VVVVVV V*****VVVVVVV'
    level.Fp[4]  = 'VRRRRRVVVV**V VVV V VVV V*****V VVV VVVVV VVVVVVV VVV*****VVVVVV'
    level.Fp[5]  = 'VVVVVVVVVVVV VVVVV VVVVV*****VVV V VVVVVVV V V V VVV VVVVVVVVVVV'
    level.Fp[6]  = 'VVVVVVVVVVV VVVVVVV**VVVVVVVVVVVV VVVVVVVVV V3V VVV VVVVVVVVVVVV'
    level.Fp[7]  = 'VVVV VVVVV VVVVVVVVV**VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVRRRRRVVVV'
    level.Fp[8]  = 'VVV V VVV3V VVV VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVVRU KRVVVV'
    level.Fp[9]  = '***VVV V VVV V V VVVV##########XX##########VVVVVVV VVVVRRRRRVVVV'
    level.Fp[10] = 'V***VVV VVVVV VVV VVVl#IIIIIIIIIIIIIIIIII##VVVVVV V**VVVVVVVV**V'
    level.Fp[11] = 'VVVVVVTVVVV**VVVVV VVa#I#####IIIIII#####I#pVVVVV VVV**VVVV V**VV'
    level.Fp[12] = 'VVVVV VVVV**VVVVV VVVv#I#LD+DIIIIIID-PU#I#iVVVV VVVVVVVVV V VVVV'
    level.Fp[13] = 'VVVVVV VVVVVVVVV VVVVa#I#####IIIIII#####I#tV***VVVVVVVVVTVVV VVV'
    level.Fp[14] = 'VVVVVVV VVVV*****VVVV##IIIIIIIIIIIIIIIIII#!VV***VVVVVVV VVVVV VV'
    level.Fp[15] = 'VVVVVV VVVVVV*****VVV##########XX##########VVV***VVVVV VVVVVVV V'
    level.Fp[16] = 'VVVVV VVVVVVVV*****VVVVVVVVVVVVVVVVVVVVVVVVVVVV***VVV VVV VVVVV '
    level.Fp[17] = 'VVVVVV****VVVV VVVVVVVVVVVVVVVVVVVVVVVVVV VVVVVVVV V VVV V VVV V'
    level.Fp[18] = 'VVVVV****VVVV VVVVVVVV***VVV V V V VVVVV V VVVVVVVV VVV VVV V VV'
    level.Fp[19] = 'VVVV****VVVVVV3VVVVVVVV***V V V V V VVVIVVV3VVVVVVVVVV VVVVV VVV'
    level.Fp[20] = 'VVVVVVVVVVVVVVV V VVVVV VV VVVRRRRRV V VVVVV VVVVVVVV VVVV**VVVV'
    level.Fp[21] = 'VVVVVVVVVVVVVVVV V VVV VVVVVVVRU KRVV VVVVVVV VVV****VVVV**VVVVV'
    level.Fp[22] = 'VVVVVVVVVVVVVV**VVV V VVVVVVVVRRRRRVVV**VVVVVV V****VVVVVVVVVVVC'
    level.Fp[23] = 'CCCCVVVVVVVVV**VVVVV VVVVVVVVVVVVVVVVVV**VVVVVV****VVVVVVVVVVVCC'
    Convert_Format(level)

def Level27(level: Level):
    level.Fp[1]  = '3     +=     =+=    =  1=  =+=  =     -   -2   -    -2    -  Z-2'
    level.Fp[2]  = '3 P =   =   =   1==  =    =   = 1=    -2  -    -2   -    K-2  - '
    level.Fp[3]  = '##################################   ###########################'
    level.Fp[4]  = '3 3 3 3 3**********************K##   ##LVSDCD++D*D++D##D1****DDC'
    level.Fp[5]  = '   K C############################   ##VV+DCD########**######D#D'
    level.Fp[6]  = '          V V  V  V V V   VV   V V   ##ITFD##---D*DID###**DCD*D-'
    level.Fp[7]  = 'VXVVVVVVVVS  VV V    V V V  V V V    ##ZW*.+D-2-D*###WWD**DCD*D-'
    level.Fp[8]  = 'V+VVV   +VVVVVVVVVVVVVVVVVVVVVVVVVV  ##########################D'
    level.Fp[9]  = 'VV  +VVV VVCCXXXXXXXKXXXXXXCXXXXXXV  #K    3C/////////////3 ZX  '
    level.Fp[10] = 'VVVVVVVV+VVXXXX+XXXXXXXXXXXXXXXXXXV  #########################  '
    level.Fp[11] = '+  V +  VVVXXXXXXXXXXXXXXXXXXXXX+XV  R2 ==+ ==C/1111111/+ 2== 1 '
    level.Fp[12] = 'V V+VVVVVVVXXXXXXXXXXXXX+XXXXXXXXXV  R  +==. ==/1111111/ ==+  . '
    level.Fp[13] = '+VVVV + VVVXXXXXXX+XXXXXXXXXXXXXXXV  R ===== 2=/111B111/1 ====  '
    level.Fp[14] = 'V  + VVV+VV+XXXXXXXXXXXXXXXXXXX+XXV  R  ==  ===/1111111/   ==   '
    level.Fp[15] = 'VVVVVVV-VVVXXXXXXXXXXXXXXXXXXXXXXXV  R 1   == ./1111111/       1'
    level.Fp[16] = '111111-11V#WWW---=   ===   =-------  R===    1 /1111111/  1  ==+'
    level.Fp[17] = '11111-111V#WWW-3-= = =B= = =222222;  R+= .  =  /////////    ===='
    level.Fp[18] = '1111-1111V#-----3= = = = = =222222;  R  2  ===   .  +== .=   == '
    level.Fp[19] = '111-11111B#3-3-3-= = = = = =222222;  R ==   == 2   ====  ===2  1'
    level.Fp[20] = '11-111111V#-3-3-3= = = = = =222222;  R ===  1+==   === 2 +===   '
    level.Fp[21] = '1-1111111V#----3-= = = = = =222222;  RK ===  ==== 1   .    1    '
    level.Fp[22] = '-11111111V#+++--3= =+   += =222222;  RRRRRRRRRRRRRRRRRRRRRRRRR-X'
    level.Fp[23] = 'T-------KV#+++-3-- =======I ------- ZU2 U2 U2 U2 UK U2 U2 U2 U2X'
    Convert_Format(level)

def Level29(level: Level):
    level.Fp[1]  = 'P-----------:333333333333333:---------:C:::::::::::K:-----------'
    level.Fp[2]  = '-:-:-::;:::-:---------------;-:::-:::-:1-1-1-1-1-1-1:-:::::::::-'
    level.Fp[3]  = '-:-:--:2:C;-:-:#############:-:U:-:U:-:-1-1-1-1-1-1-:-:   C   :-'
    level.Fp[4]  = '-:-::::2:X:-:-2#invisimaze!#2-: :3:-:-:1-1-1-1-1-::::-:::::::::-'
    level.Fp[5]  = '-:---B:2:X:-:-:#############:-:-:-:-:-:::::-::::::---------::-:-'
    level.Fp[6]  = '-::::::2:X:-:-:.K-----------:-:-:Z:-:-:S----;------:::::::-::-:-'
    level.Fp[7]  = '-:K-2222:X:-:-:::::::::::::-:-:-:::-:-:::::-::::::::-----:----:-'
    level.Fp[8]  = '-::::::::X:-:+++++++++++++++:-:K::--:-:---:-:---:----:::-::::::-'
    level.Fp[9]  = '-XXXXXXXXX:-:::::::::::::::::-::::-::-:-:-:-:-:-:-::::::--------'
    level.Fp[10] = ':::::::::::---------W---------::---::-:-:---:-:-:-::---:-:::::::'
    level.Fp[11] = '--------::::::::::::::::::::::::-:-::-:-:::::-:-:-:C-:-:-::-----'
    level.Fp[12] = '-::::::-------------W------------:----:-------:-:-::::-:-::-:::-'
    level.Fp[13] = '--:::::::::::::::::::::::::::::::::::::::::::-:-:----:-:-::---:-'
    level.Fp[14] = ':-:-----33333333333----------+----------------:-::::-:-:-::::-:-'
    level.Fp[15] = '--:-::::;;;;;;;;;;;::::::::::::::::::::::-:::-:----:-:-:-3::3-:-'
    level.Fp[16] = '-::K::::----------------------------------:Z;-:-::-:-:T--::::-:-'
    level.Fp[17] = '--::::::::::::::::::::::::::1:1:1:1:1:1:1::-:-:-::-:-:::::3:3-:-'
    level.Fp[18] = ':-:W:----------------------::::::::::::::::-:-:-::-:-------::-:`'
    level.Fp[19] = '--:-:-:11111111:Z:;:::::::-:K-XXXXXXX3333333:1:-::-:::::::-:3-:`'
    level.Fp[20] = '-::-:-::::::::::::*******:-::::::::::::::::-:-:W::-------:-::-:`'
    level.Fp[21] = '--:-:-:CI`-------:*******:-:::EWWWWW--------:T::::::::::-:-:3-:`'
    level.Fp[22] = ':-:-:-::::::::::-:::::::::---::::::::::::::::::3333333:--:-::-:`'
    level.Fp[23] = '------------------+:Z-----------------------------------::----:L'
    Convert_Format(level)

def Level30(level: Level):
    level.Fp[1]  = 'K1VXXXXXXXXXXXXXXXX3333333333333K#333##Q...\\2-2-2-2-2-2-2-2-2-:R'
    level.Fp[2]  = '-1V  +++++++++++++3333333333333333333#######-2-2-2-2-2-2-2-2-2;R'
    level.Fp[3]  = '-1V  #########################------+##-2-2-2-2-2-2-2-2-2-2-2-:R'
    level.Fp[4]  = '-1V  F-----------------------I-------##2-2-2-2---2-2-2-2-2-2-2RR'
    level.Fp[5]  = '-1V--##################################-2-2-2--C--2-2-2-2-2-2ZRR'
    level.Fp[6]  = '-1V2-2-2-2VV++K++VV2-2-2-2-2-2-2-2-2-2-2-2-2-2---2-2-2-2-2-RRRRR'
    level.Fp[7]  = '-1V-2-2-2-VV++S++VV-2-2-2-2-2-----2-2-2-2-2-2-2-2-2-2RRRRRRRRRRR'
    level.Fp[8]  = '-1V2-2-2-2VVDVVVDVV2-2-2-2-2-2-K-2-2-2-2-2-2-2-2-RRRRRRRRRRRRRRR'
    level.Fp[9]  = '-1V-2-2-2-2-2-2-2-2-2-2-2-2-2-----2-2-2-2-2-2-RRRRRRRRRRRRRRRRRR'
    level.Fp[10] = '-1V///////-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-RRRRR##333333333XXR'
    level.Fp[11] = '--XXXXXX//2-VVVVV-2-2-2==================-2-RRRRRE##3333333333XR'
    level.Fp[12] = 'P X 33ZX//-2V+B+V2-2-2C==UDCDXDXDXDXDXDCD2-2RRRREAED3333B33333UR'
    level.Fp[13] = '--XXXXXX//2-VVVVV-2-2-2==================-2-RRRRRE##3333333333XR'
    level.Fp[14] = '-1V///////-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-RRRRR##333333333XXR'
    level.Fp[15] = '-1V-2-2-2-2-2-2-2-2-2-2-2-2-2-----2-2-2-2-2-2-RRRRRRRRRRRRRRRRRR'
    level.Fp[16] = '-1V2-2-2-2VVDVVVDVV2-2-2-2-2-2-K-2-2-2-2-2-2-2-2-RRRRRRRRRRRRRRR'
    level.Fp[17] = '-1V-2-2-2-VV++S++VV-2-2-2-2-2-----2-2-2-2-2-2-2-2-2-2RRRRRRRRRRR'
    level.Fp[18] = '-1V2-2-2-2VV++K++VV2-2-2-2-2-2-2-2-2-2-2-2-2-2---2-2-2-2-2-RRRRR'
    level.Fp[19] = '-1V;##################2-2-2-2-2-2-2-2-2-2-2-2--C--2-2-2-2-2-2ZRR'
    level.Fp[20] = '-1V1EEEEE1EEEEEE11EE###################2-2-2-2---2-2-2-2-2-2-2RR'
    level.Fp[21] = '-1V1EEEE1E1EEEE1EE1E##C+++++++3KKD***##-2-2-2-2-2-2-2-2-2-2-2-:R'
    level.Fp[22] = '-1VE1E11+EE11E1EEEE1##############***##2-2-2-2-2-2-2-2-2-2-2-2;R'
    level.Fp[23] = 'K1V+E1EEEEEEE1E+EEEE+*W*+C+*W*+K##S-----2-2-2-2-2-2-2-2-2-2-2-:R'
    Convert_Format(level)