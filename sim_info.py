import mmap
import ctypes
import time
import csv
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


AC_STATUS = c_int32
AC_SESSION_TYPE = c_int32

class SPageFileGraphic(ctypes.Structure):
    _pack_ = 4
    _fields_ = [
        ('packetId', c_int32),
        ('status', AC_STATUS),
        ('session', AC_SESSION_TYPE),
        ('currentTime', c_wchar * 15),
        ('lastTime', c_wchar * 15),
        ('bestTime', c_wchar * 15),
        ('split', c_wchar * 15),
        ('completedLaps', c_int32),
        ('position', c_int32),
        ('iCurrentTime', c_int32),
        ('iLastTime', c_int32),
        ('iBestTime', c_int32),
        ('sessionTimeLeft', c_float),
        ('distanceTraveled', c_float),
        ('isInPit', c_int32),
        ('currentSectorIndex', c_int32),
        ('lastSectorTime', c_int32),
        ('numberOfLaps', c_int32),
        ('tyreCompound', c_wchar * 33),
        ('replayTimeMultiplier', c_float),
        ('normalizedCarPosition', c_float),
        ('carCoordinates', c_float * 3),
    ]



mm = mmap.mmap(-1,tagname='acpmf_physics', length=ctypes.sizeof(SPageFilePhysics))
mm2 = mmap.mmap(-1, tagname='acpmf_graphics', length=ctypes.sizeof(SPageFileGraphic))

rawDataBefore = mm2.read(ctypes.sizeof(SPageFileGraphic))
dataBefore = SPageFileGraphic.from_buffer_copy(rawDataBefore)

with open('samples.csv', 'w', newline='') as samplecsv:
  writer = csv.writer(samplecsv)
  writer.writerow(['timestamp', 'lap', 'position', 'gas', 'brake', 'speed_kmh', 'rpm', 'gear', 'steer_angle'])
with open('laps.csv', 'w', newline='') as lapcsv:
  writer = csv.writer(lapcsv)
  writer.writerow(['lap', 'lap_time_ms', 'distanceTraveled','timestamp'])


prev_position = dataBefore.normalizedCarPosition
previous_laps = dataBefore.completedLaps  
current_lap = dataBefore.completedLaps + 1
while True:
  mm.seek(0)
  mm2.seek(0)

  
  rawData = mm.read(ctypes.sizeof(SPageFilePhysics))
  data = SPageFilePhysics.from_buffer_copy(rawData)

  
  rawData2 = mm2.read(ctypes.sizeof(SPageFileGraphic))
  data2 = SPageFileGraphic.from_buffer_copy(rawData2)

  if(prev_position - data2.normalizedCarPosition > 0.5):
    current_lap = current_lap + 1

 

  with open('samples.csv', 'a', newline='') as samplecsv:
    writer = csv.writer(samplecsv)
    writer.writerow([time.time(), current_lap, data2.normalizedCarPosition,
          data.gas, data.brake, data.speedKmh, data.rpm,
          data.gear, data.steerAngle])

  if previous_laps != current_lap:
    with open('laps.csv', 'a', newline='') as lapcsv:
      writer = csv.writer(lapcsv)
      writer.writerow([current_lap, data2.iLastTime, data2.distanceTraveled,time.time()])
    previous_laps = current_lap

  prev_position = data2.normalizedCarPosition
  time.sleep(0.05) # Rate 20 Hz 

  

