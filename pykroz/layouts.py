from typing import Union
from pieces import What
from levels import LiteralLevel, RandomLevel

DungeonsLayouts: dict[int, Union[LiteralLevel, RandomLevel]] = {
    1: LiteralLevel([
        '        1    1     1  1     1     1   1      1        1         ',
        '   ---#######   1        1     1          1      1#######---   1',
        '   #        #1      1     1        1    1      1  #+ + + + #    ',
        '1  #   TT   #     1   1      1   1          1     # + + + +#1   ',
        '   #        #  1        1       1     1         1 #+ + + + #    ',
        '   ##########       1     1         1     1   1   ##########  1 ',
        '1   1       1     1    1      1         1       1      1       1',
        '  1      1      1                         1       1     1    1  ',
        '   1    1   1      1   XXXXXXXXXXXXXXX     1   1     1        1 ',
        '      1      1   1     XXXXX  I  XXXXX   1      1   1    1      ',
        '1   1    1    1    1   XXXX+     +XXXX    1   1       1        1',
        ' 1      1  1    1      XXXX+  P  +XXXX   1      1      1    1   ',
        '    1     1  1     1   XXXX+     +XXXX     1      1  1    1    1',
        ' 1   1     1     1     XXXXX  S  XXXXX   1    1       1      1  ',
        '1      1 1    1        XXXXXXXXXXXXXXX      1   1       1     1 ',
        '  1     1  1      1                      1     1    1      1    ',
        '    1       1    1     1     1     1    1     1       1 1      1',
        '1  ##########1    1   1    1    1     1      1   1########## 1  ',
        ' 1 # W W W W# 1        1    1     1      1 1      #        #    ',
        '1  #W W W W #   1   1    1     1     1         1  #   LL   #  1 ',
        '   # W W W W#1       1    1        1   1     1    #        #    ',
        '1  ---#######    1     1    1 1     1     1     1 #######---    ',
        '        1    1     1            1  1     1     1        1      1'
    ]),

    2: RandomLevel([
        (What.SlowMonster, 200),
        (What.MediumMonster, 5),
        (What.Breakable_Wall, 100),
        (What.Stairs, 2),
        (What.Chest, 1),
        (What.SlowTime, 1),
        (What.Gem, 40),
        (What.Key, 1),
        (What.Wall, 50),
        (What.TeleportTrap, 5)
    ]),

    3: LiteralLevel([
        '+++##############RRRRRRR###         ##sm######TVVVVT##K-        ',
        '+C+D       +    K#RRRRRRR##    C    ##was#### VVVVVV ###      # ',
        '+++######## ####1#RRRRRRR##         ##here## VVV++VVV ##333333# ',
        '########### #####1#RRRRRRR#####T########### VVV++++VVV1######## ',
        '         +# #2####1#RRRRRRR######+# #K# #3#1VVV++++VVV       2KC',
        ' # ######## ##+####+#RRRRRRR###....# # # ### VVV++VVVV #X###### ',
        '3# #######  ###+#####RRRRRRR## ############## VVVVVVV ##X##C### ',
        ' # ###### # ####+#####RRRRRRR##  ##+:   :+#### VVVVV ###X##X### ',
        '.# #T### ## #####+####XRRRRRRRX## #   :  :#####     ###TTT#X### ',
        '.# # ##+### ######+###XXXXXXXXX# ## ::::: ####### # #######X### ',
        '.# # # ###                          :+K+:         # #XXXXXXX###+',
        '.# # C###   P  ###### ###XXXXXXXXX# ::;:: ####### # #XXXXXX####D',
        '.# #3#### ////####### ###XRRRRRRRX#:: :   ###VW## # #XXXXX##WWWW',
        '.# ###////\\\\\\//###### ####RRRRRRR##+ :  :+###TV## # #XXXX##KWWWW',
        '.# ##//\\\\\\\\C\\//////## ##T##RRRRRRR###########V+## #     ####WWWW',
        '.# ##///\\\\\\1\\////###+ #+-+##RRRRRRR##cavern## V## ###///########',
        ' # ###///\\\\\\//#####+# #---###RRRRRRR##of#####V ## #222222222\\###',
        ' #  Q###//// #####+## #-C-#Z#RRRRRRR#tunnels# V## #222222222\\1 #',
        ' ########### ####+### #---#3##RRRRRRR########V ## #222222222\\#D#',
        '          I  ###2#### #2-2# ##RRRRRRR####  ## V## #222222222##D#',
        '##################### ##/## ###RRRRRRR## ## #V ## #222222222##D#',
        '22222222222222222222#       ####RRRRRRR# ###X V## #222222222##D#',
        'K + + + + + + + + +   ###########RRRRRRR#++##V    \\---------##L#'
    ]),

    4: RandomLevel([
        (What.MediumMonster, 200),
        (What.Whip, 38),
        (What.Stairs, 2)
    ]),

    5: LiteralLevel([
        '//1////////\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\11111\\C\\1111111\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\XXCCC',
        '/////////1//\\\\\\\\1\\\\\\\\\\\\\\\\\\\\\\\\111\\\\\\111111\\\\XXX\\\\\\1\\\\\\\\\\\\\\/1XXCCC',
        '///RRR///////\\\\\\\\\\\\\\\\\\\\\\\\\\\\Z\\\\111111111\\\\\\\\XLX\\\\\\\\\\\\\\\\\\\\///XXXXX',
        '//RRRRRR//////\\\\\\\\\\\\U\\\\\\\\1\\\\\\\\\\\\11111\\\\\\\\\\\\XXX\\\\\\\\\\/////////////',
        '///RRRR///////\\\\\\1\\W W\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//////1//////////',
        '/1//RR//XXXX/1//\\\\\\\\\\\\\\\\\\\\\\\\1\\\\\\\\\\\\\\\\\\\\//1/////////////////1////',
        '////////XCCX1//1////\\\\\\\\\\\\\\\\\\\\\\\\///////////////1////////////////',
        '////////XXXX/////////////////1////////////////////////XXXXXXXXXX',
        'XXXX///////////////1///////////////XXXXXXXXXXXXXXXXXXXX=========',
        '===XXXXXXXXXXX/////////XXXXXXXXXXXXX============================',
        '=============XXXXXXXXXXX========================================',
        '======================================================  1     ; ',
        'K11 111===============================W       1  W        W   : ',
        '1 1111 11 1    1       W        1         RR                  : ',
        '111 1111 11 1              W            RRRRR       W         : ',
        '1 1111 1111       1               W      +RRRRR               : ',
        '111 1111 1   1            1              RRRRRRRR1         W  : ',
        '1 1111 1111   B         W                 +RRRRRRR           1: ',
        '111 1111 111 1                      W     RRRRRRR    W        : ',
        '11 11 1111       1          W        1   RRRRRR         1     : ',
        ' 111111 1    1      W                     RRR1           W    : ',
        '111 11 111 1    1         P                      W            :`',
        '1 11111 111  1       W            W                   W      I:U'
    ]),

    6: RandomLevel([
        (What.FastMonster, 180),
        (What.Breakable_Wall, 50),
        (What.Stairs, 2),
        (What.Gem, 75)
    ]),

    7: LiteralLevel([
        ' I                3+             3+             3+             3',
        'PI                3+             3+             3+             3',
        ' I                3+             3+             3+             3',
        '############################################################### ',
        '+      ;K ##33333 33333##2 222 22222##111111 1111##..  ..     . ',
        ';;; ;; ;; ##3 33333 333##222222 2222##1 111111 11##  .. .....   ',
        'U;;  ;  ; ##33 33U333 3## 2222U22 22##11111U1111 ## ....########',
        '  ;; ;; ; ##3333 333333##222 2222222##11 1111 111##. .. U    3..',
        '; I  ;;   ##3 3333333 3## 2222222 22##1 11 111111##.    #     .C',
        ' ###############################################################',
        '                     W;33333333333333333333333333333333333333333',
        '  ###########################################W         K    ++++',
        'Z                                T                             1',
        '  ##############################################################',
        '    # #+# #1# #+# #1# # #E#+# # #1# # #1# #;# #1# # # #+# #;# ##',
        '  ## # #E# # #1# # # #;# # # # # # #E# #+#1# # #;# #1# #1#E# #T#',
        '  # # # #;# # # #1# #+#1# # #1# # # # #1# # # # # #E# # # #;#Q##',
        '  ## #1# #+# # # #E# # # #1#;# #+# # #;# # #1#E#+# # #;# # #E#T#',
        '    # # # # #1# # # #1# # # # # # #1# # #E# # #1# #1# # #1# # ##',
        '  ##############################################################',
        '  ###K     ;      3    +:    3     :+3       +: 3    :+     +  3',
        '  ##########  ##   :+  3  +    :+      :+     3  +:+     3  ::::',
        '              ##3         3 +:    3 +   3  :+      3   :+  :D`DL'
    ]),

    8: RandomLevel([
        (What.Whip, 20),
        (What.Stairs, 2),
        (What.Chest, 1),
        (What.Gem, 40),
        (What.Invisibility, 35),
        (What.TeleportScroll, 2),
        (What.TeleportTrap, 5),
        (What.Tree, 990),
        (What.Tunnel, 3)
    ]),

    9: LiteralLevel([
        'K            3-      33333VVVVVVVVVVVV    .         .       .  Z',
        '     3-     ---     33VVVVVVVVVVVVVVZ          .                ',
        '3-  ---           333VVVVVVVVVVVVVVVVVV  .        U   .      .  ',
        '--              333VVVVVVVVVVVVVVVVVVVVVW    .           .      ',
        '          3-   33VVVVVVVV\\\\\\\\\\\\\\\\VVVVVVVVVV         .        VVV',
        '   3-    ---  33VVVVVVV\\\\++++W+++\\\\VVVVVVVVVV   .    ZVVVVVVVVVV',
        '  ---        33VVVVVVV\\++\\\\RRRR\\\\+++\\\\VVVVVVVVVVVVVVVVVVVVVVVVVV',
        '3-       U  33VVVVVV\\\\+\\\\RRRRRRRRRR\\++\\\\VVVVVVVVVVVVVVVVVVVVVVVC',
        '--         33VVVVVV\\\\+\\RRRRRR////RRRR\\+\\\\\\VVVVVVVVVVVVVVV1111111',
        '      333333VVVVVV\\\\+\\RRRR////11///RRR\\++\\\\VVVVVVVVV111111111111',
        '  33333VVVVVVVVVV\\\\+\\\\RRR///11   1//RRRR\\+\\\\VVVV1111111111111111',
        '333VVVVVVVVVVVVV\\\\\\W\\RRR//C111 P 11//RRR\\W\\\\\\VVV1111111---111111',
        'VVVVVVVVVVVVVVVVV\\\\\\+\\RRR//111   11//RRR\\+\\\\VVVV1111111-B-111111',
        'VVVVVVVVVVVVVVVVVV\\\\\\+\\RRR//111U11//RRR\\\\+\\VVVVVV111111---111111',
        'VVVVV3 .  3  VVVVVVV\\\\+\\RRR////////RRRR\\+\\\\VVVVV1111111111111111',
        '3-.     -- .  VVVVVV\\\\\\+RRRR//////RRRR\\+\\\\VVVVV11111111111111---',
        '--   - .3- --- VVVVVVV\\\\+\\RRRRRRRRRRR\\+\\\\VVVVV111111111111111- U',
        '  - 3-  --.-3-. VVVVVVVV\\++\\RRRRRR\\\\++\\VVVVVV1111111111111111---',
        ' 3.        ---   VVVVVVVVV\\++++W++++\\\\VVVVVV111111---11111111111',
        '       U  3   3-  .VVVVVVVV\\\\\\\\\\\\\\\\VVVVVVVV1111111-B-11111111111',
        '.  --.      - --.  - VVVVVVVVVVVVVVVVVVVVV11111111---11111111111',
        '   3 --    3   -- 3-  ##VVVVVVVVVVVVVVVVV11111111111111111111111',
        ' .   3  .    . 3-   . D+DLVVTTCCCTTVVVCC11111111111111111111111K'
    ]),

    10: RandomLevel([
        (What.MediumMonster, 400),
        (What.Stairs, 1),
        (What.Gem, 20),
        (What.Freeze, 1),
        (What.Quake, 35)
    ]),

    11: LiteralLevel([
        '                                                        WWWW  3S',
        'U################# #################################`###########',
        ' :3; \\3+#3 W    K#3  #  W  W  W  W  W  W  W  W  W  #   3     3  ',
        'Z:+: \\3+# 3      #3  #  /////////////////////////  #      3     ',
        ' :3; \\3+#    3   #3  #  /+//////+/////T///////+//  #            ',
        ' :+: \\3+#        #3  #  ////T/////////////+////// 3#  3 ::;:  3 ',
        ' :3; \\3+# 3  3   #3  # 3//////////W//////////////  #    :CC:    ',
        ' :+: \\3+# W      #3  #  //+//////////////////+///  #    ;:::    ',
        ' :3; \\3+#      3 #3  #  ///////+///////+/////////3 #3         3 ',
        ' :+: \\3+#3       #3  #3 /////////////////////////  #       3    ',
        ' :3; \\3+#W   3   #3  #  ///+//////XXXXX////W/////  #  3       3 ',
        'P:C: \\3K#       3#3  #  ////////+/XXKXX+/////////  #############',
        ' :3; \\3+# 3      #3  #  //////////XXXXX////////+/ 3#3         ++',
        ' :+: \\3+#     3  #3  # 3/+////////+///////T//////  #3+        ++',
        ' :3; \\3+#  3W    #3  #  /////////////////////////  #3+          ',
        ' :+: \\3+#        #3  #  /////T//////+////////+///  #3+      ::::',
        ' :3; \\3+# 3    3 #3  #3 /////////////////////////3 #3+      ```L',
        ' :+: \\3+#        #3  #  //W//////////////+///////  #3+      ::::',
        ' :3; \\3+#W   3   #3  #  /////+////+///////////+//  #3+          ',
        'S:+: \\3+#3       #3  #  /////////////////////////  #3+        ++',
        ' :3; \\3+#        #3 K#                             #3         ++',
        'U### ####I########################## ###############E###########',
        '                                                        ++++  3S'
    ]),

    12: RandomLevel([
        (What.SlowMonster, 100),
        (What.MediumMonster, 75),
        (What.FastMonster, 50),
        (What.Breakable_Wall, 100),
        (What.Whip, 10),
        (What.Stairs, 1),
        (What.Chest, 1),
        (What.SlowTime, 1),
        (What.Gem, 30),
        (What.TeleportScroll, 1),
        (What.Key, 1),
        (What.Bomb, 5),
        (What.Invisible_Breakable_Wall, 100)
    ]),

    13: LiteralLevel([
        'KKKKDE EI .  I  E    2  I   E  RRCC211///////// ////////////T//K',
        'VVVVVE     2    I    .     .   RR22211//////// / ///////////2// ',
        '  E  I .    E  .     E  .    2 RR11111///   / ///      /////2// ',
        '2  . 2  E .     E2  . I    I   RR//////// // ////////// ////2// ',
        '  I   .    I   I .        .    RR//////// /////222////// ///2// ',
        'E .   I E  .2  E    E .    E   RR/////T// /////2P2/   /// //2// ',
        ' 2   E  . I    .   I   I .    ERRC/////// /////222/ // /// / // ',
        'I   .    2 E.  E     .      I  RR//////// ////// // // ////  // ',
        '.E I    .    I    2   E     .2 RR//////// ///////  ///I///// // ',
        '   . 2     .      . I          RR//      1/ ////////// ////// / ',
        '2I   . E   I  2.I  E      I.  \\\\\\\\ /////// /           ///////  ',
        'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\\ZZ\\RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR',
        '22--2-2--2--2-+--22----2-2---2\\\\\\\\VVVVVVVVVVVTVVV W VVVVVVTVVVVV',
        '--2-2--2-2-2---2---2-2-+2---2--RR   .VVVVVVVVV + VVVTVVVV V VVVV',
        '+2-2--2---2-2---22---2---2----2RRV     . VVVVVVVVVVVV VV VVV   V',
        '2--+-2--2--+--22---2--+-2---2-+RRVV.  .     .VVVVVVVV V VVVVVV V',
        '-2--2-2--2---2-+-22----2--2----RRVVVV    .       .VVVV  VVVV TVV',
        '2-2--2--2-+2--B-2---2-+-2--+-2-RRVVVVVV  .   .      VVVVVVV VVVV',
        '2+-2---2--2--2-2--2---2--2-----RRVVVVVVVV         .   .VVVVV VVV',
        '-22-+-2--2-2---22--+-2--2-2-2--RRVVVVVVVVVV .            .V VVVV',
        '2---2---2-2--2-+-2----2----2--+RRVVVVLDVVVVVV  .    .     . VVVV',
        'VVVV2--2-+-2-2----2--2-2-2-2---RRCCVVVVDVDDVD                VVV',
        'KKKD-2---2-2--2-2---2-+-2--2--2RRCCVVVVVDVVDVV222222222222222DKK'
    ]),

    14: RandomLevel([
        (What.FastMonster, 170),
        (What.Whip, 5),
        (What.Stairs, 1),
        (What.Chest, 1),
        (What.Gem, 25),
        (What.Invisibility, 500),
        (What.TeleportScroll, 1),
        (What.Wall, 50),
        (What.SpeedTime, 50),
        (What.TeleportTrap, 50),
        (What.WhipPower, 1),
        (What.Bomb, 1),
        (What.Tunnel, 28),
        (What.Quake, 1)
    ]),

    15: LiteralLevel([
        '+*****#3#L#+ \\    2    \\ 2   2   W#CCCC#=C;=====    ====        ',
        '+**Q**# #D#     \\/  2 \\\\     //   ##33##=;;===== === == ======= ',
        '+*****# #D#\\\\  //\\/   \\     \\\\// 2#\\33\\#===I=.  === ==== ===== =',
        '2###### #X#2  2 ///     2    //   #\\33\\#====  .=== ====== === ==',
        '2D33V  ##X#\\\\       2   \\/     2  #\\33\\#===. .=== ======= == ===',
        '2#33#C##X##\\/\\  2 /\\     2   /\\   #\\33\\#==.  ==== ==  S  == ====',
        '2#33#.##X#W\\/\\\\      2  \\\\\\   //  #\\;;\\#== ====== == ======11111',
        '2#33#.##X#/\\B      \\/  \\\\/   2  2 #\\  \\#== ====== === =====11111',
        '2#33#.###X\\///  ///   2 \\\\        #X  X#=== ===== ==== ====11111',
        '2#33#.#####+\\//2/\\//         \\\\ 2 #X  X#=    ==== ===== =======;',
        '2#33#.##X##++\\////   2\\  \\  //\\\\  #X  X#= ======= W  : ======= =',
        '2#33#.##XX##         \\/\\ 2   \\\\2  #X  X#== ====== 2    ====== ==',
        '2#XX#.##XXX######## 2          ---#X  X#= ================ W ===',
        '2#XX#.##XRRRRRRRRR##########2  - U#X  X# ====    ===1==== ======',
        ';#XX#.##XRRRRRRRRRRRRRRRRRR########X  X#= == ==== == ==== ======',
        ' #XX#.##XXRRRRRRRRRRRRRRRRRRRRRRRR#X  X#=K==    ==   =====   ===',
        ' #XX#.##X##11RRRRRRRRRRRRRRRRRRRRR##  ########== ==== ======= ==',
        'Z#XX#.####11111111111111RRRRRRRRR##  ##RRRRRR###= ==== ======= =',
        ' #XX#.###11111111111111111111RRR##  ##RRRRRRRRR#== === ======== ',
        ' #XX#.##11111111111111111111111##  ##RRRRRRRRRR##== == ======== ',
        ' #CK#.##11111111B111111111B11111111##RRRRRRRRRRR#   == ======= =',
        'P####X##111111111111111111111111111111RRRRRRRRRRU#====   ==== ==',
        '       /-------------C----------------URRRRRRRRRRR#======      T'
    ]),

    16: RandomLevel([
        (What.MediumMonster, 60),
        (What.Stairs, 1),
        (What.SlowTime, 6),
        (What.Gem, 30),
        (What.Invisibility, 20),
        (What.SpeedTime, 1),
        (What.Lava, 550),
        (What.Tunnel, 4),
        (What.Nugget, 5),
        (What.Quake, 2)
    ]),

    17: LiteralLevel([
        '     2    KRR++                P RRRRRRRRRRRR                   ',
        ' RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR      -         RRRRRRRRRRRRRRR  ',
        '                    ++++++C 3RR  RRRRR1 RRRRR  RRCE             ',
        ' RRRRRRRRRRRRRRRRRRRRRRRRRR  RR  RRC1RRRR 1RR  RRRRRRRRRRRRRRRRR',
        '2222222222           ZRRTRRRRRR  RR  -     -       XXXXXXXXXXXKR',
        '--RRRR--RRRRRRRRRRRRRRRR     RR33RRRRRRRRRRRR  RR  RRRRRRRRRRRRR',
        '  RR-----------..*****RRRRR    **         +RR  RR             RR',
        '  RR--RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--RRRRRRRRRRRRR  RR',
        '  RR--RR11111111----------D+DWD+DWD+DWLLRR333          2CBRR  RR',
        '  RR--RR11111111RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR  RR',
        '  RR--RR--RRRRRRRR  DT+*W*+TCRRZ1                             RR',
        '  RR--RR--RRII.KRR  RRRRRRRRRRRRRRRRRRRR  RRRRRRRRRRRRRRRRRRRRRR',
        '  RR--RR--RRIIRRRR                        RRU1-------XXXXXXXXX  ',
        '  RR--RR--RRIIRRRRRRRRRRRRRRRRRRRRRR  RR  RRRRRRRRRRRRRRRRRRRR  ',
        '  RR--RR--RR..RR 1RR 1RR 1RRR         RR                        ',
        '  RR--RR--RRIIRR  -   -   -    RRRRRRRRR  RRRRRRRRRRRRRRRRRRRRRR',
        '  RR------RRIIRR  RRRRRRRRRRR  RR  ;W;W;           22222222CRRK ',
        '  RRRRRRRRRRIIRR         2KRRWWRR  RRRRRRRRRRRRRRRRRRRRRRRRRRR--',
        '         -    RRRRRRRRRRRRRRRRRRR  RRXXXXXXXXXXXXXC3333333333333',
        '  RRRRR 1RRR          1            RR--RRRRRRRRRRRRRRRRRRRRRRR- ',
        '  X  RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--URRCCRRCCRRXXXXXX333333  ',
        '--RR              RRRRRRRR    2   KRR- RRR..RR..RR**RR**RR**RR  ',
        '33RRRRRRRRRRRRRR   *    *   RRRRRRRRR--E.E******RRK*RR**RR**RR  '
    ]),

    18: RandomLevel([
        (What.SlowMonster, 100),
        (What.Whip, 3),
        (What.Stairs, 1),
        (What.Chest, 1),
        (What.Gem, 20),
        (What.TeleportScroll, 2),
        (What.TeleportTrap, 5),
        (What.Bomb, 1),
        (What.Tunnel, 4),
        (What.Nugget, 20),
        (What.Invisible_Breakable_Wall, 850)
    ]),

    19: LiteralLevel([
        '1  C  1      +   1   +        +  1      +     + 1 RRR++++++RRRRL',
        '--   ---  1     ---        1    ---  1         ---RRRR++++++RRRD',
        ' 1       ---RRRRRR    1   ---       ---    W      RRRR;;;;;;RRR1',
        '---  *  1 RRRRRRRRRR1---       1       1       1  RRRR111111RRR1',
        '1      RRRRR#####RRRRRR 1     ---     ---   1 ---RRRRR111111RRR1',
        '--1   RRRRRR#U K#RRRRR ---  1      T       ---  RRRRRR11111RRRR1',
        ' ---   RRRRR#####RRR       ---           1    #RRRRRR#11111RRRR1',
        '    1    RRRRRRRRRR  1           1      ---   ########11111RRRR1',
        ' * ---    RRRRRRRR  ---         ---   1       D--Z---`11B11RRRR1',
        '      1    RRRRR            W        ---      ########111111RRR1',
        '     ---                                      #RRRRRR#111111RRR1',
        '               ;;;;;;;;;;;;;;;;;;;;;;;;;;;;; FFRRRRRR1111111RRR1',
        '#############################################;;;RRRRR11111111RR1',
        '    #++#W3#* #  # *##::::::+::::K:::::::::::#1111RRRRR1111111RR1',
        ' #  #3 #3 #        ##:3::::::::-::::::3:::::#11111RRRRR111111RR1',
        'P#  #  #  #3 #  #  ##:::::::::-:::3:::::::::#11111RRRRR111111RR1',
        ' #3 #  K  #  #  #3 ##::::::::-::::::::::::::#11111RRRRR11B111RR1',
        'I#  #  #  #  # 3#  ##:::3:::-:::::::::::3:::#11111RRRRR11111RRR1',
        ' #  #  #  #  #  #  ##::::::;::::::::*:::::::#1111RRRRRR11111RRR1',
        'Z#  #  # 3# 3#  #  ##///////////////////////#1111RRRRR11111RRRR1',
        ' #     #  #  #3 #                           #EEERRRRRR11111RRRR1',
        'C# 3#  #  #  #**#  ##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#+++RRRRR;;;;;;RRRR ',
        '3#+ #3*#3    #**#+3##33333333333333333333333#CCRRRRRRR*-U-*RRRRU'
    ]),

    20: RandomLevel([
        (What.MediumMonster, 550),
        (What.Breakable_Wall, 650),
        (What.Whip, 5),
        (What.Stairs, 1),
        (What.Chest, 1),
        (What.Gem, 5),
        (What.TeleportScroll, 1),
        (What.Key, 1),
        (What.TeleportTrap, 1),
        (What.Bomb, 1),
        (What.Nugget, 20),
        (What.Quake, 8)
    ]),

    21: LiteralLevel([
        'LVVVVVVVVVVVVVVVVVVVVVV333333333333333333VVVVVVVVVVVVVVVVVVVVVVK',
        'DVVVVVVVVVVVVVVVVVVVV333                333VVVVVVVVVVVVVVVVVVVVI',
        '.VVVVVVVVVVVVVVVVVV333         ***        333VVVVVVVVVVVVVVVVVV-',
        'DVVVVVVVVVVVVVVVV333         *******        333VVVVVVVVVVVVVVVV-',
        '.VV+VVVVVVVVVVV333          ****F****         333VVVVVVVVVVV+VV-',
        'DVQ+VVVVVVVVV333   +         *******         +  333VVVVVVVVV+CV-',
        '-VV+VVVVVVV333        +        ***        +       333VVVVVVV+VV-',
        '-VVVVVVVV333             +             +            333VVVVVVVV-',
        '-VVVVVV333      Z                              T      333VVVVVV-',
        '-VVVV333                     -------                    333VVVV-',
        '-VV333                      ---------                     333VV-',
        'E33C3         +    +    +  -----P-----  +    +    +        3C33E',
        '-VV333                      ---------                     333VV-',
        '-VVVV333                     -------                    333VVVV-',
        '-VVVVVV333      T                              Z      333VVVVVV-',
        '-VVVVVVVV333             +             +            333VVVVVVVV-',
        '-VV+VVVVVVV333        +        ***        +       333VVVVVVV+VV-',
        '-VC+VVVVVVVVV333   +         *******         +  333VVVVVVVVV+CV-',
        '-VV+VVVVVVVVVVV333          ****F****         333VVVVVVVVVVV+VV-',
        '-VVVVVVVVVVVVVVVV333         *******        333VVVVhelp!VVVVVVV-',
        '-VVVVVVVVVVVVVVVVVV333         ***        333VVVVVVVVVVVVVVVVVV-',
        '.VVVVVVVVVVVVVVVVVVVV333                333VVVVVVVVVVVVVVVVVVVVF',
        'KVVVVVVVVVVVVVVVVVVVVVV333333333333333333VVVVVVVVVVVVVVVVVVVVVVK'
    ]),

    22: RandomLevel([
        (What.FastMonster, 300),
        (What.Stairs, 1),
        (What.Invisibility, 300),
        (What.SpeedTime, 150),
        (What.TeleportTrap, 150),
        (What.Bomb, 1),
        (What.Nugget, 300)
    ]),

    23: LiteralLevel([
        'L UD*D*D*D*D------------------------;;;;;;;;;;;;;;;;;;;;;;;;;;;;',
        '############-----------------##-####                           S',
        '+2222K2222+#11111111111111111##-22X# XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        '+222222222+#-----------------##-22X# XXXXXXXXXXXXXXXXXXXXXXXXXXX',
        '+222222222+#22222222222222222##-2XX#                            ',
        '2/////////2#-----------------##-2XK#----------------------------',
        '2/W--W--W/2#33333333333333333##-22X#2222222222222222222222222222',
        '2/-------/2#-----------------##-22X#2222222222222222222222222222',
        '2/---P---/2#22222222222222222##-2XX#2222222222222222222222222222',
        '2/---B---/2#-----------------##-2X+#----------------------------',
        '2/-------/2#1111111-K-1111111##-22X#3333333333333333333333333---',
        '2/-------/2####################-22X#333333333333333333333333----',
        '2/W--W--W/2#--1111111111111-+##-2XX#3333------33333-------------',
        '2/////////2#Q-------------------2X+#333--------333----------I--3',
        '2222#Z#2222################# ##-22X#33----------3--------------3',
        '2222#-#2222#=------======K==-##-22X#3-----33---------33333333333',
        '#####-######*-=====-====-=-=-##-2XX#3----3333-------333333333333',
        'C222/-/2222#==----==--==-==--##-2X+#3---333333-----3333333333333',
        '2222/-/////#=====-====-=-====##-22X#3---3333333333333333--------',
        '2222/-;;;;;;-==---==--==-=---##-22X#3---333333333333333--*+*+*+K',
        '///////////#=-=-===-=====-==-##-2XX#---------------------#######',
        'C2222222222#W---====-----===S##-2XC#+--------------------##22222',
        '####################################:::::::::::::;:::::::##X222U'
    ]),

    24: RandomLevel([
        (What.MediumMonster, 305),
        (What.Whip, 5),
        (What.Stairs, 1),
        (What.Chest, 1),
        (What.Gem, 5),
        (What.TeleportScroll, 1),
        (What.SpeedTime, 1),
        (What.Tunnel, 2),
        (What.Nugget, 5),
        (What.Stop, 999)
    ]),

    25: LiteralLevel([
        'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVVVVVVVVVVVVVVVVVVVVVVCC',
        'VRRRRRVVVVVVVVV VVVVV VVVVVVVVVVVVVVV V VVV**VVVVVV*****VVVVVVCC',
        'VRU KRVVV**VVV V VVV VIVVV*****VVVVV VVV V**VVVVVV V*****VVVVVVV',
        'VRRRRRVVVV**V VVV V VVV V*****V VVV VVVVV VVVVVVV VVV*****VVVVVV',
        'VVVVVVVVVVVV VVVVV VVVVV*****VVV V VVVVVVV V V V VVV VVVVVVVVVVV',
        'VVVVVVVVVVV VVVVVVV**VVVVVVVVVVVV VVVVVVVVV V3V VVV VVVVVVVVVVVV',
        'VVVV VVVVV VVVVVVVVV**VVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVRRRRRVVVV',
        'VVV V VVV3V VVV VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV VVVRU KRVVVV',
        '***VVV V VVV V V VVVV##########XX##########VVVVVVV VVVVRRRRRVVVV',
        'V***VVV VVVVV VVV VVVl#IIIIIIIIIIIIIIIIII##VVVVVV V**VVVVVVVV**V',
        'VVVVVVTVVVV**VVVVV VVa#I#####IIIIII#####I#pVVVVV VVV**VVVV V**VV',
        'VVVVV VVVV**VVVVV VVVv#I#LD+DIIIIIID-PU#I#iVVVV VVVVVVVVV V VVVV',
        'VVVVVV VVVVVVVVV VVVVa#I#####IIIIII#####I#tV***VVVVVVVVVTVVV VVV',
        'VVVVVVV VVVV*****VVVV##IIIIIIIIIIIIIIIIII#!VV***VVVVVVV VVVVV VV',
        'VVVVVV VVVVVV*****VVV##########XX##########VVV***VVVVV VVVVVVV V',
        'VVVVV VVVVVVVV*****VVVVVVVVVVVVVVVVVVVVVVVVVVVV***VVV VVV VVVVV ',
        'VVVVVV****VVVV VVVVVVVVVVVVVVVVVVVVVVVVVV VVVVVVVV V VVV V VVV V',
        'VVVVV****VVVV VVVVVVVV***VVV V V V VVVVV V VVVVVVVV VVV VVV V VV',
        'VVVV****VVVVVV3VVVVVVVV***V V V V V VVVIVVV3VVVVVVVVVV VVVVV VVV',
        'VVVVVVVVVVVVVVV V VVVVV VV VVVRRRRRV V VVVVV VVVVVVVV VVVV**VVVV',
        'VVVVVVVVVVVVVVVV V VVV VVVVVVVRU KRVV VVVVVVV VVV****VVVV**VVVVV',
        'VVVVVVVVVVVVVV**VVV V VVVVVVVVRRRRRVVV**VVVVVV V****VVVVVVVVVVVC',
        'CCCCVVVVVVVVV**VVVVV VVVVVVVVVVVVVVVVVV**VVVVVV****VVVVVVVVVVVCC'
    ]),

    26: RandomLevel([
        (What.MediumMonster, 200),
        (What.FastMonster, 30),
        (What.Whip, 25),
        (What.Stairs, 2),
        (What. Chest, 1),
        (What.SlowTime, 2),
        (What.Gem, 20),
        (What.Invisibility, 1),
        (What.TeleportScroll, 2),
        (What.TeleportTrap, 10),
        (What.WhipPower, 1),
        (What.Bomb, 5),
        (What.Pit, 785),
        (What.Tunnel, 10),
        (What.Nugget, 15)
    ]),

    27: LiteralLevel([
        '3     +=     =+=    =  1=  =+=  =     -   -2   -    -2    -  Z-2',
        '3 P =   =   =   1==  =    =   = 1=    -2  -    -2   -    K-2  - ',
        '##################################   ###########################',
        '3 3 3 3 3**********************K##   ##LVSDCD++D*D++D##D1****DDC',
        '   K C############################   ##VV+DCD########**######D#D',
        '          V V  V  V V V   VV   V V   ##ITFD##---D*DID###**DCD*D-',
        'VXVVVVVVVVS  VV V    V V V  V V V    ##ZW*.+D-2-D*###WWD**DCD*D-',
        'V+VVV   +VVVVVVVVVVVVVVVVVVVVVVVVVV  ##########################D',
        'VV  +VVV VVCCXXXXXXXKXXXXXXCXXXXXXV  #K    3C/////////////3 ZX  ',
        'VVVVVVVV+VVXXXX+XXXXXXXXXXXXXXXXXXV  #########################  ',
        '+  V +  VVVXXXXXXXXXXXXXXXXXXXXX+XV  R2 ==+ ==C/1111111/+ 2== 1 ',
        'V V+VVVVVVVXXXXXXXXXXXXX+XXXXXXXXXV  R  +==. ==/1111111/ ==+  . ',
        '+VVVV + VVVXXXXXXX+XXXXXXXXXXXXXXXV  R ===== 2=/111B111/1 ====  ',
        'V  + VVV+VV+XXXXXXXXXXXXXXXXXXX+XXV  R  ==  ===/1111111/   ==   ',
        'VVVVVVV-VVVXXXXXXXXXXXXXXXXXXXXXXXV  R 1   == ./1111111/       1',
        '111111-11V#WWW---=   ===   =-------  R===    1 /1111111/  1  ==+',
        '11111-111V#WWW-3-= = =B= = =222222;  R+= .  =  /////////    ====',
        '1111-1111V#-----3= = = = = =222222;  R  2  ===   .  +== .=   == ',
        '111-11111B#3-3-3-= = = = = =222222;  R ==   == 2   ====  ===2  1',
        '11-111111V#-3-3-3= = = = = =222222;  R ===  1+==   === 2 +===   ',
        '1-1111111V#----3-= = = = = =222222;  RK ===  ==== 1   .    1    ',
        '-11111111V#+++--3= =+   += =222222;  RRRRRRRRRRRRRRRRRRRRRRRRR-X',
        'T-------KV#+++-3-- =======I ------- ZU2 U2 U2 U2 UK U2 U2 U2 U2X'
    ]),

    28: RandomLevel([
        (What.SlowMonster, 133),
        (What.MediumMonster, 133),
        (What.FastMonster, 133),
        (What.Stairs, 3),
        (What.Chest, 3),
        (What.Gem, 80),
        (What.Invisibility, 420),
        (What.TeleportScroll, 1),
        (What.Key, 1),
        (What.Nugget, 10),
        (What.Quake, 5)
    ]),

    29: LiteralLevel([
        'P-----------:333333333333333:---------:C:::::::::::K:-----------',
        '-:-:-::;:::-:---------------;-:::-:::-:1-1-1-1-1-1-1:-:::::::::-',
        '-:-:--:2:C;-:-:#############:-:U:-:U:-:-1-1-1-1-1-1-:-:   C   :-',
        '-:-::::2:X:-:-2#invisimaze!#2-: :3:-:-:1-1-1-1-1-::::-:::::::::-',
        '-:---B:2:X:-:-:#############:-:-:-:-:-:::::-::::::---------::-:-',
        '-::::::2:X:-:-:.K-----------:-:-:Z:-:-:S----;------:::::::-::-:-',
        '-:K-2222:X:-:-:::::::::::::-:-:-:::-:-:::::-::::::::-----:----:-',
        '-::::::::X:-:+++++++++++++++:-:K::--:-:---:-:---:----:::-::::::-',
        '-XXXXXXXXX:-:::::::::::::::::-::::-::-:-:-:-:-:-:-::::::--------',
        ':::::::::::---------W---------::---::-:-:---:-:-:-::---:-:::::::',
        '--------::::::::::::::::::::::::-:-::-:-:::::-:-:-:C-:-:-::-----',
        '-::::::-------------W------------:----:-------:-:-::::-:-::-:::-',
        '--:::::::::::::::::::::::::::::::::::::::::::-:-:----:-:-::---:-',
        ':-:-----33333333333----------+----------------:-::::-:-:-::::-:-',
        '--:-::::;;;;;;;;;;;::::::::::::::::::::::-:::-:----:-:-:-3::3-:-',
        '-::K::::----------------------------------:Z;-:-::-:-:T--::::-:-',
        '--::::::::::::::::::::::::::1:1:1:1:1:1:1::-:-:-::-:-:::::3:3-:-',
        ':-:W:----------------------::::::::::::::::-:-:-::-:-------::-:`',
        '--:-:-:11111111:Z:;:::::::-:K-XXXXXXX3333333:1:-::-:::::::-:3-:`',
        '-::-:-::::::::::::*******:-::::::::::::::::-:-:W::-------:-::-:`',
        '--:-:-:CI`-------:*******:-:::EWWWWW--------:T::::::::::-:-:3-:`',
        ':-:-:-::::::::::-:::::::::---::::::::::::::::::3333333:--:-::-:`',
        '------------------+:Z-----------------------------------::----:L'
    ]),

    30: LiteralLevel([
        'K1VXXXXXXXXXXXXXXXX3333333333333K#333##Q...\\2-2-2-2-2-2-2-2-2-:R',
        '-1V  +++++++++++++3333333333333333333#######-2-2-2-2-2-2-2-2-2;R',
        '-1V  #########################------+##-2-2-2-2-2-2-2-2-2-2-2-:R',
        '-1V  F-----------------------I-------##2-2-2-2---2-2-2-2-2-2-2RR',
        '-1V--##################################-2-2-2--C--2-2-2-2-2-2ZRR',
        '-1V2-2-2-2VV++K++VV2-2-2-2-2-2-2-2-2-2-2-2-2-2---2-2-2-2-2-RRRRR',
        '-1V-2-2-2-VV++S++VV-2-2-2-2-2-----2-2-2-2-2-2-2-2-2-2RRRRRRRRRRR',
        '-1V2-2-2-2VVDVVVDVV2-2-2-2-2-2-K-2-2-2-2-2-2-2-2-RRRRRRRRRRRRRRR',
        '-1V-2-2-2-2-2-2-2-2-2-2-2-2-2-----2-2-2-2-2-2-RRRRRRRRRRRRRRRRRR',
        '-1V///////-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-RRRRR##333333333XXR',
        '--XXXXXX//2-VVVVV-2-2-2==================-2-RRRRRE##3333333333XR',
        'P X 33ZX//-2V+B+V2-2-2C==UDCDXDXDXDXDXDCD2-2RRRREAED3333B33333UR',
        '--XXXXXX//2-VVVVV-2-2-2==================-2-RRRRRE##3333333333XR',
        '-1V///////-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-2-RRRRR##333333333XXR',
        '-1V-2-2-2-2-2-2-2-2-2-2-2-2-2-----2-2-2-2-2-2-RRRRRRRRRRRRRRRRRR',
        '-1V2-2-2-2VVDVVVDVV2-2-2-2-2-2-K-2-2-2-2-2-2-2-2-RRRRRRRRRRRRRRR',
        '-1V-2-2-2-VV++S++VV-2-2-2-2-2-----2-2-2-2-2-2-2-2-2-2RRRRRRRRRRR',
        '-1V2-2-2-2VV++K++VV2-2-2-2-2-2-2-2-2-2-2-2-2-2---2-2-2-2-2-RRRRR',
        '-1V;##################2-2-2-2-2-2-2-2-2-2-2-2--C--2-2-2-2-2-2ZRR',
        '-1V1EEEEE1EEEEEE11EE###################2-2-2-2---2-2-2-2-2-2-2RR',
        '-1V1EEEE1E1EEEE1EE1E##C+++++++3KKD***##-2-2-2-2-2-2-2-2-2-2-2-:R',
        '-1VE1E11+EE11E1EEEE1##############***##2-2-2-2-2-2-2-2-2-2-2-2;R',
        'K1V+E1EEEEEEE1E+EEEE+*W*+C+*W*+K##S-----2-2-2-2-2-2-2-2-2-2-2-:R'
    ])
}
