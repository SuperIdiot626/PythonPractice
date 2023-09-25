# Pointwise V18.3 Journal file - Fri Jul  2 16:22:12 2021

package require PWI_Glyph 3.18.3

pw::Application setUndoMaximumLevels 5
pw::Application reset
pw::Application markUndoLevel {Journal Reset}

pw::Application clearModified

set _TMP(mode_1) [pw::Application begin DatabaseImport]
  $_TMP(mode_1) initialize -strict -type Automatic E:/CST/Part1/Data/277/277.igs
  $_TMP(mode_1) read
  $_TMP(mode_1) convert
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Import Database}

set _DB(1) [pw::DatabaseEntity getByName BSurf-219]
set _TMP(boundary_1) [$_DB(1) getBoundary 2]
set _DB(2) [pw::DatabaseEntity getByName BSurf-223]
set _TMP(boundary_2) [$_DB(2) getBoundary 1]
set _TMP(boundary_3) [$_DB(2) getBoundary 2]
set _TMP(PW_1) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_TMP(boundary_1) $_TMP(boundary_2) $_TMP(boundary_3)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Connectors On DB Entities}

unset _TMP(boundary_1)
unset _TMP(boundary_2)
unset _TMP(boundary_3)
set _DB(3) [pw::DatabaseEntity getByName BSurf-221]
set _CN(1) [pw::GridEntity getByName con-3]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(1) getParameter -arc [expr {0.01 * 50}]]
set _TMP(PW_1) [$_CN(1) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _CN(2) [pw::GridEntity getByName con-1]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(2) getParameter -arc [expr {0.01 * 50}]]
set _TMP(PW_1) [$_CN(2) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _CN(3) [pw::GridEntity getByName con-3-split-1]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(3) getParameter -arc [expr {0.01 * 50}]]
set _TMP(PW_1) [$_CN(3) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _CN(4) [pw::GridEntity getByName con-1-split-1]
set _CN(5) [pw::GridEntity getByName con-3-split-1-split-1]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(4) getParameter -arc [expr {0.01 * 50}]]
set _TMP(PW_1) [$_CN(4) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _CN(6) [pw::GridEntity getByName con-2]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(6) getParameter -arc [expr {0.01 * 10}]]
set _TMP(PW_1) [$_CN(6) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _TMP(PW_1) [pw::Collection create]
$_TMP(PW_1) set [list $_DB(3) $_DB(1) $_DB(2)]
$_TMP(PW_1) do setRenderAttribute FillMode Shaded
$_TMP(PW_1) delete
unset _TMP(PW_1)
pw::Application markUndoLevel {Modify Entity Display}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _CN(7) [pw::GridEntity getByName con-2-split-1]
  set _CN(8) [pw::GridEntity getByName con-3-split-2]
  set _CN(9) [pw::GridEntity getByName con-3-split-1-split-2]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
  set _TMP(PW_1) [pw::SegmentSurfaceSpline create]
  $_TMP(PW_1) addPoint [$_CN(7) getPosition -arc 0]
  $_TMP(PW_1) addPoint [$_CN(8) getPosition -arc 0]
  set _CN(10) [pw::Connector create]
  $_CN(10) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(10) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
$_CN(10) delete
pw::Application markUndoLevel {Delete Last Curve}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) addPoint [$_CN(7) getPosition -arc 0]
  $_TMP(PW_1) addPoint [$_CN(8) getPosition -arc 0]
  set _CN(11) [pw::Connector create]
  $_CN(11) addSegment $_TMP(PW_1)
  $_CN(11) calculateDimension
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create Connector}

set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(11) getParameter -arc [expr {0.01 * 10}]]
set _TMP(PW_1) [$_CN(11) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _CN(12) [pw::GridEntity getByName con-2-split-2]
  $_TMP(PW_1) addPoint [$_CN(7) getPosition -arc 1]
  $_TMP(PW_1) addPoint {0.592534572976612 -0.190137308229013 -0.068908999581335}
  set _CN(13) [pw::Connector create]
  $_CN(13) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(13) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(PW_1) [subst [list $_CN(13)]]
set _TMP(mode_1) [pw::Application begin Modify $_TMP(PW_1)]
  set _TMP(PW_2) [list $_DB(2)]
  pw::Entity project -type ClosestPoint $_TMP(PW_1) $_TMP(PW_2)
  unset _TMP(PW_2)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Project

unset _TMP(PW_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _CN(14) [pw::GridEntity getByName con-1-split-1]
  set _CN(15) [pw::GridEntity getByName con-1-split-3]
  $_TMP(PW_1) addPoint [$_CN(14) getPosition -arc 1]
  $_TMP(PW_1) addPoint [$_CN(13) getPosition -arc 1]
  set _CN(16) [pw::Connector create]
  $_CN(16) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(16) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
  set _TMP(PW_1) [pw::SegmentSurfaceSpline create]
  $_TMP(PW_1) addPoint [$_CN(13) getPosition -arc 1]
  $_TMP(PW_1) addPoint [$_CN(5) getPosition -arc 1]
  set _CN(17) [pw::Connector create]
  $_CN(17) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(17) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
pw::Display setShowDatabase 0
$_CN(13) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(14) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(16) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(7) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(9) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(5) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

set _CN(18) [pw::GridEntity getByName con-1-split-1-split-2]
$_CN(18) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

set _CN(19) [pw::GridEntity getByName con-1-split-1-split-1]
$_CN(19) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(15) setDimension 151
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(17) setDimension 151
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(12) setDimension 151
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(14) $_CN(13) $_CN(7) $_CN(16)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(13) $_CN(5) $_CN(17) $_CN(12)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(15) $_CN(9) $_CN(17) $_CN(16)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _DM(1) [pw::GridEntity getByName dom-1]
set _TMP(mode_1) [pw::Application begin EllipticSolver [list $_DM(1)]]
  set _TMP(ENTS) [pw::Collection create]
  $_TMP(ENTS) set [list $_DM(1)]
  $_TMP(ENTS) do setInitializeMethod Standard
  $_TMP(ENTS) delete
  unset _TMP(ENTS)
  $_TMP(mode_1) setActiveSubGrids $_DM(1) [list]
  $_TMP(mode_1) run -entities [list $_DM(1)] Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

set _TMP(mode_1) [pw::Application begin Modify [list $_CN(12) $_CN(15) $_CN(17)]]
  set _TMP(PW_1) [$_CN(12) getDistribution 1]
  $_TMP(PW_1) setBeginSpacing 0.01
  unset _TMP(PW_1)
  set _TMP(PW_1) [$_CN(15) getDistribution 1]
  $_TMP(PW_1) setBeginSpacing 0.01
  unset _TMP(PW_1)
  set _TMP(PW_1) [$_CN(17) getDistribution 1]
  $_TMP(PW_1) setBeginSpacing 0.01
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Change Spacings}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _DM(2) [pw::GridEntity getByName dom-2]
  set _CN(20) [pw::GridEntity getByName con-1-split-2]
  set _DM(3) [pw::GridEntity getByName dom-3]
  $_TMP(PW_1) addPoint [$_CN(20) getPosition -arc 0]
  $_TMP(PW_1) addPoint [$_CN(7) getPosition -arc 0]
  set _CN(21) [pw::Connector create]
  $_CN(21) addSegment $_TMP(PW_1)
  $_CN(21) calculateDimension
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create Connector}

set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(21) getParameter -arc [expr {0.01 * 90}]]
set _TMP(PW_1) [$_CN(21) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

pw::Display setShowDatabase 1
pw::Display setShowDomains 0
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _CN(22) [pw::GridEntity getByName con-4-split-1]
  set _CN(23) [pw::GridEntity getByName con-4-split-2]
  $_TMP(PW_1) addPoint [$_CN(22) getPosition -arc 1]
  $_TMP(PW_1) addPoint {0.500383532954824 -0.221222188265632 0.0408622532208911}
  set _CN(24) [pw::Connector create]
  $_CN(24) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(24) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(PW_1) [subst [list $_CN(24)]]
set _TMP(mode_1) [pw::Application begin Modify $_TMP(PW_1)]
  set _TMP(PW_2) [list $_DB(1)]
  pw::Entity project -type ClosestPoint $_TMP(PW_1) $_TMP(PW_2)
  unset _TMP(PW_2)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Project

unset _TMP(PW_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) addPoint [$_CN(7) getPosition -arc 1]
  $_TMP(PW_1) addPoint [$_CN(24) getPosition -arc 1]
  set _CN(25) [pw::Connector create]
  $_CN(25) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(25) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
$_CN(24) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(25) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(23) setDimension 51
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

pw::Display setShowDatabase 0
pw::Display setShowDomains 1
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
  set _TMP(PW_1) [pw::SegmentSurfaceSpline create]
  $_TMP(PW_1) addPoint [$_CN(19) getPosition -arc 1]
  $_TMP(PW_1) addPoint [$_CN(24) getPosition -arc 1]
  set _CN(26) [pw::Connector create]
  $_CN(26) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(26) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
$_CN(26) setDimension 151
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(22) setDimension 151
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(18) $_CN(22) $_CN(26) $_CN(24)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(19) $_CN(26) $_CN(25) $_CN(12)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainStructured createFromConnectors -reject _TMP(unusedCons) -solid [list $_CN(23) $_CN(25) $_CN(24) $_CN(7)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _DM(4) [pw::GridEntity getByName dom-6]
set _TMP(mode_1) [pw::Application begin EllipticSolver [list $_DM(4)]]
  set _TMP(ENTS) [pw::Collection create]
  $_TMP(ENTS) set [list $_DM(4)]
  $_TMP(ENTS) do setInitializeMethod Standard
  $_TMP(ENTS) delete
  unset _TMP(ENTS)
  $_TMP(mode_1) setActiveSubGrids $_DM(4) [list]
  $_TMP(mode_1) run -entities [list $_DM(4)] Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

set _TMP(mode_1) [pw::Application begin Modify [list $_CN(22)]]
  set _TMP(PW_1) [$_CN(22) getDistribution 1]
  $_TMP(PW_1) setEndSpacing 0.01
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Change Spacing}

set _TMP(mode_1) [pw::Application begin Modify [list $_CN(26)]]
  set _TMP(PW_1) [$_CN(26) getDistribution 1]
  $_TMP(PW_1) setEndSpacing 0.01
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Change Spacing}

set _TMP(mode_1) [pw::Application begin Modify [list $_CN(22)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Modify [list $_CN(26)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Modify [list $_CN(12)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Modify [list $_CN(17)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Modify [list $_CN(15)]]
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  pw::Display resetView +Y
  $_TMP(PW_1) addPoint [$_CN(8) getPosition -arc 0]
  $_TMP(PW_1) addPoint [list 5.0 -7.617604463883154e-16 3.7636949734838]
  set _CN(27) [pw::Connector create]
  $_CN(27) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(27) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _DM(5) [pw::GridEntity getByName dom-4]
  pw::Display resetView +Y
  set _DM(6) [pw::GridEntity getByName dom-5]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentConic create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
  set _TMP(PW_1) [pw::SegmentConic create]
  $_TMP(PW_1) addPoint {-1 0 0}
  $_TMP(PW_1) addPoint [$_CN(27) getPosition -arc 1]
  $_TMP(PW_1) setShoulderPoint {0.592603474524128 -7.61760446388315e-16 2.67743517907742}
  set _DB(4) [pw::Curve create]
  $_DB(4) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create Curve}

pw::Display setShowDatabase 1
set _TMP(mode_1) [pw::Application begin Create]
  set _DB(5) [pw::Surface create]
  $_DB(5) revolve -angle 360 $_DB(4) [pw::Application getXYZ [list 0 0 $_DB(4)]] {1 0 0}
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create Revolve}

set _TMP(PW_1) [pw::Connector createOnDatabase -parametricConnectors Aligned -merge 0 -reject _TMP(unused) [list $_DB(5)]]
unset _TMP(unused)
unset _TMP(PW_1)
pw::Application markUndoLevel {Connectors On DB Entities}

set _CN(28) [pw::GridEntity getByName con-8]
pw::Entity delete [list $_CN(28)]
pw::Application markUndoLevel Delete

set _TMP(PW_1) [pw::Collection create]
$_TMP(PW_1) set [list $_DB(5)]
$_TMP(PW_1) do setRenderAttribute FillMode Shaded
$_TMP(PW_1) delete
unset _TMP(PW_1)
pw::Application markUndoLevel {Modify Entity Display}

set _CN(29) [pw::GridEntity getByName con-10]
set _TMP(split_params) [list]
lappend _TMP(split_params) [$_CN(29) getParameter -arc [expr {0.01 * 50}]]
set _TMP(PW_1) [$_CN(29) split $_TMP(split_params)]
unset _TMP(PW_1)
unset _TMP(split_params)
pw::Application markUndoLevel Split

set _CN(30) [pw::GridEntity getByName con-10-split-2]
pw::Entity delete [list $_CN(30)]
pw::Application markUndoLevel Delete

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentConic create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
  set _TMP(PW_1) [pw::SegmentConic create]
  set _CN(31) [pw::GridEntity getByName con-9]
  set _CN(32) [pw::GridEntity getByName con-10-split-1]
  pw::Display resetView +Y
  $_TMP(PW_1) addPoint [$_CN(31) getPosition -arc 0]
  $_TMP(PW_1) addPoint [$_CN(32) getPosition -arc 1]
  $_TMP(PW_1) setShoulderPoint {0.620219051773602 3.00840746163924e-16 -2.72701465410368}
  set _CN(33) [pw::Connector create]
  $_CN(33) addSegment $_TMP(PW_1)
  $_CN(33) calculateDimension
  unset _TMP(PW_1)
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create Connector}

$_CN(31) setDimension 61
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(33) setDimension 61
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(32) setDimension 61
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

pw::Application setGridPreference Unstructured
set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(32) $_CN(31) $_CN(33)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

pw::Display setShowDatabase 0
set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  set _DM(7) [pw::GridEntity getByName dom-7]
  $_TMP(PW_1) addPoint [$_CN(32) getPosition -arc 1]
  $_TMP(PW_1) addPoint [$_CN(20) getPosition -arc 0]
  set _CN(34) [pw::Connector create]
  $_CN(34) addSegment $_TMP(PW_1)
  unset _TMP(PW_1)
  $_CN(34) calculateDimension
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel {Create 2 Point Connector}

set _TMP(mode_1) [pw::Application begin Create]
  set _TMP(PW_1) [pw::SegmentSpline create]
  $_TMP(PW_1) delete
  unset _TMP(PW_1)
$_TMP(mode_1) abort
unset _TMP(mode_1)
set _TMP(PW_1) [pw::Collection create]
$_TMP(PW_1) set [list $_CN(27) $_CN(34)]
$_TMP(PW_1) do setDimension 61
$_TMP(PW_1) delete
unset _TMP(PW_1)
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(27) setDimension 61
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

$_CN(34) setDimension 61
pw::CutPlane refresh
pw::Application markUndoLevel Dimension

set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(5) $_CN(19) $_CN(18) $_CN(9) $_CN(27) $_CN(34) $_CN(32)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _TMP(PW_1) [pw::DomainUnstructured createFromConnectors -reject _TMP(unusedCons)  [list $_CN(14) $_CN(15) $_CN(22) $_CN(23) $_CN(27) $_CN(34) $_CN(31) $_CN(33)]]
unset _TMP(unusedCons)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Domains}

set _DM(8) [pw::GridEntity getByName dom-9]
set _DM(9) [pw::GridEntity getByName dom-8]
set _TMP(PW_1) [pw::BlockUnstructured createFromDomains -reject _TMP(unusedDoms) -voids _TMP(voidBlocks) -baffles _TMP(baffleFaces) [concat [list] [list $_DM(1) $_DM(3) $_DM(2) $_DM(7) $_DM(8) $_DM(9) $_DM(6) $_DM(5) $_DM(4)]]]
unset _TMP(unusedDoms)
unset _TMP(PW_1)
pw::Application markUndoLevel {Assemble Blocks}

pw::Application setCAESolver CFD++ 3
pw::Application markUndoLevel {Select Solver}

set _BL(1) [pw::GridEntity getByName blk-1]
set _TMP(PW_1) [pw::BoundaryCondition getByName Unspecified]
set _TMP(PW_2) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_3) [pw::BoundaryCondition getByName bc-2]
unset _TMP(PW_2)
set _TMP(PW_4) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_5) [pw::BoundaryCondition getByName bc-3]
unset _TMP(PW_4)
set _TMP(PW_6) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_7) [pw::BoundaryCondition getByName bc-4]
unset _TMP(PW_6)
$_TMP(PW_3) setName in
pw::Application markUndoLevel {Name BC}

$_TMP(PW_5) setName out
pw::Application markUndoLevel {Name BC}

$_TMP(PW_7) setName wall
pw::Application markUndoLevel {Name BC}

$_TMP(PW_3) apply [list [list $_BL(1) $_DM(7)]]
pw::Application markUndoLevel {Set BC}

set _TMP(PW_8) [pw::BoundaryCondition create]
pw::Application markUndoLevel {Create BC}

set _TMP(PW_9) [pw::BoundaryCondition getByName bc-5]
unset _TMP(PW_8)
$_TMP(PW_9) setName sym
pw::Application markUndoLevel {Name BC}

$_TMP(PW_9) apply [list [list $_BL(1) $_DM(8)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_5) apply [list [list $_BL(1) $_DM(9)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(1)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(3)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(2)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(5)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(4)]]
pw::Application markUndoLevel {Set BC}

$_TMP(PW_7) apply [list [list $_BL(1) $_DM(6)]]
pw::Application markUndoLevel {Set BC}

unset _TMP(PW_1)
unset _TMP(PW_3)
unset _TMP(PW_5)
unset _TMP(PW_7)
unset _TMP(PW_9)
set _TMP(mode_1) [pw::Application begin UnstructuredSolver [list $_BL(1)]]
  set _TMP(PW_1) [pw::TRexCondition getByName Unspecified]
  set _TMP(PW_2) [pw::TRexCondition create]
  set _TMP(PW_3) [pw::TRexCondition getByName bc-2]
  unset _TMP(PW_2)
  $_TMP(PW_3) setName wall
  $_TMP(PW_3) setConditionType Wall
  $_TMP(PW_3) setValue 1.0000000000000001e-05
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(3) Same]]
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(2) Same]]
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(1) Same]]
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(5) Opposite]]
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(6) Opposite]]
  $_TMP(PW_3) apply [list [list $_BL(1) $_DM(4) Opposite]]
  $_BL(1) setUnstructuredSolverAttribute TRexFullLayers 20
  $_BL(1) setUnstructuredSolverAttribute TRexMaximumLayers 20
  $_BL(1) setUnstructuredSolverAttribute TRexGrowthRate 1.2
  $_TMP(mode_1) setStopWhenFullLayersNotMet true
  $_TMP(mode_1) setAllowIncomplete true
  $_TMP(mode_1) run Initialize
$_TMP(mode_1) end
unset _TMP(mode_1)
pw::Application markUndoLevel Solve

unset _TMP(PW_1)
unset _TMP(PW_3)
set _TMP(exam_1) [pw::Examine create BlockSkewEquiangle]
$_TMP(exam_1) addEntity [list $_BL(1)]
$_TMP(exam_1) examine
pw::CutPlane applyMetric BlockSkewEquiangle
$_TMP(exam_1) delete
unset _TMP(exam_1)
pw::CutPlane applyMetric {}
pw::Application save E:/CST/Part1/Data/277/277.pw
set _TMP(mode_1) [pw::Application begin CaeExport [pw::Entity sort [list $_BL(1)]]]
  $_TMP(mode_1) initialize -strict -type CAE E:/CST/Part1/Data/277
  $_TMP(mode_1) verify
  $_TMP(mode_1) write
$_TMP(mode_1) end
unset _TMP(mode_1)
