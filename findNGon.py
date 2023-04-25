# This example assumes we have a mesh object in edit-mode

import bpy
import bmesh

# change mode
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode(type="FACE")


# Get the active mesh
obj = bpy.context.edit_object
me = obj.data


# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

for face in bm.faces:
    if len(face.verts) == 4:
        face.select_set(False)
    else:
        face.select_set(True)

# bm.faces.active = None

# Modify the BMesh, can do anything here...
# for v in bm.verts:
#     v.co.x += 1.0


# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, True)
