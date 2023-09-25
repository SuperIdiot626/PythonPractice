# Pointwise V18.0R2 Journal file - Sun Jun 27 14:32:31 2021

package require PWI_Glyph 2.18.0

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}

pw::Application clearModified

set _TMP(mode_1) [pw::Application begin DatabaseImport]
  $_TMP(mode_1) initialize -type Automatic {E:/CST/Part1/Data/622/622.igs}
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Database}

set _DB(1) [pw::DatabaseEntity getByName "BSurf-219"]
set _TMP(boundary_1) [$_DB(1) getBoundary 3]
set _TMP(PW_1) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_TMP(boundary_1)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Connectors On DB Entities}

unset _TMP(boundary_1)
set _TMP(boundary_2) [$_DB(1) getBoundary 1]
set _TMP(PW_2) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_TMP(boundary_2)]]
unset _TMP(unused)
unset _TMP(PW_2)
pw::Application markUndoLevel {Connectors On DB Entities}

unset _TMP(boundary_2)
set _DB(2) [pw::DatabaseEntity getByName "BSurf-223"]
set _TMP(boundary_3) [$_DB(2) getBoundary 2]
set _TMP(PW_3) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_TMP(boundary_3)]]
unset _TMP(unused)
unset _TMP(PW_3)
pw::Application markUndoLevel {Connectors On DB Entities}

unset _TMP(boundary_3)
set _TMP(boundary_4) [$_DB(1) getBoundary 2]
set _TMP(PW_4) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_TMP(boundary_4)]]
unset _TMP(unused)
unset _TMP(PW_4)
pw::Application markUndoLevel {Connectors On DB Entities}

unset _TMP(boundary_4)
set _CN(1) [pw::GridEntity getByName "con-1"]
set _TMP(PW_5) [pw::Collection create]
$_TMP(PW_5) set [list $_CN(1)]
$_TMP(PW_5) do setDimension 251
$_TMP(PW_5) delete
unset _TMP(PW_5)
pw::Application markUndoLevel {Dimension}

set _CN(2) [pw::GridEntity getByName "con-2"]
set _TMP(PW_6) [pw::Collection create]
$_TMP(PW_6) set [list $_CN(2)]
$_TMP(PW_6) do setDimension 251
$_TMP(PW_6) delete
unset _TMP(PW_6)
pw::Application markUndoLevel {Dimension}

set _CN(3) [pw::GridEntity getByName "con-3"]
set _TMP(PW_7) [pw::Collection create]
$_TMP(PW_7) set [list $_CN(3)]
$_TMP(PW_7) do setDimension 161
$_TMP(PW_7) delete
unset _TMP(PW_7)
pw::Application markUndoLevel {Dimension}

set _CN(4) [pw::GridEntity getByName "con-4"]
set _TMP(PW_8) [pw::Collection create]
$_TMP(PW_8) set [list $_CN(4)]
$_TMP(PW_8) do setDimension 161
$_TMP(PW_8) delete
unset _TMP(PW_8)
pw::Application markUndoLevel {Dimension}

pw::Application setGridPreference Unstructured
set _TMP(PW_9) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(1) $_CN(3) $_CN(2)]]
unset _TMP(unusedCons)
unset _TMP(PW_9)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_10) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(1) $_CN(4) $_CN(2)]]
unset _TMP(unusedCons)
unset _TMP(PW_10)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_11) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(4) $_CN(3)]]
unset _TMP(unusedCons)
unset _TMP(PW_11)
pw::Application markUndoLevel {Assemble Domains}

set _DM(1) [pw::GridEntity getByName "dom-1"]
set _TMP(PW_12) [pw::Collection create]
$_TMP(PW_12) set [list $_DM(1)]
$_TMP(PW_12) do setRenderAttribute FillMode Shaded
$_TMP(PW_12) delete
unset _TMP(PW_12)
pw::Application markUndoLevel {Modify Entity Display}

set _TMP(mode_2) [pw::Application begin Create]
  set _TMP(PW_13) [pw::SegmentSpline create]
  $_TMP(PW_13) delete
  unset _TMP(PW_13)
  set _TMP(PW_14) [pw::SegmentConic create]
  pw::Display resetView +Y
  $_TMP(PW_14) addPoint {-1 0 0}
  $_TMP(PW_14) addPoint {5.79688953401208 0 3.20994326201264}
  $_TMP(PW_14) setShoulderPoint {0.7869839650993 0 2.3237836191357}
  set _TMP(curve_1) [pw::Curve create]
  $_TMP(curve_1) addSegment $_TMP(PW_14)
  unset _TMP(PW_14)
$_TMP(mode_2) end
unset _TMP(mode_2)
pw::Application markUndoLevel {Create Curve}

unset _TMP(curve_1)
set _DB(3) [pw::DatabaseEntity getByName "curve-1"]
set _TMP(mode_3) [pw::Application begin Create]
  set _TMP(surface_1) [pw::Surface create]
  $_TMP(surface_1) revolve -angle 360 $_DB(3) [pw::Application getXYZ [list 0 0 $_DB(3)]] {1 0 0}
  unset _TMP(surface_1)
$_TMP(mode_3) end
unset _TMP(mode_3)
pw::Application markUndoLevel {Create Revolve}

set _DB(4) [pw::DatabaseEntity getByName "surface-1"]
set _TMP(PW_15) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -type Unstructured -reject _TMP(unused) [list $_DB(4)]]
unset _TMP(unused)
unset _TMP(PW_15)
pw::Application markUndoLevel {Connectors On DB Entities}

set _CN(5) [pw::GridEntity getByName "con-7"]
set _TMP(PW_16) [pw::Collection create]
$_TMP(PW_16) set [list $_CN(5)]
$_TMP(PW_16) do setDimension 151
$_TMP(PW_16) delete
unset _TMP(PW_16)
pw::Application markUndoLevel {Dimension}

set _CN(6) [pw::GridEntity getByName "con-5"]
set _TMP(PW_17) [pw::Collection create]
$_TMP(PW_17) set [list $_CN(6)]
$_TMP(PW_17) do setDimension 151
$_TMP(PW_17) delete
unset _TMP(PW_17)
pw::Application markUndoLevel {Dimension}

set _CN(7) [pw::GridEntity getByName "con-6"]
set _TMP(PW_18) [pw::Collection create]
$_TMP(PW_18) set [list $_CN(7)]
$_TMP(PW_18) do setDimension 151
$_TMP(PW_18) delete
unset _TMP(PW_18)
pw::Application markUndoLevel {Dimension}

set _CN(8) [pw::GridEntity getByName "con-8"]
set _TMP(PW_19) [pw::Collection create]
$_TMP(PW_19) set [list $_CN(8)]
$_TMP(PW_19) do setDimension 151
$_TMP(PW_19) delete
unset _TMP(PW_19)
pw::Application markUndoLevel {Dimension}

set _TMP(PW_20) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(8) $_CN(7)]]
unset _TMP(unusedCons)
unset _TMP(PW_20)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_21) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(6) $_CN(8) $_CN(5)]]
unset _TMP(unusedCons)
unset _TMP(PW_21)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_22) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(6) $_CN(7) $_CN(5)]]
unset _TMP(unusedCons)
unset _TMP(PW_22)
pw::Application markUndoLevel {Assemble Domains}

set _DM(2) [pw::GridEntity getByName "dom-5"]
set _DM(3) [pw::GridEntity getByName "dom-2"]
set _DM(4) [pw::GridEntity getByName "dom-3"]
set _DM(5) [pw::GridEntity getByName "dom-6"]
set _DM(6) [pw::GridEntity getByName "dom-4"]
set _TMP(PW_23) [pw::BlockUnstructured createFromDomains -reject _TMP(unusedDoms) -voids _TMP(voidBlocks) -baffles _TMP(baffleFaces) [concat [list] [list $_DM(2) $_DM(3) $_DM(4) $_DM(5) $_DM(1) $_DM(6)]]]
unset _TMP(unusedDoms)
unset _TMP(PW_23)
pw::Application markUndoLevel {Assemble Blocks}

pw::Application setCAESolver {CFD++} 3
pw::Application markUndoLevel {Select Solver}

set _BL(1) [pw::GridEntity getByName "blk-1"]
set _TMP(PW_24) [pw::BoundaryCondition getByName "Unspecified"]
set _TMP(PW_25) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_26) [pw::BoundaryCondition getByName "bc-2"]
unset _TMP(PW_25)
set _TMP(PW_27) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_28) [pw::BoundaryCondition getByName "bc-3"]
unset _TMP(PW_27)
set _TMP(PW_29) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_30) [pw::BoundaryCondition getByName "bc-4"]
unset _TMP(PW_29)
$_TMP(PW_26) setName "IN"
pw::Application markUndoLevel {Name BC}

$_TMP(PW_28) setName "OUT"
pw::Application markUndoLevel {Name BC}

$_TMP(PW_30) setName "WALL"
pw::Application markUndoLevel {Name BC}

$_TMP(PW_26) apply [list [list $_BL(1) $_DM(5)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_26) apply [list [list $_BL(1) $_DM(2)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_28) apply [list [list $_BL(1) $_DM(6)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_30) apply [list [list $_BL(1) $_DM(1)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_30) apply [list [list $_BL(1) $_DM(3)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_30) apply [list [list $_BL(1) $_DM(4)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_24)
unset _TMP(PW_26)
unset _TMP(PW_28)
unset _TMP(PW_30)
set _TMP(mode_4) [pw::Application begin UnstructuredSolver [list $_BL(1)]]
  set _TMP(PW_31) [pw::TRexCondition getByName {Unspecified}]
  set _TMP(PW_32) [pw::TRexCondition create]
  set _TMP(PW_33) [pw::TRexCondition getByName {bc-2}]
  unset _TMP(PW_32)
  $_TMP(PW_33) setName {WALL}
  $_TMP(PW_33) setConditionType {Wall}
  $_TMP(PW_33) setSpacing 1.0000000000000001e-05
  $_TMP(PW_33) apply [list [list $_BL(1) $_DM(1) Opposite]]
  $_TMP(PW_33) apply [list [list $_BL(1) $_DM(3) Same]]
  set _TMP(ENTS) [pw::Collection create]
$_TMP(ENTS) set [list $_BL(1)]
  $_BL(1) setUnstructuredSolverAttribute TRexMaximumLayers 20
  $_TMP(ENTS) delete
  unset _TMP(ENTS)
  $_TMP(mode_4) run Initialize
$_TMP(mode_4) end
unset _TMP(mode_4)
pw::Application markUndoLevel {Solve}


unset _TMP(PW_31)
unset _TMP(PW_33)
pw::Application save {E:/CST/Part1/Data/622/622.pw}
set _TMP(exam_1) [pw::Examine create BlockMaximumAngle]
$_TMP(exam_1) addEntity [list $_BL(1)]
$_TMP(exam_1) examine
$_TMP(exam_1) delete
unset _TMP(exam_1)
set _TMP(mode_5) [pw::Application begin CaeExport [pw::Entity sort [list $_BL(1)]]]
  $_TMP(mode_5) initialize -type CAE {E:/CST/Part1/Data/622}
  if {![$_TMP(mode_5) verify]} {
    error "Data verification failed."
  }
  $_TMP(mode_5) write
$_TMP(mode_5) end
unset _TMP(mode_5)
