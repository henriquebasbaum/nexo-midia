"""Nexo 3D ACTING PILOT (not approved for publication).
Blender headless; a true 3D character with separate mouth, eyes, limbs,
gestures, reactions and 3D cards. Envelope lip sync is a prototype only.
"""
import bpy, math, wave, os, struct
from mathutils import Vector
from math import pi

OUT = os.environ.get("NEXO_OUT", "out")
os.makedirs(OUT + "/frames", exist_ok=True)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def material(name, rgb, rough=.55, emission=0):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*rgb, 1)
    m.use_nodes = True
    p = m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value = (*rgb, 1)
    p.inputs["Roughness"].default_value = rough
    if emission:
        p.inputs["Emission Color"].default_value = (*rgb, 1)
        p.inputs["Emission Strength"].default_value = emission
    return m

cyan = material("Nexo soft turquoise", (.02,.69,.79), .55)
teal = material("Nexo shadow turquoise", (.015,.40,.54), .58)
white = material("Eye whites", (.96,.98,.96), .22)
black = material("Pupils / mouth", (.004,.018,.036), .16)
shine = material("Eye catchlight", (1,1,1), .1, .7)
orange = material("Orange four-point star", (1,.31,.09), .3, .7)
navy = material("Cozy navy backdrop", (.012,.025,.10), .85)
floor_mat = material("Navy matte floor", (.016,.06,.15), .7)
card_mat = material("Warm translucent-looking card", (.85,.91,.98), .3)
title_mat = material("Dark card lettering", (.012,.04,.14), .5)
accent_mat = material("Cyan highlight", (.02,.62,.78), .4)

def sphere(name, pos, scale, mat, parent=None):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=(0,0,0))
    o = bpy.context.object
    o.name = name
    o.parent = parent
    o.location = pos
    o.scale = scale
    o.data.materials.append(mat)
    for poly in o.data.polygons:
        poly.use_smooth = True
    return o

def cube(name, pos, scale, mat, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0,0,0))
    o=bpy.context.object
    o.name=name
    o.parent=parent
    o.location=pos
    o.scale=scale
    o.data.materials.append(mat)
    bevel=o.modifiers.new("Soft corners","BEVEL")
    bevel.width=.10
    bevel.segments=3
    o.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
    return o

def text_obj(name, content, pos, size, mat, parent=None):
    cu=bpy.data.curves.new(name,"FONT")
    cu.body=content
    cu.size=size
    cu.space_line=1.18
    cu.extrude=.001
    ob=bpy.data.objects.new(name,cu)
    bpy.context.collection.objects.link(ob)
    ob.parent=parent
    ob.location=pos
    ob.rotation_euler=(pi/2,0,0)
    ob.data.materials.append(mat)
    return ob

# World, floor, cinematic lighting.
world=bpy.context.scene.world
world.color=(.01,.03,.08)
world.use_nodes=True
world.node_tree.nodes["Background"].inputs["Color"].default_value=(.016,.028,.08,1)
world.node_tree.nodes["Background"].inputs["Strength"].default_value=.55
cube("Floor",(0,0,-.08),(12,12,.12),floor_mat)
cube("Background wall",(0,2.2,2),(12,.10,8),navy)
def area(name, loc, energy, size, color):
    bpy.ops.object.light_add(type="AREA",location=loc)
    ob=bpy.context.object
    ob.name=name
    ob.data.energy=energy
    ob.data.shape="DISK"
    ob.data.size=size
    ob.data.color=color
    direction=Vector((0,0,1.5))-ob.location
    ob.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
area("Warm softbox",(-3,-4,5),550,5,(1,.70,.46))
area("Cool fill",(2,-3,3.8),440,4,(.30,.76,1))
area("Orange rim",(1.2,2,4),620,3,(1,.42,.18))

# Mascot is fully modelled in 3D, NOT a cut-out PNG.
body=sphere("Nexo body",(-.48,0,1.40),(.88,.66,.93),cyan)
feet=[sphere("Left foot",(-.91,-.10,.43),(.29,.38,.23),cyan),
      sphere("Right foot",(-.02,-.10,.43),(.29,.38,.23),cyan)]
arms=[]
for name,x,side in [("Left arm",-1.23,-1),("Right arm",.25,1)]:
    pivot=bpy.data.objects.new(name+" joint",None)
    bpy.context.collection.objects.link(pivot)
    pivot.location=(x,-.05,1.22)
    sphere(name+" paw",(side*.14,-.26,-.17),(.24,.26,.36),cyan,pivot)
    arms.append(pivot)

eyes=[]
for side,x in [("L",-.80),("R",-.14)]:
    eyeball=sphere(side+" eye white",(x,-.566,1.76),(.245,.19,.30),white)
    pupil=sphere(side+" pupil",(x+.06,-.735,1.75),(.143,.09,.204),black)
    sphere(side+" eye highlight",(x+.02,-.817,1.85),(.047,.024,.060),shine)
    eyes.append((eyeball,pupil))
mouth=sphere("Mouth (speech animated)",(-.46,-.654,1.17),(.19,.055,.065),black)
# Orange four-point sparkle: raised 3D silhouette in X/Z plane.
vertices=[]
for i in range(8):
    a=pi*i/4
    r=.34 if i%2==0 else .105
    vertices.append((.86+math.cos(a)*r,-.1,2.79+math.sin(a)*r))
vertices += [(.86,-.19,2.79)]
faces=[(i,(i+1)%8,8) for i in range(8)]
mesh=bpy.data.meshes.new("Star mesh")
mesh.from_pydata(vertices,[],faces)
mesh.materials.append(orange)
star=bpy.data.objects.new("Canonical orange star",mesh)
bpy.context.collection.objects.link(star)

# Nexo physically points at cards; cards exist as 3D scene geometry.
def make_card(name, heading, body_text):
    root=bpy.data.objects.new(name+" animated root",None)
    bpy.context.collection.objects.link(root)
    root.location=(.87,-.08,1.66)
    cube(name+" board",(0,0,0),(1.58,.12,1.19),card_mat,root)
    text_obj(name+" heading",heading,(-.68,-.09,.32),.15,title_mat,root)
    text_obj(name+" example",body_text,(-.68,-.09,.03),.125,title_mat,root)
    return root

bad=make_card("Vague prompt","PROMPT VAGO","Organize meu dia.")
good=make_card("Useful prompt","COM CONTEXTO","Tenho 90 min.\\n3 tarefas e\\n10 min de folga.")
def key(obj, frame, prop, value):
    setattr(obj,prop,value)
    obj.keyframe_insert(data_path=prop,frame=frame)

for frame,sc in [(1,(1,1,1)),(41,(1,1,1)),(46,(0,0,0))]:
    key(bad,frame,"scale",sc)
for frame,sc in [(1,(0,0,0)),(41,(0,0,0)),(46,(1,1,1)),(96,(1,1,1))]:
    key(good,frame,"scale",sc)

# Body acting: nod, lean, happy bounce; arms gesture toward the cards.
for frame,loc in [(1,(-.48,0,1.40)),(19,(-.48,0,1.37)),
                  (36,(-.52,0,1.41)),(53,(-.46,0,1.49)),
                  (70,(-.48,0,1.42)),(96,(-.48,0,1.44))]:
    key(body,frame,"location",loc)
for frame,angle in [(1,0),(16,-.08),(32,-.11),(48,.12),(72,.04),(96,0)]:
    body.rotation_euler=(0,angle,0)
    body.keyframe_insert(data_path="rotation_euler",frame=frame)
for arm,sequence in [(arms[0],[(1,0),(19,-.35),(39,-.15),(55,.22),(78,.05),(96,0)]),
                     (arms[1],[(1,0),(18,-.4),(39,-.9),(53,-1.0),(72,-.6),(96,-.2)])]:
    for frame,ang in sequence:
        arm.rotation_euler=(0,ang,0)
        arm.keyframe_insert(data_path="rotation_euler",frame=frame)
for frame,angle in [(1,0),(26,.1),(46,-.08),(63,.13),(96,0)]:
    star.rotation_euler=(0,angle,0)
    star.keyframe_insert(data_path="rotation_euler",frame=frame)

# Real blinking eyelids via independent 3D eye geometry, not sprite swap.
for eye,pupil in eyes:
    for frame,zscale in [(1,1),(21,1),(22,.08),(24,1),
                         (60,1),(61,.07),(63,1),(88,1),(89,.08),(91,1),(96,1)]:
        eye.scale.z=.30*zscale
        pupil.scale.z=.204*zscale
        eye.keyframe_insert(data_path="scale",frame=frame)
        pupil.keyframe_insert(data_path="scale",frame=frame)

# Speech envelope drives the mouth on each rendered frame (prototype, not phonetic visemes).
audio=os.path.join(OUT,"nexo.wav")
energy=[]
if os.path.exists(audio):
    with wave.open(audio,"rb") as w:
        sr=w.getframerate()
        raw=w.readframes(w.getnframes())
        sw=w.getsampwidth()
        if sw==2:
            samples=struct.unpack("<%dh"%(len(raw)//2),raw)
            for f in range(96):
                t=f/12
                chunk=samples[int(t*sr):int((t+.06)*sr)]
                rms=math.sqrt(sum(s*s for s in chunk)/max(1,len(chunk)))/32768
                energy.append(rms)
for f in range(1,97):
    e=energy[f-1] if len(energy)>=f else 0
    mouth.scale.z=.045+min(.19,max(0,e*5))
    mouth.scale.x=.19+min(.03,e)
    mouth.keyframe_insert(data_path="scale",frame=f)

bpy.ops.object.camera_add(location=(0,-8.5,2.3))
camera=bpy.context.object
direction=Vector((0,0,1.55))-camera.location
camera.rotation_euler=direction.to_track_quat("-Z","Y").to_euler()
camera.data.type="ORTHO"
camera.data.ortho_scale=4.75
bpy.context.scene.camera=camera
for frame,scale in [(1,4.75),(48,4.55),(96,4.45)]:
    camera.data.ortho_scale=scale
    camera.data.keyframe_insert(data_path="ortho_scale",frame=frame)

scene=bpy.context.scene
scene.render.engine="BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items] else "BLENDER_EEVEE"
scene.render.resolution_x=360
scene.render.resolution_y=640
scene.render.resolution_percentage=100
scene.render.fps=12
scene.frame_start=1
scene.frame_end=96
scene.render.image_settings.file_format="PNG"
scene.render.filepath=OUT+"/frames/frame_"
scene.camera.data.lens=35
scene.view_settings.view_transform="Standard"
bpy.ops.wm.save_as_mainfile(filepath=OUT+"/nexo_3d_pilot.blend")
bpy.ops.render.render(animation=True)
print("PILOT_DONE",OUT)
