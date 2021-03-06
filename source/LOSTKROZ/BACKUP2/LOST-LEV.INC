{//-------------------------------------------------------------------------}
{/*                                                                         }
{Copyright (C) 1987, 2009 - Apogee Software, Ltd.                           }
{                                                                           }
{This file is part of Kroz. Kroz is free software; you can redistribute it  }
{and/or modify it under the terms of the GNU General Public License         }
{as published by the Free Software Foundation; either version 2             }
{of the License, or (at your option) any later version.                     }
{                                                                           }
{This program is distributed in the hope that it will be useful,            }
{but WITHOUT ANY WARRANTY; without even the implied warranty of             }
{MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                       }
{                                                                           }
{See the GNU General Public License for more details.                       }
{                                                                           }
{You should have received a copy of the GNU General Public License          }
{along with this program; if not, write to the Free Software                }
{Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.}
{                                                                           }
{Original Source: 1987-1990 Scott Miller                                    }
{Prepared for public release: 03/19/09 - Joe Siegler, Apogee Software, Ltd. }
{*/                                                                         }
{//-------------------------------------------------------------------------}
{*** THE LOST ADVENTURES OF KROZ level layouts.  By Scott Miller 11/12/89 ***}

procedure Level48;
 begin
  FP[1]:= '##################RRRRRRRRRRR#the#swamp#RRRRRRR-\\�\\\\/\\\\\\\C';
  FP[2]:= 'LL�D�D�D--VVVV--44----------------------------RR-\\\\\\\\\\\\\\\';
  FP[3]:= 'LL�D�D�D--VVVV--44--RRRRRRRRRRRRRRRRRRRRRRRR--RRR-/\\\\\\\\\U\\\';
  FP[4]:= '##################RRRR-------------------------RRR-\\\\/\\\\\\\\';
  FP[5]:= 'RRRRRRRRRRRRRRRRRRRRRR--RRRRRRRRRRRRRRRRRRRRK))RRRR--\\\\\\\\\\\';
  FP[6]:= 'R-----RRR-------R----)))RR)))))))3)3)3)3)3)3)3)3)3RRR--\\\\\\\\\';
  FP[7]:= 'R-RRR�RR-RRRRRRR-RRR-RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--/\\\/\�';
  FP[8]:= 'R-RR-RR-RRR\\\RRR-RRR--------------------------�-------RR--\\\\\';
  FP[9]:= 'R-RRRR-RR\\\K\\RRR-RR-RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--\\\';
  FP[10]:='R-RRR-RRRR\\\\\\RRR-RR------------Z-8�-999999999999�--RRRRRRR--\';
  FP[11]:='R-RR-RRRR\\\\\\�\RR-RRR-RRRRRRRRRRRRR8-111111111111RRR-----RRRR-';
  FP[12]:='R---RRRRRR-\\\RRRR-RRRRRFRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR-RRRR';
  FP[13]:='RRRR-RRRRR-RRRRRR-RRRS(((((+((((((((((((((((((K++(3RRRRRRRRR-RRR';
  FP[14]:='RRRRR-RRRR��RRRR-RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR*R.R*RRR-RR';
  FP[15]:='RRRRRRTRRR1R-RR-RRR@@@@@@@RRRRRRRRRRRRRRRRRR-----------�-�RRR�RR';
  FP[16]:='###RRRRRR11RR--RRRR@@RRRRFRR-66----H----------RRRRRRR*R.R*RRRRRR';
  FP[17]:='77###RRR111RR--RR*F@@@22@WRR-RR-RRORRRRRRRRRRRRRRRRRRRRRRRRRRR  ';
  FP[18]:='7777###RR11RR--RR*F@@@22@WRR-RR-RRORR                          P';
  FP[19]:='77777###RR1RR--RR*F@@@22@WRR-RR-RRORR  RRRRRRRRR-RRRRRRRRRRRRR  ';
  FP[20]:='77!777###RRRR--RR*F@@@22@WRR-RR-RR>RRFSRRRRRRRRR�RRRRRRRRRRRRRRR';
  FP[21]:='7777777##RRRR--RR*F@@@22@WRR-RR-RRRRR����������3333333333C������';
  FP[22]:='77777777##RRR--RRRRFFRRRRRRR-RR-RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR--';
  FP[23]:='U7777777##RRR----------------RR---------------------------------';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level48 }

procedure Level52;
 begin 
  FP[1]:= '�  ]  �]�   ]��] �]]�  ���]��� ] � �    �]��         �]���] �---';
  FP[2]:= ' �� �] � ��] �� � ]� �� ]���] � � � ]��� ]� ��]���]�� �]�� � -P-';
  FP[3]:= '  ���]� ��] �� �] � ��]�� ��] ���]���]�� � ]��    �] ���] ���---';
  FP[4]:= '�� �]���]� ��]� �� ]���]�� �]�   ��]���  ] �� �]��  �]���] ���]�';
  FP[5]:= '�]�  ��]��� ]� ��]��  �]�� �]���] ���] ��� ]��   �]���]���]  ���';
  FP[6]:= '���]� ��]��� ]� ��  ]�  ��] ���] ���  ]��� ]���]� ��]   ���]� ��';
  FP[7]:= '���] ���  ]��  �] ���]�� �]� �� ]�� �]���]� ��]�� �] ��� ]���] �';
  FP[8]:= '�]� ��  ]� ��]�� �]�  ��] ���  ]�� ��]���]��  �]��  �]  ���]��� ';
  FP[9]:= '�� ]� ��]��     �]� �� ]�� �]���] ��     �]��� ]���]� ��]�  �� ]';
  FP[10]:='� �] ��� ]���]���] ���] ��� ]��� ]� ��]�� ��]�� ��]� ��]� �� ]� ';
  FP[11]:=' �� ]�� � � ] � ��] ���] ����]�� �]� ��]�� �]���]� ��]�� �] � �';
  FP[12]:=']  ��� ]�� � ] �   ��]���   ]���]   ���]���    ]���]     ���] ��';
  FP[13]:='#####444############follow#the#bread#crumbs#####################';
  FP[14]:='����#555#&����������������������������������������@MMMMMMMMK##LL';
  FP[15]:='����66666�����������������������������������������@MMMMMMMMM##��';
  FP[16]:='��������������������������������������������������@MMMMMMMMM##``';
  FP[17]:='��������������������������������������������������@MMMMMMMMM##��';
  FP[18]:='�������������������������!������������������������@MMMMMMMMM##``';
  FP[19]:='��������������������������������������������������@MMMMMMMMM##��';
  FP[20]:='��������������������������������������������������@MMMMMMMMM##--';
  FP[21]:='��������������������������������������������������@MMMMMMMMM##--';
  FP[22]:='00������������������������������������������������@MMMMMMMMM##--';
  FP[23]:='K0������������������������������������������������@MMMMMMMMM66--';
  Fast:=#234;{or #1}
  Convert_Format;
  MakeFloor(#250,6,7,0,0); HideCreate:=true; HideMBlock:=true;
 end; { Level52 }

procedure Level53;
 begin
  FP[1]:= 'U----------; 55555------------------------�--##-U-##            ';
  FP[2]:= 'XXXXXXXXX�-; ##�############################-##---## ##������##�';
  FP[3]:= '-----------; #2�2#K--B-----------------------##---## ##������##-';
  FP[4]:= '-----------; ##�##-############################---## ##W����W##-';
  FP[5]:= '-----------; #2�2#      M   M   M   M   M    ##---## ## W��W ##-';
  FP[6]:= '-----------; ##�############################-##---## ##  WW  ##-';
  FP[7]:= 'XX�XXXX----; #2�2#�------------------K-------##---## ##2 22 2##-';
  FP[8]:= '------;----; ##�##�####################-----:##---## ##########-';
  FP[9]:= '------;----; #2�2#�-----------------------:::##---## C--�7;-;---';
  FP[10]:='------;----; ##�##�---------------------::-::##---## ##########-';
  FP[11]:='[-----;----; #2�2#--------------------:::::-:##-�-## -1--1--�##-';
  FP[12]:='------;----; ##�##XXXXXXXXXXXX�-----::::::::-##---## ##########-';
  FP[13]:='------;----; #2�|#-------------XXX::::::::::"##---## -------C##-';
  FP[14]:='------;----; ##�##--------------�##############---##4##########-';
  FP[15]:='------;----; #2�2#---------------#####-�----C##---##--------K##-';
  FP[16]:='------;----; ##�##`::::::::::::::##�##XOXXXXX##---##4##########-';
  FP[17]:='------;----; #2�2#--`---�---`LL# �-----------66���##--------<##-';
  FP[18]:='------;--�-; ##�################ ::�::;;;;;;;##888##4##########-';
  FP[19]:='------#1111#                     ##H##3333333##VVV##--------�##-';
  FP[20]:='------######XXXXXXXXXXXXXXXXXXXXX###################4##########-';
  FP[21]:='----------------------------------------------------------------';
  FP[22]:='XX�XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
  FP[23]:='                                P                               ';
  Fast:=#234;{or #1}
  Convert_Format;
  GravOn:=true;GravRate:=0;Sideways:=true;
 end; { Level53 }

procedure Level54;
 begin
  FP[1]:= '  P  ##-U--------##-------##��------------------##--DDDD-�-KKKKK';
  FP[2]:= 'II#II##----------##�#####-##--------------777---##�5555555555555';
  FP[3]:= 'M   M###########-##�-----�###########X##�##�######-##LLLLLLLLLLL';
  FP[4]:= 'M   M##---;---------------##K---------##-##7-<[|##-#############';
  FP[5]:= 'M   M###-#########################---###-######X##-----�----�-C"';
  FP[6]:= 'M   M##----------------�----------7�7-44--------##-#############';
  FP[7]:= 'M   M##-######################################�-##-�������������';
  FP[8]:= 'M   M##---------------------------------D--K##--##-]]]]]]]]]]?]]';
  FP[9]:= 'M   M######################################-##--##-abcdefghijklm';
  FP[10]:='M   M##K�`�:�-�-�-�:�-�:�:�-�:�-�-�-�:�:�##-##--##-#############';
  FP[11]:='M   M##-�`�-�:�-�:�:�:�-�-�:�-�:�-�:�:�-�##-##--##-##---------�!';
  FP[12]:='M   M##-�`�:�:�-�:�-�:�:�-�:�:�-�-�:�:�:�##-##--##-##�##########';
  FP[13]:='M   M##-�`�:�:�-�:�-�:�-�-�:�-�:�-�:�:�:�##-##--##-##-----------';
  FP[14]:='M   M##-�`�:�-�-�:�:�-�:�-�:�:�:�-�:�-�:�##-##--##-########�####';
  FP[15]:='M   M##-�`�:�-�-�:�-�:�:�7�:�:�:�-�:�:�-�##-##--##-##-----------';
  FP[16]:='M   M##-�`�-�:�-�:�:�:�:���:�-�:�-�:�-�:�##-##-.##-####�########';
  FP[17]:='M   M##-�-�-�:�-�:�:�-�-�-�:�:�-�-�:�-�:�##-##--##-##-----------';
  FP[18]:='M   M##:�:�:�:�:�:�:�:�:�:�:�:�:�-�:�:�:����##--##-############�';   
  FP[19]:='M   M##---                       ;          ##--##�88----------�';
  FP[20]:='M   M##-##VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV##--##0############�';
  FP[21]:='M   M##D######################################--##~------------�';
  FP[22]:='M K M##K-�1��1��1�11�1��11�11�1�11��1��1��11�-�-44�------------�';
  FP[23]:='M U M##K--�11�11�1��1�11��1��1�1��11�11�11��1�--44--------------';
  Fast:=#234;{or #1}
  Convert_Format;
  GravOn:=true;GravRate:=0;Sideways:=true;
 end; { Level54 }

procedure Level55;
 begin
  FP[1]:= '� P                          �#diary�#day#five�#################';
  FP[2]:= '#######################XXXX#####################################';
  FP[3]:= 'VVVYVVVVVVVVVVVVVVVVVVV----VVV#you�ve#traveled#deeper#into#kroz#';
  FP[4]:= 'VVVVVVVVVVVVVVVVVVYYVV-�--VVVV##################################';
  FP[5]:= 'VVVVVVVYYVVVVVVVVVVYVV----VVYV#than#ever#before�##where#will####';
  FP[6]:= 'YVVVVVVVYVVVVYVVVVVVV----VVVVV##################################';
  FP[7]:= 'VVVVVVVVVVVVVVVVVVVV--�-VVVVVV#the#many#chambers#lead#to�##and##';
  FP[8]:= 'VVVYVVVVVVYVVVVVVVV----VVYYVVV##################################';
  FP[9]:= 'VVVYVVVVVVVVVVVVVVV-�--VVVYVVV#what#do#they#protect#below�######';
  FP[10]:='VVVVVVVVVVVVYVVVVVVV----VVVVVV##################################';
  FP[11]:='VVVVVVVYVVVVYYVVVVVV----VVVVYV#you#have#a#good#feeling#these####';
  FP[12]:='VVVVVVVVVVVVVVVVVVV--�-VVVVVVV##################################';
  FP[13]:='VVYYYVVVVVVVVVVVVV----VVVVVVVV#questions#might#finally#be#######';
  FP[14]:='VVVVVVVVYVVVYVVVV----VVVYYYVVV##################################';
  FP[15]:='VVVVVVVVYVVVVVVV--�-VVVVVVVVVV#answered#during#this#expedition�#';
  FP[16]:='VVVVVVVVYVVVVVVV----VVVYYVVVVV##################################';
  FP[17]:='YYVVVYVVVVVVVVV----VVVVYVVVVVV#but#can#you#survive#to#learn#the#';
  FP[18]:='VYVVVVVVVVVVVV--�-VVVVVVVVVVYV##################################';
  FP[19]:='VVVVVVVVYVVVV----VVVYVVVVVVVVV#answers�##a#deep#lava#pit#lies###';
  FP[20]:='VVYVVVVVVVVV----VVVYYVVVVVVVVV##################################';
  FP[21]:='VVYYVVVVVVV-�--VVVVVVVVVVYYYVV#before#you#forbidding#your#######';
  FP[22]:='VVVVVVVYVV----VVYYVVVVVVVVVVVV##################################';
  FP[23]:='VVVVVVVVVLLLLVVVVYVVVVVYVVVVVV#progress���it#doesn�t#work����###';
  Fast:=#234;{or #1}
  Convert_Format;
  GravOn:=true;GravRate:=1;Sideways:=true; HideStairs:=true;
 end; { Level55 }

procedure Level56;
 begin
  FP[1]:= 'YVV P VVVYVVVVVYVVVVVVYVVYVVVVVXXVVVVVVVVV#U#VVVVVV�---------!VV';
  FP[2]:= 'VVV---VVVVVYVVVVVVVYVVVVYVVVYVVXXVVVVVVVVVV-VVVVVVVO#########RVV';
  FP[3]:= 'VYV---VVYVVVVVYVVVVVVYVVVVYVVVVXXVVVVVVVVV---VVVVVVOVVVVVVVVVRVV';
  FP[4]:= 'VVVV---VVVYVVVVVYVYVVVVVYVVVVYVXXVVVVVVVVV---VVVVVVOVVVVVVVVVRVV';
  FP[5]:= 'VVYV---VYVVVVYVVVVVVVYVVVVVYVVVXXVVVVVVVVV--VVVVVVVOVVVVVVVVVRVV';
  FP[6]:= 'VVVVV---VVVVVVVYVVVVVVVYVVVVVYVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[7]:= 'VVYVVV---VVYVYVVVVYVVVYVVVVYVVVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[8]:= 'VYVVYVV---VVVVVYVVVVYVVVVYVVVYVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[9]:= 'VVYVVVV---VVYVVVVYVVVVYVVVVYVVVXXVVVVVVVVVVVHHVVVVVOVVVVVVVVVRVV';
  FP[10]:='VYVVYVVV---VVVYVVVVYVVVVYVVVYVVXXVVVVVVVVVVV--VVVVVOVVVVVVVVVRVV';
  FP[11]:='VVVYVVYVV---VYVVYVVVVYVVVVYVVVVXXVVVVVVVVVVV--VVVVVOVVVVVVVVVRVV';
  FP[12]:='VYVVYVVVV---VVVVVVVYVVVYVVVVVYVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[13]:='VVVVVVVYVV---VVYVVYVVVVVVVYVYVVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[14]:='VVYVYVVVV---VVVVYVVVVYVVYVVVVVVXXVVVVVVVVVV--VVVVVVOVVVVVVVVVRVV';
  FP[15]:='YVVVVVVYVV---VVYVVYVVVVVVVVYVVVXXVVVVVVVVV--VVVVVVVOVVVVVVVVVRVV';
  FP[16]:='VVYVVYVVVVV---VVVYVVVVVYVVVVVYVXXVVVVVVVVV�-VVVVVVVOVVVVVVVVVRVV';
  FP[17]:='VYVVVVVVYVV---VVYVVVVYVVVVVYVVVXXVVVVVVVVV--VVVVVVVOVVVVVVVVVRVV';
  FP[18]:='VVVVYVYVVVYV---VVVVYVVVVYVVVYVVXXVVVVVVVVV--VVVVVVVOVVVVVVVVVRVV';
  FP[19]:='VYVVVVVYVVVVV---VVYVVVYVVVYVVVVXXVVVVVVVV--VVVVVVVVOVVVVVVVVVRVV';
  FP[20]:='VVVYVVVVVVYVVV---VVVYVVVYVVVVYVXXVVVVVVVV--VVVVVVVVOVVVVVVVVVRVV';
  FP[21]:='YVVVVVVVYVVVYVV---VVVVYVVVYVVVVXXVVVVVVVV--VVVVVVVVOVVVVVVVVVRVV';
  FP[22]:='VVVYVYVVVVYVVVV---VVYVVVYVVVVYVXXVVVVVVVVV--VVVVVVVOVVVVVVVVVRVV';
  FP[23]:='VYVVVVYVVVVVYVV#U#VVVVYVVVYVYVVXXVVVVVVVVV----------VVVVVVVVVLVV';
  Fast:=#234;{or #1}
  Convert_Format;
  GravOn:=true;GravRate:=1;Sideways:=true;HideStairs:=true;
 end; { Level56 }
(*
procedure Level;
 begin
  FP[1]:= '                                                                ';
  FP[2]:= '                                                                ';
  FP[3]:= '                                                                ';
  FP[4]:= '                                                                ';
  FP[5]:= '                                                                ';
  FP[6]:= '                                                                ';
  FP[7]:= '                                                                ';
  FP[8]:= '                                                                ';
  FP[9]:= '                                                                ';
  FP[10]:='                                                                ';
  FP[11]:='                                                                ';
  FP[12]:='                                                                ';
  FP[13]:='                                                                ';
  FP[14]:='                                                                ';
  FP[15]:='                                                                ';
  FP[16]:='                                                                ';
  FP[17]:='                                                                ';
  FP[18]:='                                                                ';
  FP[19]:='                                                                ';
  FP[20]:='                                                                ';
  FP[21]:='                                                                ';
  FP[22]:='                                                                ';
  FP[23]:='                                                                ';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level }

procedure Level;
 begin
  FP[1]:= '                                                                ';
  FP[2]:= '                                                                ';
  FP[3]:= '                                                                ';
  FP[4]:= '                                                                ';
  FP[5]:= '                                                                ';
  FP[6]:= '                                                                ';
  FP[7]:= '                                                                ';
  FP[8]:= '                                                                ';
  FP[9]:= '                                                                ';
  FP[10]:='                                                                ';
  FP[11]:='                                                                ';
  FP[12]:='                                                                ';
  FP[13]:='                                                                ';
  FP[14]:='                                                                ';
  FP[15]:='                                                                ';
  FP[16]:='                                                                ';
  FP[17]:='                                                                ';
  FP[18]:='                                                                ';
  FP[19]:='                                                                ';
  FP[20]:='                                                                ';
  FP[21]:='                                                                ';
  FP[22]:='                                                                ';
  FP[23]:='                                                                ';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level }

procedure Level;
 begin
  FP[1]:= '                                                                ';
  FP[2]:= '                                                                ';
  FP[3]:= '                                                                ';
  FP[4]:= '                                                                ';
  FP[5]:= '                                                                ';
  FP[6]:= '                                                                ';
  FP[7]:= '                                                                ';
  FP[8]:= '                                                                ';
  FP[9]:= '                                                                ';
  FP[10]:='                                                                ';
  FP[11]:='                                                                ';
  FP[12]:='                                                                ';
  FP[13]:='                                                                ';
  FP[14]:='                                                                ';
  FP[15]:='                                                                ';
  FP[16]:='                                                                ';
  FP[17]:='                                                                ';
  FP[18]:='                                                                ';
  FP[19]:='                                                                ';
  FP[20]:='                                                                ';
  FP[21]:='                                                                ';
  FP[22]:='                                                                ';
  FP[23]:='                                                                ';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level }

procedure Level;
 begin
  FP[1]:= '                                                                ';
  FP[2]:= '                                                                ';
  FP[3]:= '                                                                ';
  FP[4]:= '                                                                ';
  FP[5]:= '                                                                ';
  FP[6]:= '                                                                ';
  FP[7]:= '                                                                ';
  FP[8]:= '                                                                ';
  FP[9]:= '                                                                ';
  FP[10]:='                                                                ';
  FP[11]:='                                                                ';
  FP[12]:='                                                                ';
  FP[13]:='                                                                ';
  FP[14]:='                                                                ';
  FP[15]:='                                                                ';
  FP[16]:='                                                                ';
  FP[17]:='                                                                ';
  FP[18]:='                                                                ';
  FP[19]:='                                                                ';
  FP[20]:='                                                                ';
  FP[21]:='                                                                ';
  FP[22]:='                                                                ';
  FP[23]:='                                                                ';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level }
*)
procedure Level75;
 begin
  FP[1]:= '                                                                ';
  FP[2]:= '                                                                ';
  FP[3]:= '                                                                ';
  FP[4]:= '                                                                ';
  FP[5]:= '                                                                ';
  FP[6]:= '                                                                ';
  FP[7]:= '                                                                ';
  FP[8]:= '                                                                ';
  FP[9]:= '                                                                ';
  FP[10]:='                                                                ';
  FP[11]:='                                                                ';
  FP[12]:='                                                                ';
  FP[13]:='                                                                ';
  FP[14]:='                                                                ';
  FP[15]:='                                                                ';
  FP[16]:='                                                                ';
  FP[17]:='                                                                ';
  FP[18]:='                                                                ';
  FP[19]:='                                                                ';
  FP[20]:='                                                                ';
  FP[21]:='                                                                ';
  FP[22]:='                                                                ';
  FP[23]:='                                                                ';
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level75 }


(*
procedure Level#;
 begin
  FP[1]:= 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
  FP[2]:= 
  FP[3]:= 
  FP[4]:= 
  FP[5]:= 
  FP[6]:= 
  FP[7]:= 
  FP[8]:= 
  FP[9]:= 
  FP[10]:=
  FP[11]:=
  FP[12]:=
  FP[13]:=
  FP[14]:=
  FP[15]:=
  FP[16]:=
  FP[17]:=
  FP[18]:=
  FP[19]:=
  FP[20]:=
  FP[21]:=
  FP[22]:=
  FP[23]:=
  Fast:=#234;{or #1}
  Convert_Format;
 end; { Level# }
*)