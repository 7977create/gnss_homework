// Auto-generated. Do not edit!

// (in-package gnss_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class location {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.pitch = null;
      this.roll = null;
      this.heading = null;
      this.longtitude = null;
      this.latitude = null;
      this.altitude = null;
      this.speed2d = null;
      this.Ve = null;
      this.Vn = null;
      this.Vu = null;
      this.GPStime = null;
      this.pose_type = null;
      this.INS_Status = null;
      this.Lat_vart = null;
      this.Lon_vart = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('pitch')) {
        this.pitch = initObj.pitch
      }
      else {
        this.pitch = 0.0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
      if (initObj.hasOwnProperty('heading')) {
        this.heading = initObj.heading
      }
      else {
        this.heading = 0.0;
      }
      if (initObj.hasOwnProperty('longtitude')) {
        this.longtitude = initObj.longtitude
      }
      else {
        this.longtitude = 0.0;
      }
      if (initObj.hasOwnProperty('latitude')) {
        this.latitude = initObj.latitude
      }
      else {
        this.latitude = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
      }
      if (initObj.hasOwnProperty('speed2d')) {
        this.speed2d = initObj.speed2d
      }
      else {
        this.speed2d = 0.0;
      }
      if (initObj.hasOwnProperty('Ve')) {
        this.Ve = initObj.Ve
      }
      else {
        this.Ve = 0.0;
      }
      if (initObj.hasOwnProperty('Vn')) {
        this.Vn = initObj.Vn
      }
      else {
        this.Vn = 0.0;
      }
      if (initObj.hasOwnProperty('Vu')) {
        this.Vu = initObj.Vu
      }
      else {
        this.Vu = 0.0;
      }
      if (initObj.hasOwnProperty('GPStime')) {
        this.GPStime = initObj.GPStime
      }
      else {
        this.GPStime = 0.0;
      }
      if (initObj.hasOwnProperty('pose_type')) {
        this.pose_type = initObj.pose_type
      }
      else {
        this.pose_type = 0;
      }
      if (initObj.hasOwnProperty('INS_Status')) {
        this.INS_Status = initObj.INS_Status
      }
      else {
        this.INS_Status = 0;
      }
      if (initObj.hasOwnProperty('Lat_vart')) {
        this.Lat_vart = initObj.Lat_vart
      }
      else {
        this.Lat_vart = 0.0;
      }
      if (initObj.hasOwnProperty('Lon_vart')) {
        this.Lon_vart = initObj.Lon_vart
      }
      else {
        this.Lon_vart = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type location
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [pitch]
    bufferOffset = _serializer.float32(obj.pitch, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float32(obj.roll, buffer, bufferOffset);
    // Serialize message field [heading]
    bufferOffset = _serializer.float32(obj.heading, buffer, bufferOffset);
    // Serialize message field [longtitude]
    bufferOffset = _serializer.float64(obj.longtitude, buffer, bufferOffset);
    // Serialize message field [latitude]
    bufferOffset = _serializer.float64(obj.latitude, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float64(obj.altitude, buffer, bufferOffset);
    // Serialize message field [speed2d]
    bufferOffset = _serializer.float32(obj.speed2d, buffer, bufferOffset);
    // Serialize message field [Ve]
    bufferOffset = _serializer.float64(obj.Ve, buffer, bufferOffset);
    // Serialize message field [Vn]
    bufferOffset = _serializer.float64(obj.Vn, buffer, bufferOffset);
    // Serialize message field [Vu]
    bufferOffset = _serializer.float64(obj.Vu, buffer, bufferOffset);
    // Serialize message field [GPStime]
    bufferOffset = _serializer.float64(obj.GPStime, buffer, bufferOffset);
    // Serialize message field [pose_type]
    bufferOffset = _serializer.int32(obj.pose_type, buffer, bufferOffset);
    // Serialize message field [INS_Status]
    bufferOffset = _serializer.int32(obj.INS_Status, buffer, bufferOffset);
    // Serialize message field [Lat_vart]
    bufferOffset = _serializer.float32(obj.Lat_vart, buffer, bufferOffset);
    // Serialize message field [Lon_vart]
    bufferOffset = _serializer.float32(obj.Lon_vart, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type location
    let len;
    let data = new location(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [pitch]
    data.pitch = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [heading]
    data.heading = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [longtitude]
    data.longtitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [latitude]
    data.latitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [speed2d]
    data.speed2d = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Ve]
    data.Ve = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vn]
    data.Vn = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Vu]
    data.Vu = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [GPStime]
    data.GPStime = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pose_type]
    data.pose_type = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [INS_Status]
    data.INS_Status = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [Lat_vart]
    data.Lat_vart = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [Lon_vart]
    data.Lon_vart = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 88;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gnss_pkg/location';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd10dd53c2060c0966a0cb0e0c08fa213';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
    
    float32     pitch         #俯仰角
    float32     roll            #翻滚角
    float32     heading     #航向角
    
    float64     longtitude  #经度
    float64     latitude      #纬度
    float64     altitude      #海拔
    
    float32     speed2d     #车辆速度
    #-------------------------------->
    float64     Ve               #向东速度
    float64     Vn               #向北速度
    float64     Vu               #天向速度
    #<-------------------------------
    float64    GPStime      #时间
    int32       pose_type   #定位状态
    int32       INS_Status  #解算状态
    float32    Lat_vart      #纬度标准差
    float32    Lon_vart     #经度标准差
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new location(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.pitch !== undefined) {
      resolved.pitch = msg.pitch;
    }
    else {
      resolved.pitch = 0.0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    if (msg.heading !== undefined) {
      resolved.heading = msg.heading;
    }
    else {
      resolved.heading = 0.0
    }

    if (msg.longtitude !== undefined) {
      resolved.longtitude = msg.longtitude;
    }
    else {
      resolved.longtitude = 0.0
    }

    if (msg.latitude !== undefined) {
      resolved.latitude = msg.latitude;
    }
    else {
      resolved.latitude = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
    }

    if (msg.speed2d !== undefined) {
      resolved.speed2d = msg.speed2d;
    }
    else {
      resolved.speed2d = 0.0
    }

    if (msg.Ve !== undefined) {
      resolved.Ve = msg.Ve;
    }
    else {
      resolved.Ve = 0.0
    }

    if (msg.Vn !== undefined) {
      resolved.Vn = msg.Vn;
    }
    else {
      resolved.Vn = 0.0
    }

    if (msg.Vu !== undefined) {
      resolved.Vu = msg.Vu;
    }
    else {
      resolved.Vu = 0.0
    }

    if (msg.GPStime !== undefined) {
      resolved.GPStime = msg.GPStime;
    }
    else {
      resolved.GPStime = 0.0
    }

    if (msg.pose_type !== undefined) {
      resolved.pose_type = msg.pose_type;
    }
    else {
      resolved.pose_type = 0
    }

    if (msg.INS_Status !== undefined) {
      resolved.INS_Status = msg.INS_Status;
    }
    else {
      resolved.INS_Status = 0
    }

    if (msg.Lat_vart !== undefined) {
      resolved.Lat_vart = msg.Lat_vart;
    }
    else {
      resolved.Lat_vart = 0.0
    }

    if (msg.Lon_vart !== undefined) {
      resolved.Lon_vart = msg.Lon_vart;
    }
    else {
      resolved.Lon_vart = 0.0
    }

    return resolved;
    }
};

module.exports = location;
