
# -*- python -*-
import math
import numpy
import Shadow
from Shadow.ShadowPreprocessorsXraylib import prerefl, pre_mlayer, bragg
from srxraylib.sources import srfunc

source = Shadow.Source()
beam = Shadow.Beam()

source.NPOINT = 100000
source.ISTAR1 = 567656


source.FSOUR = 3
source.WXSOU = 0.100000001
source.WZSOU = 0.200000003
source.SIGMAX = 0.00931
source.SIGMAZ = 0.00121
source.FDISTR = 3
source.SIGDIX = 2.3e-05
source.SIGDIZ = 4.5e-06
source.CONE_MAX = 0.0
source.CONE_MIN = 0.0
source.FSOURCE_DEPTH = 1
source.WYSOU = 0.2
source.SIGMAY = 0.001
source.F_COLOR = 1
source.F_POLAR = 1
source.F_COHER = 0
source.POL_ANGLE = 0.0
source.POL_DEG = 1.0
source.HDIV1 = 0.0005
source.HDIV2 = 0.0005
source.VDIV1 = 1.0
source.VDIV2 = 1.0
source.F_PHOT = 0
source.PH1 = 8000.0
source.F_BOUND_SOUR = 0
beam.genSource(source)



oe = Shadow.OE()
oe.DUMMY = 1.0
oe.set_empty().set_screens()
oe.I_SLIT[0] = 1
oe.K_SLIT[0] = 0
oe.RX_SLIT[0] = 0.1
oe.RZ_SLIT[0] = 0.1
oe.CX_SLIT[0] = 0.0
oe.CZ_SLIT[0] = 0.0
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 2000.0
beam.traceOE(oe, 1)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 1499.9975
beam.traceOE(oe, 2)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 3)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 4)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 5)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 6)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 7)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 8)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 9)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 10)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 11)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 12)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 13)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 14)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 15)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 16)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = -0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 17)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe.DUMMY = 1.0
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_IMA = 1.8953
oe.R_IND_IMA = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 0.0025
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = -0.0025
beam.traceOE(oe, 18)

oe = Shadow.OE()
oe.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0])
oe.DUMMY = 1.0
oe.F_CONVEX = 1
oe.F_EXT = 1
oe.F_REFRAC = 1
oe.FHIT_C = 1
oe.FMIRR = 4
oe.FSHAPE = 2
oe.FWRITE = 3
oe.PARAM = 0.1
oe.R_ATTENUATION_OBJ = 1.8953
oe.R_IND_OBJ = 0.999994674
oe.RLEN2 = 0.075
oe.RWIDX2 = 0.075
oe.T_IMAGE = 1499.9975
oe.T_INCIDENCE = 0.0
oe.T_REFLECTION = 180.0
oe.T_SOURCE = 0.0025
beam.traceOE(oe, 19)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.set_empty()
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 1500.0
beam.traceOE(oe, 20)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.set_empty().set_screens()
oe.I_SLIT[0] = 1
oe.K_SLIT[0] = 0
oe.RX_SLIT[0] = 0.0015
oe.RZ_SLIT[0] = 0.001
oe.CX_SLIT[0] = 0.0
oe.CZ_SLIT[0] = 0.0
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 0.0
beam.traceOE(oe, 21)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.set_empty()
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 3890.0
beam.traceOE(oe, 22)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.FMIRR = 2
oe.ALPHA = 0
oe.FHIT_C = 1
oe.F_EXT = 0
oe.F_DEFAULT = 0
oe.SSOUR = 3915.0
oe.SIMAG = 85.0
oe.THETA = 89.794
oe.F_CONVEX = 0
oe.FCYL = 1
oe.CIL_ANG = 0.0
oe.FSHAPE = 1
oe.RWIDX1 = 0.5
oe.RWIDX2 = 0.5
oe.RLEN1 = 25.0
oe.RLEN2 = 25.0
oe.T_INCIDENCE = 89.794
oe.T_REFLECTION = 89.794
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 25.0
beam.traceOE(oe, 23)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.FMIRR = 2
oe.ALPHA = 90
oe.FHIT_C = 1
oe.F_EXT = 0
oe.F_DEFAULT = 0
oe.SSOUR = 3965.0
oe.SIMAG = 45.0
oe.THETA = 89.794
oe.F_CONVEX = 0
oe.FCYL = 1
oe.CIL_ANG = 0.0
oe.FSHAPE = 1
oe.RWIDX1 = 0.5
oe.RWIDX2 = 0.5
oe.RLEN1 = 25.0
oe.RLEN2 = 25.0
oe.T_INCIDENCE = 89.794
oe.T_REFLECTION = 89.794
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 50.0
beam.traceOE(oe, 24)

oe = Shadow.OE()
oe.DUMMY = 1.0
oe.set_empty()
oe.FWRITE = 3
oe.T_IMAGE = 0.0
oe.T_SOURCE = 35.0
beam.traceOE(oe, 25)
beam.write('shadow-output.dat')


import Shadow.ShadowTools
Shadow.ShadowTools.plotxy(beam, 1, 3, nbins=100, nolost=1)
    