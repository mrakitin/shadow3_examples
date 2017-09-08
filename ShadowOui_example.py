#
# Python script to run shadow3. Created automatically with ShadowTools.make_python_script_from_list().
#
import Shadow
import numpy

# write (1) or not (0) SHADOW files start.xx end.xx star.xx
iwrite = 0

#
# initialize shadow3 source (oe0) and beam
#
beam = Shadow.Beam()
oe0 = Shadow.Source()
oe1 = Shadow.OE()
oe2 = Shadow.OE()
oe3 = Shadow.OE()
oe4 = Shadow.OE()
oe5 = Shadow.OE()
oe6 = Shadow.OE()
oe7 = Shadow.OE()
oe8 = Shadow.OE()
oe9 = Shadow.OE()
oe10 = Shadow.OE()
oe11 = Shadow.OE()
oe12 = Shadow.OE()
oe13 = Shadow.OE()
oe14 = Shadow.OE()
oe15 = Shadow.OE()
oe16 = Shadow.OE()
oe17 = Shadow.OE()
oe18 = Shadow.OE()
oe19 = Shadow.OE()
oe20 = Shadow.OE()
oe21 = Shadow.OE()
oe22 = Shadow.OE()

#
# Define variables. See meaning of variables in: 
#  https://raw.githubusercontent.com/srio/shadow3/master/docs/source.nml 
#  https://raw.githubusercontent.com/srio/shadow3/master/docs/oe.nml
#

oe0.FDISTR = 3
oe0.F_PHOT = 0
oe0.HDIV1 = 0.0
oe0.HDIV2 = 0.0
oe0.IDO_VX = 0
oe0.IDO_VZ = 0
oe0.IDO_X_S = 0
oe0.IDO_Y_S = 0
oe0.IDO_Z_S = 0
oe0.NPOINT = 1000000
oe0.PH1 = 8000.0
oe0.SIGDIX = 2.3e-05
oe0.SIGDIZ = 4.5e-06
oe0.SIGMAX = 0.00931
oe0.SIGMAZ = 0.00121
oe0.VDIV1 = 0.0
oe0.VDIV2 = 0.0

oe1.DUMMY = 1.0
oe1.FWRITE = 3
oe1.F_REFRAC = 2
oe1.F_SCREEN = 1
oe1.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
oe1.N_SCREEN = 1
oe1.RX_SLIT = numpy.array([0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
oe1.RZ_SLIT = numpy.array([0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
oe1.T_IMAGE = 0.0
oe1.T_INCIDENCE = 0.0
oe1.T_REFLECTION = 180.0
oe1.T_SOURCE = 2000.0

oe2.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe2.DUMMY = 1.0
oe2.FHIT_C = 1
oe2.FMIRR = 4
oe2.FSHAPE = 2
oe2.FWRITE = 3
oe2.F_EXT = 1
oe2.F_REFRAC = 1
oe2.PARAM = 0.1
oe2.RLEN2 = 0.075
oe2.RWIDX2 = 0.075
oe2.R_ATTENUATION_IMA = 1.8953
oe2.R_IND_IMA = 0.999994674
oe2.T_IMAGE = 0.0025
oe2.T_INCIDENCE = 0.0
oe2.T_REFLECTION = 180.0
oe2.T_SOURCE = 1499.9975

oe3.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe3.DUMMY = 1.0
oe3.FHIT_C = 1
oe3.FMIRR = 4
oe3.FSHAPE = 2
oe3.FWRITE = 3
oe3.F_CONVEX = 1
oe3.F_EXT = 1
oe3.F_REFRAC = 1
oe3.PARAM = 0.1
oe3.RLEN2 = 0.075
oe3.RWIDX2 = 0.075
oe3.R_ATTENUATION_OBJ = 1.8953
oe3.R_IND_OBJ = 0.999994674
oe3.T_IMAGE = -0.0025
oe3.T_INCIDENCE = 0.0
oe3.T_REFLECTION = 180.0
oe3.T_SOURCE = 0.0025

oe4.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe4.DUMMY = 1.0
oe4.FHIT_C = 1
oe4.FMIRR = 4
oe4.FSHAPE = 2
oe4.FWRITE = 3
oe4.F_EXT = 1
oe4.F_REFRAC = 1
oe4.PARAM = 0.1
oe4.RLEN2 = 0.075
oe4.RWIDX2 = 0.075
oe4.R_ATTENUATION_IMA = 1.8953
oe4.R_IND_IMA = 0.999994674
oe4.T_IMAGE = 0.0025
oe4.T_INCIDENCE = 0.0
oe4.T_REFLECTION = 180.0
oe4.T_SOURCE = -0.0025

oe5.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe5.DUMMY = 1.0
oe5.FHIT_C = 1
oe5.FMIRR = 4
oe5.FSHAPE = 2
oe5.FWRITE = 3
oe5.F_CONVEX = 1
oe5.F_EXT = 1
oe5.F_REFRAC = 1
oe5.PARAM = 0.1
oe5.RLEN2 = 0.075
oe5.RWIDX2 = 0.075
oe5.R_ATTENUATION_OBJ = 1.8953
oe5.R_IND_OBJ = 0.999994674
oe5.T_IMAGE = -0.0025
oe5.T_INCIDENCE = 0.0
oe5.T_REFLECTION = 180.0
oe5.T_SOURCE = 0.0025

oe6.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe6.DUMMY = 1.0
oe6.FHIT_C = 1
oe6.FMIRR = 4
oe6.FSHAPE = 2
oe6.FWRITE = 3
oe6.F_EXT = 1
oe6.F_REFRAC = 1
oe6.PARAM = 0.1
oe6.RLEN2 = 0.075
oe6.RWIDX2 = 0.075
oe6.R_ATTENUATION_IMA = 1.8953
oe6.R_IND_IMA = 0.999994674
oe6.T_IMAGE = 0.0025
oe6.T_INCIDENCE = 0.0
oe6.T_REFLECTION = 180.0
oe6.T_SOURCE = -0.0025

oe7.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe7.DUMMY = 1.0
oe7.FHIT_C = 1
oe7.FMIRR = 4
oe7.FSHAPE = 2
oe7.FWRITE = 3
oe7.F_CONVEX = 1
oe7.F_EXT = 1
oe7.F_REFRAC = 1
oe7.PARAM = 0.1
oe7.RLEN2 = 0.075
oe7.RWIDX2 = 0.075
oe7.R_ATTENUATION_OBJ = 1.8953
oe7.R_IND_OBJ = 0.999994674
oe7.T_IMAGE = -0.0025
oe7.T_INCIDENCE = 0.0
oe7.T_REFLECTION = 180.0
oe7.T_SOURCE = 0.0025

oe8.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe8.DUMMY = 1.0
oe8.FHIT_C = 1
oe8.FMIRR = 4
oe8.FSHAPE = 2
oe8.FWRITE = 3
oe8.F_EXT = 1
oe8.F_REFRAC = 1
oe8.PARAM = 0.1
oe8.RLEN2 = 0.075
oe8.RWIDX2 = 0.075
oe8.R_ATTENUATION_IMA = 1.8953
oe8.R_IND_IMA = 0.999994674
oe8.T_IMAGE = 0.0025
oe8.T_INCIDENCE = 0.0
oe8.T_REFLECTION = 180.0
oe8.T_SOURCE = -0.0025

oe9.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe9.DUMMY = 1.0
oe9.FHIT_C = 1
oe9.FMIRR = 4
oe9.FSHAPE = 2
oe9.FWRITE = 3
oe9.F_CONVEX = 1
oe9.F_EXT = 1
oe9.F_REFRAC = 1
oe9.PARAM = 0.1
oe9.RLEN2 = 0.075
oe9.RWIDX2 = 0.075
oe9.R_ATTENUATION_OBJ = 1.8953
oe9.R_IND_OBJ = 0.999994674
oe9.T_IMAGE = -0.0025
oe9.T_INCIDENCE = 0.0
oe9.T_REFLECTION = 180.0
oe9.T_SOURCE = 0.0025

oe10.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe10.DUMMY = 1.0
oe10.FHIT_C = 1
oe10.FMIRR = 4
oe10.FSHAPE = 2
oe10.FWRITE = 3
oe10.F_EXT = 1
oe10.F_REFRAC = 1
oe10.PARAM = 0.1
oe10.RLEN2 = 0.075
oe10.RWIDX2 = 0.075
oe10.R_ATTENUATION_IMA = 1.8953
oe10.R_IND_IMA = 0.999994674
oe10.T_IMAGE = 0.0025
oe10.T_INCIDENCE = 0.0
oe10.T_REFLECTION = 180.0
oe10.T_SOURCE = -0.0025

oe11.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe11.DUMMY = 1.0
oe11.FHIT_C = 1
oe11.FMIRR = 4
oe11.FSHAPE = 2
oe11.FWRITE = 3
oe11.F_CONVEX = 1
oe11.F_EXT = 1
oe11.F_REFRAC = 1
oe11.PARAM = 0.1
oe11.RLEN2 = 0.075
oe11.RWIDX2 = 0.075
oe11.R_ATTENUATION_OBJ = 1.8953
oe11.R_IND_OBJ = 0.999994674
oe11.T_IMAGE = -0.0025
oe11.T_INCIDENCE = 0.0
oe11.T_REFLECTION = 180.0
oe11.T_SOURCE = 0.0025

oe12.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe12.DUMMY = 1.0
oe12.FHIT_C = 1
oe12.FMIRR = 4
oe12.FSHAPE = 2
oe12.FWRITE = 3
oe12.F_EXT = 1
oe12.F_REFRAC = 1
oe12.PARAM = 0.1
oe12.RLEN2 = 0.075
oe12.RWIDX2 = 0.075
oe12.R_ATTENUATION_IMA = 1.8953
oe12.R_IND_IMA = 0.999994674
oe12.T_IMAGE = 0.0025
oe12.T_INCIDENCE = 0.0
oe12.T_REFLECTION = 180.0
oe12.T_SOURCE = -0.0025

oe13.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe13.DUMMY = 1.0
oe13.FHIT_C = 1
oe13.FMIRR = 4
oe13.FSHAPE = 2
oe13.FWRITE = 3
oe13.F_CONVEX = 1
oe13.F_EXT = 1
oe13.F_REFRAC = 1
oe13.PARAM = 0.1
oe13.RLEN2 = 0.075
oe13.RWIDX2 = 0.075
oe13.R_ATTENUATION_OBJ = 1.8953
oe13.R_IND_OBJ = 0.999994674
oe13.T_IMAGE = -0.0025
oe13.T_INCIDENCE = 0.0
oe13.T_REFLECTION = 180.0
oe13.T_SOURCE = 0.0025

oe14.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe14.DUMMY = 1.0
oe14.FHIT_C = 1
oe14.FMIRR = 4
oe14.FSHAPE = 2
oe14.FWRITE = 3
oe14.F_EXT = 1
oe14.F_REFRAC = 1
oe14.PARAM = 0.1
oe14.RLEN2 = 0.075
oe14.RWIDX2 = 0.075
oe14.R_ATTENUATION_IMA = 1.8953
oe14.R_IND_IMA = 0.999994674
oe14.T_IMAGE = 0.0025
oe14.T_INCIDENCE = 0.0
oe14.T_REFLECTION = 180.0
oe14.T_SOURCE = -0.0025

oe15.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe15.DUMMY = 1.0
oe15.FHIT_C = 1
oe15.FMIRR = 4
oe15.FSHAPE = 2
oe15.FWRITE = 3
oe15.F_CONVEX = 1
oe15.F_EXT = 1
oe15.F_REFRAC = 1
oe15.PARAM = 0.1
oe15.RLEN2 = 0.075
oe15.RWIDX2 = 0.075
oe15.R_ATTENUATION_OBJ = 1.8953
oe15.R_IND_OBJ = 0.999994674
oe15.T_IMAGE = -0.0025
oe15.T_INCIDENCE = 0.0
oe15.T_REFLECTION = 180.0
oe15.T_SOURCE = 0.0025

oe16.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe16.DUMMY = 1.0
oe16.FHIT_C = 1
oe16.FMIRR = 4
oe16.FSHAPE = 2
oe16.FWRITE = 3
oe16.F_EXT = 1
oe16.F_REFRAC = 1
oe16.PARAM = 0.1
oe16.RLEN2 = 0.075
oe16.RWIDX2 = 0.075
oe16.R_ATTENUATION_IMA = 1.8953
oe16.R_IND_IMA = 0.999994674
oe16.T_IMAGE = 0.0025
oe16.T_INCIDENCE = 0.0
oe16.T_REFLECTION = 180.0
oe16.T_SOURCE = -0.0025

oe17.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe17.DUMMY = 1.0
oe17.FHIT_C = 1
oe17.FMIRR = 4
oe17.FSHAPE = 2
oe17.FWRITE = 3
oe17.F_CONVEX = 1
oe17.F_EXT = 1
oe17.F_REFRAC = 1
oe17.PARAM = 0.1
oe17.RLEN2 = 0.075
oe17.RWIDX2 = 0.075
oe17.R_ATTENUATION_OBJ = 1.8953
oe17.R_IND_OBJ = 0.999994674
oe17.T_IMAGE = -0.0025
oe17.T_INCIDENCE = 0.0
oe17.T_REFLECTION = 180.0
oe17.T_SOURCE = 0.0025

oe18.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.2, 0.0])
oe18.DUMMY = 1.0
oe18.FHIT_C = 1
oe18.FMIRR = 4
oe18.FSHAPE = 2
oe18.FWRITE = 3
oe18.F_EXT = 1
oe18.F_REFRAC = 1
oe18.PARAM = 0.1
oe18.RLEN2 = 0.075
oe18.RWIDX2 = 0.075
oe18.R_ATTENUATION_IMA = 1.8953
oe18.R_IND_IMA = 0.999994674
oe18.T_IMAGE = 0.0025
oe18.T_INCIDENCE = 0.0
oe18.T_REFLECTION = 180.0
oe18.T_SOURCE = -0.0025

oe19.CCC = numpy.array([1.0, 1.0, 0.0, 0.0, -0.0, -0.0, 0.0, 0.0, 0.2, 0.0])
oe19.DUMMY = 1.0
oe19.FHIT_C = 1
oe19.FMIRR = 4
oe19.FSHAPE = 2
oe19.FWRITE = 3
oe19.F_CONVEX = 1
oe19.F_EXT = 1
oe19.F_REFRAC = 1
oe19.PARAM = 0.1
oe19.RLEN2 = 0.075
oe19.RWIDX2 = 0.075
oe19.R_ATTENUATION_OBJ = 1.8953
oe19.R_IND_OBJ = 0.999994674
oe19.T_IMAGE = 1499.9975
oe19.T_INCIDENCE = 0.0
oe19.T_REFLECTION = 180.0
oe19.T_SOURCE = 0.0025

oe20.DUMMY = 1.0
oe20.FWRITE = 3
oe20.F_REFRAC = 2
oe20.F_SCREEN = 1
oe20.I_SLIT = numpy.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
oe20.N_SCREEN = 1
oe20.RX_SLIT = numpy.array([0.0015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
oe20.RZ_SLIT = numpy.array([0.001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
oe20.T_IMAGE = 0.0
oe20.T_INCIDENCE = 0.0
oe20.T_REFLECTION = 180.0
oe20.T_SOURCE = 0.0

oe21.DUMMY = 1.0
oe21.FCYL = 1
oe21.FHIT_C = 1
oe21.FMIRR = 2
oe21.FWRITE = 3
oe21.F_DEFAULT = 0
oe21.RLEN1 = 25.0
oe21.RLEN2 = 25.0
oe21.RWIDX1 = 0.5
oe21.RWIDX2 = 0.5
oe21.SIMAG = 85.0
oe21.SSOUR = 3915.0
oe21.THETA = 89.79373519375291
oe21.T_IMAGE = 25.0
oe21.T_INCIDENCE = 89.79373519375291
oe21.T_REFLECTION = 89.79373519375291
oe21.T_SOURCE = 3915.0

oe22.ALPHA = 90.0
oe22.DUMMY = 1.0
oe22.FCYL = 1
oe22.FHIT_C = 1
oe22.FMIRR = 2
oe22.FWRITE = 3
oe22.F_DEFAULT = 0
oe22.RLEN1 = 25.0
oe22.RLEN2 = 25.0
oe22.RWIDX1 = 0.5
oe22.RWIDX2 = 0.5
oe22.SIMAG = 35.0
oe22.SSOUR = 3965.0
oe22.THETA = 89.79373519375291
oe22.T_IMAGE = 35.0
oe22.T_INCIDENCE = 89.79373519375291
oe22.T_REFLECTION = 89.79373519375291
oe22.T_SOURCE = 25.0



#Run SHADOW to create the source

if iwrite:
    oe0.write("start.00")

beam.genSource(oe0)

if iwrite:
    oe0.write("end.00")
    beam.write("begin.dat")


#
#run optical element 1
#
print("    Running optical element: %d"%(1))
if iwrite:
    oe1.write("start.01")
beam.traceOE(oe1,1)
if iwrite:
    oe1.write("end.01")
    beam.write("star.01")


#
#run optical element 2
#
print("    Running optical element: %d"%(2))
if iwrite:
    oe2.write("start.02")
beam.traceOE(oe2,2)
if iwrite:
    oe2.write("end.02")
    beam.write("star.02")


#
#run optical element 3
#
print("    Running optical element: %d"%(3))
if iwrite:
    oe3.write("start.03")
beam.traceOE(oe3,3)
if iwrite:
    oe3.write("end.03")
    beam.write("star.03")


#
#run optical element 4
#
print("    Running optical element: %d"%(4))
if iwrite:
    oe4.write("start.04")
beam.traceOE(oe4,4)
if iwrite:
    oe4.write("end.04")
    beam.write("star.04")


#
#run optical element 5
#
print("    Running optical element: %d"%(5))
if iwrite:
    oe5.write("start.05")
beam.traceOE(oe5,5)
if iwrite:
    oe5.write("end.05")
    beam.write("star.05")


#
#run optical element 6
#
print("    Running optical element: %d"%(6))
if iwrite:
    oe6.write("start.06")
beam.traceOE(oe6,6)
if iwrite:
    oe6.write("end.06")
    beam.write("star.06")


#
#run optical element 7
#
print("    Running optical element: %d"%(7))
if iwrite:
    oe7.write("start.07")
beam.traceOE(oe7,7)
if iwrite:
    oe7.write("end.07")
    beam.write("star.07")


#
#run optical element 8
#
print("    Running optical element: %d"%(8))
if iwrite:
    oe8.write("start.08")
beam.traceOE(oe8,8)
if iwrite:
    oe8.write("end.08")
    beam.write("star.08")


#
#run optical element 9
#
print("    Running optical element: %d"%(9))
if iwrite:
    oe9.write("start.09")
beam.traceOE(oe9,9)
if iwrite:
    oe9.write("end.09")
    beam.write("star.09")


#
#run optical element 10
#
print("    Running optical element: %d"%(10))
if iwrite:
    oe10.write("start.10")
beam.traceOE(oe10,10)
if iwrite:
    oe10.write("end.10")
    beam.write("star.10")


#
#run optical element 11
#
print("    Running optical element: %d"%(11))
if iwrite:
    oe11.write("start.11")
beam.traceOE(oe11,11)
if iwrite:
    oe11.write("end.11")
    beam.write("star.11")


#
#run optical element 12
#
print("    Running optical element: %d"%(12))
if iwrite:
    oe12.write("start.12")
beam.traceOE(oe12,12)
if iwrite:
    oe12.write("end.12")
    beam.write("star.12")


#
#run optical element 13
#
print("    Running optical element: %d"%(13))
if iwrite:
    oe13.write("start.13")
beam.traceOE(oe13,13)
if iwrite:
    oe13.write("end.13")
    beam.write("star.13")


#
#run optical element 14
#
print("    Running optical element: %d"%(14))
if iwrite:
    oe14.write("start.14")
beam.traceOE(oe14,14)
if iwrite:
    oe14.write("end.14")
    beam.write("star.14")


#
#run optical element 15
#
print("    Running optical element: %d"%(15))
if iwrite:
    oe15.write("start.15")
beam.traceOE(oe15,15)
if iwrite:
    oe15.write("end.15")
    beam.write("star.15")


#
#run optical element 16
#
print("    Running optical element: %d"%(16))
if iwrite:
    oe16.write("start.16")
beam.traceOE(oe16,16)
if iwrite:
    oe16.write("end.16")
    beam.write("star.16")


#
#run optical element 17
#
print("    Running optical element: %d"%(17))
if iwrite:
    oe17.write("start.17")
beam.traceOE(oe17,17)
if iwrite:
    oe17.write("end.17")
    beam.write("star.17")


#
#run optical element 18
#
print("    Running optical element: %d"%(18))
if iwrite:
    oe18.write("start.18")
beam.traceOE(oe18,18)
if iwrite:
    oe18.write("end.18")
    beam.write("star.18")


#
#run optical element 19
#
print("    Running optical element: %d"%(19))
if iwrite:
    oe19.write("start.19")
beam.traceOE(oe19,19)
if iwrite:
    oe19.write("end.19")
    beam.write("star.19")


#
#run optical element 20
#
print("    Running optical element: %d"%(20))
if iwrite:
    oe20.write("start.20")
beam.traceOE(oe20,20)
if iwrite:
    oe20.write("end.20")
    beam.write("star.20")


#
#run optical element 21
#
print("    Running optical element: %d"%(21))
if iwrite:
    oe21.write("start.21")
beam.traceOE(oe21,21)
if iwrite:
    oe21.write("end.21")
    beam.write("star.21")


#
#run optical element 22
#
print("    Running optical element: %d"%(22))
if iwrite:
    oe22.write("start.22")
beam.traceOE(oe22,22)
if iwrite:
    oe22.write("end.22")
    beam.write("star.22")


Shadow.ShadowTools.plotxy(beam,1,3,nbins=101,nolost=1,title="Real space")
# Shadow.ShadowTools.plotxy(beam,1,4,nbins=101,nolost=1,title="Phase space X")
# Shadow.ShadowTools.plotxy(beam,3,6,nbins=101,nolost=1,title="Phase space Z")
    