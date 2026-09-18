import mmap
import ctypes
import time
from ctypes import c_int32, c_float, c_wchar
class SPageFilePhysics(ctypes.Structure):
  _pack_ = 4
  _fields_ = [
    ('packetId',c_int32),
    ('gas', c_float),
    ('brake', c_float),
    ('fuel', c_float),
    ('gear', c_int32),
    ('rpm', c_int32),
    ('steerAngle', c_float),
    ('speedKmh', c_float),
    ('velocity', c_float * 3),
    ('accG', c_float * 3),
    ('wheelSlip', c_float * 4),
    ('wheelLoad', c_float * 4),
    ('wheelsPressure', c_float * 4),
    ('wheelAngularSpeed', c_float * 4),
    ('tyreWear', c_float * 4),
    ('tyreDirtyLevel', c_float * 4),
    ('tyreCoreTemperature', c_float * 4),
    ('camberRAD', c_float * 4),
    ('suspensionTravel', c_float * 4),
    ('drs', c_float),
    ('tc', c_float),
    ('heading', c_float),
    ('pitch', c_float),
    ('roll', c_float),
    ('cgHeight', c_float),
    ('carDamage', c_float * 5),
    ('numberOfTyresOut', c_int32),
    ('pitLimiterOn', c_int32),
    ('abs', c_float),
  ]

print(ctypes.sizeof(SPageFilePhysics))
mm = mmap.mmap(-1,tagname='acpmf_physics', length=ctypes.sizeof(SPageFilePhysics))

while True:
  mm.seek(0)
  rawData = mm.read(ctypes.sizeof(SPageFilePhysics))
  data = SPageFilePhysics.from_buffer_copy(rawData)
  print(
    f"packetId={data.packetId} "
    f"gas={data.gas:.2f} brake={data.brake:.2f} fuel={data.fuel:.2f} "
    f"gear={data.gear} rpm={data.rpm} steerAngle={data.steerAngle:.2f} "
    f"speedKmh={data.speedKmh:.2f} "
    f"velocity=({data.velocity[0]:.2f},{data.velocity[1]:.2f},{data.velocity[2]:.2f}) "
    f"accG=({data.accG[0]:.2f},{data.accG[1]:.2f},{data.accG[2]:.2f}) "
    f"wheelSlip=({data.wheelSlip[0]:.2f},{data.wheelSlip[1]:.2f},{data.wheelSlip[2]:.2f},{data.wheelSlip[3]:.2f}) "
    f"wheelLoad=({data.wheelLoad[0]:.1f},{data.wheelLoad[1]:.1f},{data.wheelLoad[2]:.1f},{data.wheelLoad[3]:.1f}) "
    f"wheelsPressure=({data.wheelsPressure[0]:.2f},{data.wheelsPressure[1]:.2f},{data.wheelsPressure[2]:.2f},{data.wheelsPressure[3]:.2f}) "
    f"wheelAngularSpeed=({data.wheelAngularSpeed[0]:.2f},{data.wheelAngularSpeed[1]:.2f},{data.wheelAngularSpeed[2]:.2f},{data.wheelAngularSpeed[3]:.2f}) "
    f"tyreWear=({data.tyreWear[0]:.2f},{data.tyreWear[1]:.2f},{data.tyreWear[2]:.2f},{data.tyreWear[3]:.2f}) "
    f"tyreDirtyLevel=({data.tyreDirtyLevel[0]:.2f},{data.tyreDirtyLevel[1]:.2f},{data.tyreDirtyLevel[2]:.2f},{data.tyreDirtyLevel[3]:.2f}) "
    f"tyreCoreTemperature=({data.tyreCoreTemperature[0]:.1f},{data.tyreCoreTemperature[1]:.1f},{data.tyreCoreTemperature[2]:.1f},{data.tyreCoreTemperature[3]:.1f}) "
    f"camberRAD=({data.camberRAD[0]:.3f},{data.camberRAD[1]:.3f},{data.camberRAD[2]:.3f},{data.camberRAD[3]:.3f}) "
    f"suspensionTravel=({data.suspensionTravel[0]:.3f},{data.suspensionTravel[1]:.3f},{data.suspensionTravel[2]:.3f},{data.suspensionTravel[3]:.3f}) "
    f"drs={data.drs:.2f} tc={data.tc:.2f} "
    f"heading={data.heading:.2f} pitch={data.pitch:.2f} roll={data.roll:.2f} "
    f"cgHeight={data.cgHeight:.3f} "
    f"carDamage=({data.carDamage[0]:.2f},{data.carDamage[1]:.2f},{data.carDamage[2]:.2f},{data.carDamage[3]:.2f},{data.carDamage[4]:.2f}) "
    f"tyresOut={data.numberOfTyresOut} pitLimiter={data.pitLimiterOn} abs={data.abs:.2f}"
)
  time.sleep(0.2)

  

