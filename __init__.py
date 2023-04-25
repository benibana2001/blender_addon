import bpy


bpy.ops.mesh.primitive_monkey_add()

bl_info = {
    "name" : "testAddon",
    "author" : "MyName",
    "description" : "tesuto dayo",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "category" : "Generic"
}

# from . import auto_load

# auto_load.init()

def register():
    print("Hello World")
    # auto_load.register()

def unregister():
#     auto_load.unregister()
    print("Goodbye World")
