# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gnss_pkg/LaneLineArray.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import gnss_pkg.msg

class LaneLineArray(genpy.Message):
  _md5sum = "b311b16e049dce662db6f00b38186809"
  _type = "gnss_pkg/LaneLineArray"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
#------------------------------
#车道线序列
#------当前项目中车道线点序列长度为30
#------------------------------

LaneLine[]         lines

================================================================================
MSG: gnss_pkg/LaneLine

#------------------------------
#车道线
#------当前项目中车道线点序列长度为30
#------geometry_msgs/Point类型是（x,y,z),目前只填充x,y忽略z
#------s可以用来计算点位于地图的frenet的s坐标值
#------------------------------
uint32                         id
uint8                          type
float64[]                      x
float64[]                      y
float64[]                      s

geometry_msgs/Point[]          points
uint8                          current_lane_num
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['lines']
  _slot_types = ['gnss_pkg/LaneLine[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lines

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaneLineArray, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.lines is None:
        self.lines = []
    else:
      self.lines = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.lines)
      buff.write(_struct_I.pack(length))
      for val1 in self.lines:
        _x = val1
        buff.write(_get_struct_IB().pack(_x.id, _x.type))
        length = len(val1.x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.x))
        length = len(val1.y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.y))
        length = len(val1.s)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.Struct(pattern).pack(*val1.s))
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.current_lane_num
        buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.lines is None:
        self.lines = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lines = []
      for i in range(0, length):
        val1 = gnss_pkg.msg.LaneLine()
        _x = val1
        start = end
        end += 5
        (_x.id, _x.type,) = _get_struct_IB().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.x = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.y = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.s = s.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.points.append(val2)
        start = end
        end += 1
        (val1.current_lane_num,) = _get_struct_B().unpack(str[start:end])
        self.lines.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.lines)
      buff.write(_struct_I.pack(length))
      for val1 in self.lines:
        _x = val1
        buff.write(_get_struct_IB().pack(_x.id, _x.type))
        length = len(val1.x)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.x.tostring())
        length = len(val1.y)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.y.tostring())
        length = len(val1.s)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.s.tostring())
        length = len(val1.points)
        buff.write(_struct_I.pack(length))
        for val2 in val1.points:
          _x = val2
          buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _x = val1.current_lane_num
        buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.lines is None:
        self.lines = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.lines = []
      for i in range(0, length):
        val1 = gnss_pkg.msg.LaneLine()
        _x = val1
        start = end
        end += 5
        (_x.id, _x.type,) = _get_struct_IB().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.x = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.y = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.s = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.points = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Point()
          _x = val2
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
          val1.points.append(val2)
        start = end
        end += 1
        (val1.current_lane_num,) = _get_struct_B().unpack(str[start:end])
        self.lines.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_IB = None
def _get_struct_IB():
    global _struct_IB
    if _struct_IB is None:
        _struct_IB = struct.Struct("<IB")
    return _struct_IB
