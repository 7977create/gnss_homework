# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from gnss_pkg/LaneLine.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class LaneLine(genpy.Message):
  _md5sum = "f3ebb5bbdb4203b7c30588c0e1e0db20"
  _type = "gnss_pkg/LaneLine"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
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
  __slots__ = ['id','type','x','y','s','points','current_lane_num']
  _slot_types = ['uint32','uint8','float64[]','float64[]','float64[]','geometry_msgs/Point[]','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,type,x,y,s,points,current_lane_num

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaneLine, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.type is None:
        self.type = 0
      if self.x is None:
        self.x = []
      if self.y is None:
        self.y = []
      if self.s is None:
        self.s = []
      if self.points is None:
        self.points = []
      if self.current_lane_num is None:
        self.current_lane_num = 0
    else:
      self.id = 0
      self.type = 0
      self.x = []
      self.y = []
      self.s = []
      self.points = []
      self.current_lane_num = 0

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
      _x = self
      buff.write(_get_struct_IB().pack(_x.id, _x.type))
      length = len(self.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.x))
      length = len(self.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.y))
      length = len(self.s)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.s))
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self.current_lane_num
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
      if self.points is None:
        self.points = None
      end = 0
      _x = self
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
      self.x = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.y = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.s = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 1
      (self.current_lane_num,) = _get_struct_B().unpack(str[start:end])
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
      _x = self
      buff.write(_get_struct_IB().pack(_x.id, _x.type))
      length = len(self.x)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.x.tostring())
      length = len(self.y)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.y.tostring())
      length = len(self.s)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.s.tostring())
      length = len(self.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.points:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self.current_lane_num
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
      if self.points is None:
        self.points = None
      end = 0
      _x = self
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
      self.x = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.y = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.s = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.points = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.points.append(val1)
      start = end
      end += 1
      (self.current_lane_num,) = _get_struct_B().unpack(str[start:end])
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
