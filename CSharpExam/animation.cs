//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from: ProtoExam/animation.proto
namespace ProtoExam.animation
{
  [global::System.Serializable, global::ProtoBuf.ProtoContract(Name=@"animation")]
  public partial class animation : global::ProtoBuf.IExtensible
  {
    public animation() {}
    
    private readonly global::System.Collections.Generic.List<animation.animationItem> _items = new global::System.Collections.Generic.List<animation.animationItem>();
    [global::ProtoBuf.ProtoMember(1, Name=@"items", DataFormat = global::ProtoBuf.DataFormat.Default)]
    public global::System.Collections.Generic.List<animation.animationItem> items
    {
      get { return _items; }
    }
  
  [global::System.Serializable, global::ProtoBuf.ProtoContract(Name=@"animationItem")]
  public partial class animationItem : global::ProtoBuf.IExtensible
  {
    public animationItem() {}
    
    private int _id;
    [global::ProtoBuf.ProtoMember(1, IsRequired = true, Name=@"id", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public int id
    {
      get { return _id; }
      set { _id = value; }
    }
    private string _name;
    [global::ProtoBuf.ProtoMember(2, IsRequired = true, Name=@"name", DataFormat = global::ProtoBuf.DataFormat.Default)]
    public string name
    {
      get { return _name; }
      set { _name = value; }
    }
    private string _coment;
    [global::ProtoBuf.ProtoMember(3, IsRequired = true, Name=@"coment", DataFormat = global::ProtoBuf.DataFormat.Default)]
    public string coment
    {
      get { return _coment; }
      set { _coment = value; }
    }
    private float _length;
    [global::ProtoBuf.ProtoMember(4, IsRequired = true, Name=@"length", DataFormat = global::ProtoBuf.DataFormat.FixedSize)]
    public float length
    {
      get { return _length; }
      set { _length = value; }
    }
    private string _keyframe;
    [global::ProtoBuf.ProtoMember(5, IsRequired = true, Name=@"keyframe", DataFormat = global::ProtoBuf.DataFormat.Default)]
    public string keyframe
    {
      get { return _keyframe; }
      set { _keyframe = value; }
    }
    private string _path;
    [global::ProtoBuf.ProtoMember(6, IsRequired = true, Name=@"path", DataFormat = global::ProtoBuf.DataFormat.Default)]
    public string path
    {
      get { return _path; }
      set { _path = value; }
    }
    private global::ProtoBuf.IExtension extensionObject;
    global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
      { return global::ProtoBuf.Extensible.GetExtensionObject(ref extensionObject, createIfMissing); }
  }
  
    private global::ProtoBuf.IExtension extensionObject;
    global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
      { return global::ProtoBuf.Extensible.GetExtensionObject(ref extensionObject, createIfMissing); }
  }
  
}