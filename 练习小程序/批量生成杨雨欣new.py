#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
stringPart0=r'''NX 10.0.0.24
Macro File: C:\Users\admin8\Desktop\0625-4.macro
Macro Version 7.50
Macro List Language and Codeset: simpl_chinese 13
Created by admin8 on Fri Jun 25 21:51:13 2021
Part Name Display Style: $FILENAME
Selection Parameters 1 2 0.229167 1
Display Parameters 1.000000 16.208333 8.729167 -1.000000 -0.538560 1.000000 0.538560
*****************
RESET'''

stringPart1=r'''
MENU, 0, UG_MODELING_FF_THROUGH_POINTS UG_GATEWAY_MAIN_MENUBAR <RibbonTopBar->MenuBar->UG_INSERT->UG_MODELING_SURFACE> ## ! 
DIALOG_BEGIN "Through Points" 0 ! DA2
  BEG_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  BEG_ITEM  1 (1 OPTM 0) = 0  ! Neither
  BEG_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  BEG_ITEM  4 (1 INTE 0) = 3  ! Column Degree
  END_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  END_ITEM  1 (1 OPTM 0) = 0  ! Neither
  END_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  END_ITEM  4 (1 INTE 0) = 3  ! Column Degree
DIALOG_END 6, 1 ! Through Points: Points from File
FOCUS CHANGE IN 1
FOCUS CHANGE IN 1
FOCUS CHANGE OUT 1
FOCUS CHANGE IN 1
'''

ChangedP1_01='FILE_BOX -2,@@@E:\\CST\\Part1\\Data\\'
ChangedP1_02='\\down.dat@@@E:\\CST\\Part1\\Data\\'
ChangedP1_03='\\*.DAT@@@ 0 ! Point File\n'

stringPart2=r'''   SET_VALUE: 0 ! FSB item
FOCUS CHANGE IN 1
MESSAGE_BOX -2, Consecutive equal points
MESSAGE_TEXT  Some points rejected
DIALOG_BEGIN "Through Points" 0 ! DA2
  BEG_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  BEG_ITEM  1 (1 OPTM 0) = 0  ! Neither
  BEG_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  BEG_ITEM  4 (1 INTE 0) = 3  ! Column Degree
FOCUS CHANGE OUT 1
FOCUS CHANGE OUT 1
  END_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  END_ITEM  1 (1 OPTM 0) = 0  ! Neither
  END_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  END_ITEM  4 (1 INTE 0) = 3  ! Column Degree
DIALOG_END 6, 1 ! Through Points: Points from File
FOCUS CHANGE IN 1
FOCUS CHANGE IN 1
FOCUS CHANGE OUT 1
FOCUS CHANGE IN 1
'''

ChangedP2_01='FILE_BOX -2,@@@E:\\CST\\Part1\\Data\\'
ChangedP2_02='\\udersurface.dat@@@E:\\CST\Part1\Data\\'
ChangedP2_03='\\*.DAT@@@ 0 ! Point File\n'

stringPart3=r'''   SET_VALUE: 0 ! FSB item
DIALOG_BEGIN "Through Points" 0 ! DA2
  BEG_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  BEG_ITEM  1 (1 OPTM 0) = 0  ! Neither
  BEG_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  BEG_ITEM  4 (1 INTE 0) = 3  ! Column Degree
  END_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  END_ITEM  1 (1 OPTM 0) = 0  ! Neither
  END_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  END_ITEM  4 (1 INTE 0) = 3  ! Column Degree
DIALOG_END 6, 1 ! Through Points: Points from File
FOCUS CHANGE IN 1
FOCUS CHANGE IN 1
FOCUS CHANGE OUT 1
FOCUS CHANGE IN 1
'''

ChangedP3_01='FILE_BOX -2,@@@E:\\CST\\Part1\\Data\\'
ChangedP3_02='\\up.dat@@@E:\\CST\\Part1\\Data\\'
ChangedP3_03='\\*.DAT@@@ 0 ! Point File\n'

stringPart4=r'''   SET_VALUE: 0 ! FSB item
FOCUS CHANGE IN 1
MESSAGE_BOX -2, Consecutive equal points
MESSAGE_TEXT  Some points rejected
DIALOG_BEGIN "Through Points" 0 ! DA2
  BEG_ITEM  0 (1 OPTM 0) = 1  ! Multiple
  BEG_ITEM  1 (1 OPTM 0) = 0  ! Neither
  BEG_ITEM  3 (1 INTE 0) = 3  ! Row Degree
  BEG_ITEM  4 (1 INTE 0) = 3  ! Column Degree
FOCUS CHANGE IN 1
  MENU, 0, UG_VIEW_FIT UG_GATEWAY_MAIN_MENUBAR <RibbonTopBar->rbn_view.grb> ## ! 
DIALOG_END -3, 0 ! Through Points: CANCEL
FOCUS CHANGE IN 1
MENU, 0, UG_FILE_EXPORT_IGES UG_GATEWAY_MAIN_MENUBAR <RibbonFileBar->BackStageBar->LeftBackStageGroup->UG_FILE_EXPORT_MENU> ## ! 
ASK_ITEM 6488064 (1 BOOL 0) = 1  ! Model Data
ASK_ITEM 6684672 (1 BOOL 0) = 1  ! Drawings
ASK_ITEM 8257536 (1 BOOL 0) = 1  ! Curves
ASK_ITEM 8454144 (1 BOOL 0) = 1  ! Surfaces
ASK_ITEM 8650752 (1 BOOL 0) = 1  ! Solids
ASK_ITEM 8847360 (1 BOOL 0) = 1  ! Annotations
ASK_ITEM 9043968 (1 BOOL 0) = 1  ! Structures
ASK_ITEM 9240576 (1 BOOL 0) = 1  ! Coordinate Systems
ASK_ITEM 9240576 (1 BOOL 0) = 0  ! Coordinate Systems
ASK_ITEM 9437184 (1 BOOL 0) = 1  ! Product Data
ASK_ITEM 9437184 (1 BOOL 0) = 0  ! Product Data
ASK_ITEM 9633792 (1 BOOL 0) = 1  ! PMI
ASK_ITEM 9633792 (1 BOOL 0) = 0  ! PMI
ASK_ITEM 15204352 (1 OPTT 0) = 8 0 ! CSYS of Object
ASK_ITEM 15204352 (1 OPTT 0) = 8 1 ! CSYS of Object
ASK_ITEM 15204352 (1 OPTT 0) = 8 1 ! CSYS of Object
ASK_ITEM 15204352 (1 OPTT 0) = 8 0 ! CSYS of Object
ASK_ITEM 16711680 (1 BOOL 0) = 1  ! Japanese Automotive Compliant (JAMA)
ASK_ITEM 16711680 (1 BOOL 0) = 0  ! Japanese Automotive Compliant (JAMA)
ASK_ITEM 16908288 (1 BOOL 0) = 1  ! Flatten Assembly
ASK_ITEM 16908288 (1 BOOL 0) = 0  ! Flatten Assembly
ASK_ITEM 17104896 (1 BOOL 0) = 1  ! Map Tabulated Cylinder to B-surface
ASK_ITEM 18481152 (1 BOOL 0) = 1  ! System Defined Maximum 3D Model Space
ASK_ITEM 18874368 (1 BOOL 0) = 1  ! System Defined Identical Point Resolution
ASK_ITEM 20250624 (1 BOOL 0) = 1  ! Use Start Section File
ASK_ITEM 20250624 (1 BOOL 0) = 0  ! Use Start Section File
EVENT FOCUS_IN 0 0, 3211264, 0, 0, 0!  
ASK_ITEM 3211264 (1 STRN 0) = "E:\CST\Part1\Data\1\_model1.igs"  !  
DIALOG_BEGIN "Export to IGES Options" 0 ! DA2
BEG_ITEM 131072 (1 BTAB 0) = 1  !  
BEG_ITEM 589824 (1 RADI 0) = 0  ! Displayed Part
BEG_ITEM 1310720 (1 STRN 0) = ""  !  
BEG_ITEM 2031616 (1 STRN 0) = ""  !  
BEG_ITEM 3211264 (1 STRN 0) = "E:\CST\Part1\Data\1\_model1.igs"  !  
BEG_ITEM 4325376 (1 STRN 0) = "D:\Program Files\Siemens\NX 10.0\iges\igesexport.def"  !  
BEG_ITEM 5111808 (1 STRN 0) = ""  !  
BEG_ITEM 6488064 (1 BOOL 0) = 1  ! Model Data
BEG_ITEM 6684672 (1 BOOL 0) = 1  ! Drawings
BEG_ITEM 7340032 (1 OPTM 0) = 0  ! Entire Part
BEG_ITEM 7536640 (1 BOOL 0) = 0  ! Object
BEG_ITEM 8257536 (1 BOOL 0) = 1  ! Curves
BEG_ITEM 8454144 (1 BOOL 0) = 1  ! Surfaces
BEG_ITEM 8650752 (1 BOOL 0) = 1  ! Solids
BEG_ITEM 8847360 (1 BOOL 0) = 1  ! Annotations
BEG_ITEM 9043968 (1 BOOL 0) = 1  ! Structures
BEG_ITEM 9240576 (1 BOOL 0) = 0  ! Coordinate Systems
BEG_ITEM 9437184 (1 BOOL 0) = 0  ! Product Data
BEG_ITEM 9633792 (1 BOOL 0) = 0  ! PMI
BEG_ITEM 9961472 (1 OPTM 0) = 0  ! All Views
BEG_ITEM 10158081 (1 MULT 0) = 0  ! List (Items selected)
BEG_ITEM 11796480 (1 OPTM 0) = 0  ! All Drawings
BEG_ITEM 11993089 (1 MULT 0) = 0  ! List (Items selected)
BEG_ITEM 13828096 (1 STRN 0) = ""  ! Disable Layer
BEG_ITEM 14024704 (1 STRN 0) = ""  ! Enable Layer
BEG_ITEM 14942208 (1 OPTM 0) = 0  ! ##32Absolute
BEG_ITEM 15204352 (1 OPTT 0) = 8 0 ! CSYS of Object
BEG_ITEM 15794176 (1 OPTM 0) = 8  ! CSYS of Object
BEG_ITEM 15794178 (1 TOOL 0) = 5  ! CSYS of Object
BEG_ITEM 16711680 (1 BOOL 0) = 0  ! Japanese Automotive Compliant (JAMA)
BEG_ITEM 16908288 (1 BOOL 0) = 0  ! Flatten Assembly
BEG_ITEM 17104896 (1 BOOL 0) = 1  ! Map Tabulated Cylinder to B-surface
BEG_ITEM 17301504 (1 RADI 0) = 0  ! B-surfaces
BEG_ITEM 17498112 (1 RADI 0) = 0  ! Section Area
BEG_ITEM 18087936 (1 REAL 0) = 0.0508000000000000  ! SP-curve/B-surface Tolerance
BEG_ITEM 18284544 (1 REAL 0) = 2.0000000000000000  ! Maximum Line Thickness
BEG_ITEM 18481152 (1 BOOL 0) = 1  ! System Defined Maximum 3D Model Space
BEG_ITEM 18677760 (1 REAL 0) = 10000.0000000000000000  ! Maximum 3D Model Space
BEG_ITEM 18874368 (1 BOOL 0) = 1  ! System Defined Identical Point Resolution
BEG_ITEM 19070976 (1 REAL 0) = 0.0010000000000000  ! Identical Point Resolution
BEG_ITEM 19660800 (1 STRN 0) = ""  ! Author:
BEG_ITEM 19857408 (1 STRN 0) = ""  ! Company:
BEG_ITEM 20054016 (1 STRN 0) = ""  ! ID for Receiver:
BEG_ITEM 20250624 (1 BOOL 0) = 0  ! Use Start Section File
BEG_ITEM 20905984 (1 STRN 0) = ""  !  
BEG_ITEM 21823490 (1 BOOL 0) = 1  ! Preview
EVENT FOCUS_IN 0 0, 3014656, 0, 0, 0! Browse...
ASK_ITEM 3211264 (1 STRN 0) = "E:\CST\Part1\Data\1\_model1.igs"  !  
EVENT ACTIVATE 0 0, 3014656, 0, 0, 0! <DLC> Browse...
FOCUS CHANGE OUT 1
FOCUS CHANGE OUT 1
FOCUS CHANGE OUT 1
FOCUS CHANGE OUT 1
'''
ChangedP4_01='FILE_BOX -2,@@@E:\\CST\\Part1\\Data\\'
ChangedP4_02='@@@E:\\CST\\Part1\\Data\\'
ChangedP4_03='\\*.IGS@@@ 0 ! IGES File\n'

stringPart5=r'''ASK_ITEM 3211264 (1 STRN 0) = "E:\CST\Part1\Data\1\_model1.igs"  !
'''
ChangedP5_01='ASK_ITEM 3211264 (1 STRN 0) = "E:\\CST\\Part1\\Data\\'
ChangedP5_02='.igs"  !\n'




stringPart6=r'''OK 0 0 ! OK Callback  
FOCUS CHANGE IN 1
MESSAGE_BOX -4, The following part has been modified:
MESSAGE_TEXT      D:\Program Files\Siemens\NX 10.0\UGII\_model1.prt
MESSAGE_TEXT  
MESSAGE_TEXT  Do you want to save it first?
MESSAGE_TEXT  
MESSAGE_TEXT  Choose Yes to save the part and translate it.
MESSAGE_TEXT  Choose Continue to translate the part without saving it first.
MESSAGE_TEXT  Choose No to cancel the translation of this part.
FOCUS CHANGE IN 1
END_ITEM 131072 (1 BTAB 0) = 1  !  
END_ITEM 589824 (1 RADI 0) = 0  ! Displayed Part
END_ITEM 1310720 (1 STRN 0) = ""  !  
END_ITEM 2031616 (1 STRN 0) = ""  !  
'''
ChangedP6_01='END_ITEM 3211264 (1 STRN 0) = "E:\\CST\\Part1\\Data\\'
ChangedP6_02='.igs"  !\n'

stringPart7=r'''END_ITEM 4325376 (1 STRN 0) = "D:\Program Files\Siemens\NX 10.0\iges\igesexport.def"  !  
END_ITEM 5111808 (1 STRN 0) = ""  !  
END_ITEM 6488064 (1 BOOL 0) = 1  ! Model Data
END_ITEM 6684672 (1 BOOL 0) = 1  ! Drawings
END_ITEM 7340032 (1 OPTM 0) = 0  ! Entire Part
END_ITEM 7536640 (1 BOOL 0) = 0  ! Object
END_ITEM 8257536 (1 BOOL 0) = 1  ! Curves
END_ITEM 8454144 (1 BOOL 0) = 1  ! Surfaces
END_ITEM 8650752 (1 BOOL 0) = 1  ! Solids
END_ITEM 8847360 (1 BOOL 0) = 1  ! Annotations
END_ITEM 9043968 (1 BOOL 0) = 1  ! Structures
END_ITEM 9240576 (1 BOOL 0) = 0  ! Coordinate Systems
END_ITEM 9437184 (1 BOOL 0) = 0  ! Product Data
END_ITEM 9633792 (1 BOOL 0) = 0  ! PMI
END_ITEM 9961472 (1 OPTM 0) = 0  ! All Views
END_ITEM 10158081 (1 MULT 0) = 0  ! List (Items selected)
END_ITEM 11796480 (1 OPTM 0) = 0  ! All Drawings
END_ITEM 11993089 (1 MULT 0) = 0  ! List (Items selected)
END_ITEM 13828096 (1 STRN 0) = ""  ! Disable Layer
END_ITEM 14024704 (1 STRN 0) = ""  ! Enable Layer
END_ITEM 14942208 (1 OPTM 0) = 0  ! ##32Absolute
END_ITEM 15204352 (1 OPTT 0) = 8 0 ! CSYS of Object
END_ITEM 15794176 (1 OPTM 0) = 8  ! CSYS of Object
END_ITEM 15794178 (1 TOOL 0) = 5  ! CSYS of Object
END_ITEM 16711680 (1 BOOL 0) = 0  ! Japanese Automotive Compliant (JAMA)
END_ITEM 16908288 (1 BOOL 0) = 0  ! Flatten Assembly
END_ITEM 17104896 (1 BOOL 0) = 1  ! Map Tabulated Cylinder to B-surface
END_ITEM 17301504 (1 RADI 0) = 0  ! B-surfaces
END_ITEM 17498112 (1 RADI 0) = 0  ! Section Area
END_ITEM 18087936 (1 REAL 0) = 0.0508000000000000  ! SP-curve/B-surface Tolerance
END_ITEM 18284544 (1 REAL 0) = 2.0000000000000000  ! Maximum Line Thickness
END_ITEM 18481152 (1 BOOL 0) = 1  ! System Defined Maximum 3D Model Space
END_ITEM 18677760 (1 REAL 0) = 10000.0000000000000000  ! Maximum 3D Model Space
END_ITEM 18874368 (1 BOOL 0) = 1  ! System Defined Identical Point Resolution
END_ITEM 19070976 (1 REAL 0) = 0.0010000000000000  ! Identical Point Resolution
END_ITEM 19660800 (1 STRN 0) = ""  ! Author:
END_ITEM 19857408 (1 STRN 0) = ""  ! Company:
END_ITEM 20054016 (1 STRN 0) = ""  ! ID for Receiver:
END_ITEM 20250624 (1 BOOL 0) = 0  ! Use Start Section File
END_ITEM 20905984 (1 STRN 0) = ""  !  
END_ITEM 21823490 (1 BOOL 0) = 1  ! Preview
DIALOG_END -2, 0 ! Export to IGES Options: OK
MENU, 0, UG_SEL_SELECT_ALL UG_GATEWAY_MAIN_MENUBAR <Ctrl A> ## ! 
MENU, 0, UG_EDIT_DELETE UG_GATEWAY_MAIN_MENUBAR < Delete> ## ! '''

i=501
file=open('0625-3-100'+'.txt','w')
file.write(stringPart0)
while(i<=768):
    print('file name is 0625-3-100'+str(i)+'.macro')
    file.write(stringPart1)
    file.write(ChangedP1_01+str(i)+ChangedP1_02+str(i)+ChangedP1_03)
    
    file.write(stringPart2)
    file.write(ChangedP2_01+str(i)+ChangedP2_02+str(i)+ChangedP2_03)

    file.write(stringPart3)
    file.write(ChangedP3_01+str(i)+ChangedP3_02+str(i)+ChangedP3_03)

    file.write(stringPart4)
    file.write(ChangedP4_01+str(i)+'\\'+str(i)+ChangedP4_02+str(i)+ChangedP4_03)

    file.write(stringPart5)
    file.write(ChangedP5_01+str(i)+'\\'+str(i)+ChangedP5_02)

    file.write(stringPart6)
    file.write(ChangedP6_01+str(i)+'\\'+str(i)+ChangedP6_02)
    
    file.write(stringPart7)

    i=i+1

file.close()

#问题：txt文本的第95和101行出现了序号，是否需要进行修改？