# Rigging


## Rigging


### Crear un armature (esqueleto) básico

*Blender · Basic*

```python
import bpy
bpy.ops.object.armature_add(location=(0, 0, 0))
```


### Añadir un prefijo a los huesos seleccionados

*Blender · Intermediate*

Ejecútalo en modo edición del armature, con los huesos seleccionados.

```python
import bpy
for bone in bpy.context.selected_editable_bones:
    bone.name = "DEF_" + bone.name
```


### Crear una cadena de 3 joints en el origen

*Maya · Intermediate*

```python
import maya.cmds as cmds
cmds.select(clear=True)
cmds.joint(position=(0, 0, 0), name="joint_root")
cmds.joint(position=(0, 5, 0), name="joint_mid")
cmds.joint(position=(0, 10, 0), name="joint_end")
```


### Crear un IK handle entre dos joints

*Maya · Advanced*

Ajusta los nombres de los joints a los tuyos.

```python
import maya.cmds as cmds
cmds.ikHandle(startJoint="joint_root",
              endEffector="joint_end",
              solver="ikRPsolver")
```


### Crear grupo Offset (Zero Group) para los controles seleccionados

*Maya · Intermediate*

Crea un grupo padre en la misma posición que cada control seleccionado, para tener un "cero" limpio sobre el que animar.

```python
from maya import cmds as cmds
controls = cmds.ls(sl=True)
for i in controls:
    off = cmds.createNode("transform", name=i.replace("_CTL", "Ctl_OFF"))
    cmds.delete(cmds.parentConstraint(i, off))
    cmds.parent(i, off)
```


### Convertir un objeto poligonal en control de curva

*Maya · Advanced*

Convierte los bordes de la malla poligonal seleccionada en un control de curva con la misma silueta, ya centrado con su grupo Offset.

```python
import maya.cmds as cmds

def convertir_poly_3d_a_control():
    sel = cmds.ls(sl=True)
    if not sel:
        return
    obj = sel[0]
    pos = cmds.xform(obj, q=True, rp=True, ws=True)
    rot = cmds.xform(obj, q=True, ro=True, ws=True)
    temp_crvs = []
    edges = cmds.polyEvaluate(obj, e=True)
    for i in range(edges):
        c = cmds.polyToCurve(f"{obj}.e[{i}]", f=2, dg=1, ch=False)
        if c:
            temp_crvs.append(c[0])
    main_ctrl = cmds.group(em=True, n=obj + "Ctl")
    for crv in temp_crvs:
        shape = cmds.listRelatives(crv, s=True)[0]
        cmds.parent(shape, main_ctrl, r=True, s=True)
        cmds.delete(crv)
    off_grp = cmds.group(em=True, n=main_ctrl + "_OFF")
    cmds.xform(off_grp, ws=True, t=pos)
    cmds.xform(off_grp, ws=True, ro=rot)
    cmds.parent(main_ctrl, off_grp)
    cmds.setAttr(main_ctrl + ".t", 0, 0, 0)
    cmds.setAttr(main_ctrl + ".r", 0, 0, 0)
    cmds.select(main_ctrl)

convertir_poly_3d_a_control()
```


### Fusionar varias curvas de control en un único transform

*Maya · Advanced*

Selecciona primero las curvas a fusionar y en último lugar el control destino. Congela transformaciones antes de fusionar.

```python
import maya.cmds as cmds

def fusionar_controles():
    sel = cmds.ls(sl=True)
    if len(sel) < 2:
        cmds.warning("Selecciona 2 o más curvas.")
        return
    destino = sel[-1]
    fuentes = sel[:-1]
    cmds.makeIdentity(sel, apply=True, t=1, r=1, s=1, n=0)
    for obj in fuentes:
        shapes = cmds.listRelatives(obj, s=True, f=True)
        if shapes:
            for s in shapes:
                cmds.parent(s, destino, r=True, s=True)
            cmds.delete(obj)
    cmds.select(destino)
    print("Fusión completada con éxito.")

fusionar_controles()
```


### Auto-crear controles FK sobre una cadena de joints

*Maya · Advanced*

Selecciona los joints en el Outliner antes de ejecutar. Crea, por cada joint, un control circular con su jerarquía OFF/DRV y lo conecta con parentConstraint.

```python
from maya import cmds as cmds

# Añadimos a la variable joints la lista que tenemos seleccionada en el outliner
joints = cmds.ls(sl=True)
for i in joints:
    # Creamos los controles y nos aseguramos de coger los controles y no la shape
    ctl = cmds.circle(name=i.replace("_JNT", "_CTL"), nr=(0, 1, 0), r=5)[0]
    # Guardamos también la shape en una variable para cambiar los colores de los controles
    shape = cmds.listRelatives(ctl, children=True)[0]
    cmds.setAttr(shape + ".overrideEnabled", 1)
    cmds.setAttr(shape + ".overrideColor", 23)
    # Ponemos los controles en la misma posición y orientación que los huesos
    cmds.delete(cmds.parentConstraint(i, ctl))
    # Creamos grupos DRV y OFF y los ponemos en la misma pos/orientación que los huesos
    drv = cmds.createNode("transform", name=i.replace("_JNT", "Ctl_DRV"))
    off = cmds.createNode("transform", name=i.replace("_JNT", "Ctl_OFF"))
    cmds.delete(cmds.parentConstraint(i, drv))
    cmds.delete(cmds.parentConstraint(i, off))
    # Emparentamos
    cmds.parent(drv, off)
    cmds.parent(ctl, drv)
    # Los controles mandan sobre los joints
    cmds.parentConstraint(ctl, i)
```


### Auto-crear controles sobre una cadena de joints (variante con orientConstraint)

*Maya · Advanced*

Igual que el anterior pero conecta con orientConstraint en vez de parentConstraint (solo transmite rotación).

```python
from maya import cmds as cmds

# Añadimos a la variable joints la lista que tenemos seleccionada en el outliner
joints = cmds.ls(sl=True)
for i in joints:
    # Creamos los controles y nos aseguramos de coger los controles y no la shape
    ctl = cmds.circle(name=i.replace("_JNT", "_CTL"), nr=(0, 1, 0), r=5)[0]
    # Guardamos también la shape en una variable para cambiar los colores de los controles
    shape = cmds.listRelatives(ctl, children=True)[0]
    cmds.setAttr(shape + ".overrideEnabled", 1)
    cmds.setAttr(shape + ".overrideColor", 23)
    # Ponemos los controles en la misma posición y orientación que los huesos
    cmds.delete(cmds.parentConstraint(i, ctl))
    # Creamos grupos DRV y OFF y los ponemos en la misma pos/orientación que los huesos
    drv = cmds.createNode("transform", name=i.replace("_JNT", "Ctl_DRV"))
    off = cmds.createNode("transform", name=i.replace("_JNT", "Ctl_OFF"))
    cmds.delete(cmds.parentConstraint(i, drv))
    cmds.delete(cmds.parentConstraint(i, off))
    # Emparentamos
    cmds.parent(drv, off)
    cmds.parent(ctl, drv)
    # Los controles mandan sobre los joints (solo orientación)
    cmds.orientConstraint(ctl, i)
```


### Creación de cadenas IK/FK a partir de la cadena original

*Maya · Advanced*

Crea varias cadenas de huesos para los IK - FK - Weight Paint.

```python
"""
FK/IK SETUP - script directo para el Script Editor de Maya
==========================================================
Pegalo entero en la pestana Python del Script Editor y ejecutalo: se abre
la ventana. No hace falta instalar nada ni copiarlo a la carpeta scripts.

Para el boton de shelf: selecciona todo el texto en el Script Editor y
arrastralo al shelf con el boton central del raton (la rueda). Si Maya
pregunta el lenguaje, elige Python.

QUE ESPERA
----------
Que las tres cadenas ya existan, hechas por ti, con esta convencion:

    cadena de bind      brazo_L_JNT
    cadena FK           brazo_L_FK_JNT
    cadena IK           brazo_L_IK_JNT

El token FK o IK va en el penultimo bloque del nombre. Puedes seleccionar
cualquiera de las tres cadenas, o solo su primer joint: el script deduce
las otras dos por nombre y avisa si falta alguna. No modifica tu esqueleto,
solo crea los controles y las conexiones que los unen.

QUE CREA
--------
    control FK          brazo_L_FK_CTL     (uno por joint, jerarquizados)
    control IK          muneca_L_IK_CTL    (del ultimo joint de la cadena)
    pole vector         brazo_L_PV_CTL
    switch              brazo_L_FKIK_CTL   con el atributo FKIK (0 = FK, 1 = IK)
    ikHandle            brazo_L_IKH        (ikRPsolver, dentro del control IK)

Conecta la cadena de bind a las dos driver: parentConstraint en la raiz,
orientConstraint en el resto, con un nodo reverse gobernado por el switch.

SNAP
----
Los botones "Snap a FK" y "Snap a IK" de la ventana funcionan con el
control de switch seleccionado.

ANTES DE EJECUTAR
-----------------
- Los joints deben tener las rotaciones a cero y el orient ya resuelto.
- Los nombres de nodo en Maya no admiten tildes ni enyes.
- Si tus huesos no apuntan por X, cambia FK_NORMAL en la configuracion.
"""

import json

from maya import cmds
import maya.api.OpenMaya as om


# =============================================================================
# CONFIGURACION
# =============================================================================

CTL_SUFFIX = "_CTL"
OFF_SUFFIX = "_OFF"
DRV_SUFFIX = "_DRV"
GRP_SUFFIX = "_GRP"

FK_TOKEN = "FK"
IK_TOKEN = "IK"

SWITCH_ATTR = "FKIK"        # 0 = FK, 1 = IK
META_ATTR = "fkikData"      # atributo oculto con el montaje serializado

COLOR_FK = 23               # verde
COLOR_IK = 17               # amarillo
COLOR_PV = 20               # rosa
COLOR_SWITCH = 18           # cian

FK_NORMAL = (1, 0, 0)       # eje por el que "mira" el circulo FK.
                            # Si tus huesos apuntan por Y o Z, cambialo aqui.


# =============================================================================
# UTILIDADES DE NOMBRE
# =============================================================================

def _short(name):
    """Nombre corto y sin namespace."""
    return name.split("|")[-1].split(":")[-1]


def _namespace(name):
    """Devuelve el namespace con los dos puntos, o cadena vacia."""
    short = name.split("|")[-1]
    return short.rsplit(":", 1)[0] + ":" if ":" in short else ""


def _insert_token(name, token):
    """brazo_L_JNT  ->  brazo_L_FK_JNT   (conserva el namespace)"""
    namespace = _namespace(name)
    parts = _short(name).split("_")
    if len(parts) < 2:
        return namespace + "{0}_{1}".format(parts[0], token)
    parts.insert(len(parts) - 1, token)
    return namespace + "_".join(parts)


def _strip_token(name):
    """brazo_L_FK_JNT  ->  brazo_L_JNT   (solo si el token esta donde toca)"""
    namespace = _namespace(name)
    parts = _short(name).split("_")
    if len(parts) >= 3 and parts[-2] in (FK_TOKEN, IK_TOKEN):
        del parts[-2]
    return namespace + "_".join(parts)


def _has_token(name):
    parts = _short(name).split("_")
    return len(parts) >= 3 and parts[-2] in (FK_TOKEN, IK_TOKEN)


def _swap_suffix(name, new_suffix):
    """brazo_L_FK_JNT  ->  brazo_L_FK_CTL   (cambia el ultimo bloque)"""
    namespace = _namespace(name)
    parts = _short(name).split("_")
    if len(parts) > 1:
        parts = parts[:-1]
    return namespace + "_".join(parts) + new_suffix


def _base_name(name):
    """brazo_L_FK_JNT  ->  brazo_L"""
    return _swap_suffix(_strip_token(name), "")


# =============================================================================
# LECTURA Y VALIDACION DE LAS TRES CADENAS
# =============================================================================

def _ancestors(long_name):
    parts = long_name.split("|")[1:]
    return ["|" + "|".join(parts[:i]) for i in range(1, len(parts))]


def _ordered_chain(joints):
    """Ordena de raiz a punta y valida que sea una cadena continua.

    Si se pasa un solo joint, recorre hacia abajo toda su descendencia.
    """
    longs = cmds.ls(joints, long=True, type="joint") or []
    if not longs:
        raise RuntimeError("Selecciona joints, no otro tipo de nodo.")

    if len(longs) == 1:
        ordered, current = [longs[0]], longs[0]
        while True:
            children = cmds.listRelatives(current, children=True, type="joint",
                                          fullPath=True) or []
            if len(children) != 1:
                break
            ordered.append(children[0])
            current = children[0]
    else:
        selected = set(longs)
        roots = [j for j in longs if not (set(_ancestors(j)) & selected)]
        if len(roots) != 1:
            raise RuntimeError(
                "La seleccion contiene {0} cadenas distintas. Selecciona una "
                "sola.".format(len(roots)))

        ordered, current = [roots[0]], roots[0]
        while True:
            children = cmds.listRelatives(current, children=True, type="joint",
                                          fullPath=True) or []
            following = [c for c in children if c in selected]
            if len(following) > 1:
                raise RuntimeError(
                    "El joint {0} tiene mas de un hijo seleccionado. La "
                    "cadena debe ser lineal.".format(_short(current)))
            if not following:
                break
            ordered.append(following[0])
            current = following[0]

        if len(ordered) != len(longs):
            raise RuntimeError(
                "Los joints seleccionados no forman una cadena continua "
                "padre-hijo.")

    if len(ordered) < 3:
        raise RuntimeError(
            "La cadena necesita al menos 3 joints (raiz, medio y punta).")
    return ordered


def _verify_chain(joints, label):
    """Comprueba que la lista sea realmente una cadena padre-hijo."""
    for i in range(1, len(joints)):
        parents = cmds.listRelatives(joints[i], parent=True, fullPath=True)
        expected = cmds.ls(joints[i - 1], long=True)[0]
        if not parents or cmds.ls(parents[0], long=True)[0] != expected:
            raise RuntimeError(
                "En la cadena {0}, el joint {1} no cuelga de {2}. Revisa la "
                "jerarquia.".format(label, _short(joints[i]),
                                    _short(joints[i - 1])))


def _resolve_chains(selection=None):
    """A partir de cualquiera de las tres cadenas, devuelve las tres.

    Returns
    -------
    (bind, fk, ik) : tres listas de joints ordenadas de raiz a punta.
    """
    chain = _ordered_chain(selection or cmds.ls(selection=True))

    # La cadena de bind es la version sin token del nombre.
    bind_names = [_strip_token(j) for j in chain]

    missing = []
    bind, fk, ik = [], [], []
    for name in bind_names:
        fk_name = _insert_token(name, FK_TOKEN)
        ik_name = _insert_token(name, IK_TOKEN)
        for candidate, bucket in ((name, bind), (fk_name, fk), (ik_name, ik)):
            if not cmds.objExists(candidate):
                missing.append(candidate)
            elif cmds.nodeType(candidate) != "joint":
                missing.append(candidate + "   (existe pero no es un joint)")
            else:
                found = cmds.ls(candidate, long=True, type="joint")
                if len(found) > 1:
                    raise RuntimeError(
                        "Hay mas de un nodo llamado {0}. Los nombres deben "
                        "ser unicos.".format(candidate))
                bucket.append(found[0])

    if missing:
        raise RuntimeError(
            "No encuentro estos joints. Revisa que las tres cadenas existan "
            "y sigan la convencion nombre_lado_FK_JNT:\n  "
            + "\n  ".join(missing))

    _verify_chain(bind, "de bind")
    _verify_chain(fk, "FK")
    _verify_chain(ik, "IK")

    # Aviso si las cadenas driver no estan encima de la de bind.
    tolerance = max(_chain_length(bind) * 0.01, 0.001)
    for reference, driver, label in ((bind, fk, "FK"), (bind, ik, "IK")):
        for a, b in zip(reference, driver):
            if (_world_pos(a) - _world_pos(b)).length() > tolerance:
                cmds.warning(
                    "El joint {0} de la cadena {1} no coincide con {2}. El "
                    "montaje se hara igual, pero revisalo."
                    .format(_short(b), label, _short(a)))
                break

    return bind, fk, ik


# =============================================================================
# GEOMETRIA DE CONTROLES
# =============================================================================

_CUBE = [(-1, 1, 1), (1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1),
         (-1, -1, 1), (1, -1, 1), (1, 1, 1), (1, -1, 1), (1, -1, -1),
         (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1), (-1, -1, -1),
         (-1, -1, 1)]

_DIAMOND = [(0, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 0), (-1, 0, 0),
            (0, 0, -1), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0),
            (0, 0, -1), (1, 0, 0), (0, -1, 0), (0, 0, 1)]

_CROSS = [(-0.5, 0, 0.2), (-0.2, 0, 0.2), (-0.2, 0, 0.5), (0.2, 0, 0.5),
          (0.2, 0, 0.2), (0.5, 0, 0.2), (0.5, 0, -0.2), (0.2, 0, -0.2),
          (0.2, 0, -0.5), (-0.2, 0, -0.5), (-0.2, 0, -0.2), (-0.5, 0, -0.2),
          (-0.5, 0, 0.2)]


def _rename_shapes(ctl):
    for shape in cmds.listRelatives(ctl, shapes=True, fullPath=True) or []:
        cmds.rename(shape, "{0}Shape".format(_short(ctl)))


def _set_color(ctl, color):
    for shape in cmds.listRelatives(ctl, shapes=True, fullPath=True) or []:
        cmds.setAttr(shape + ".overrideEnabled", 1)
        cmds.setAttr(shape + ".overrideColor", color)


def _make_circle(name, radius, color):
    ctl = cmds.circle(name=name, normal=FK_NORMAL, radius=radius,
                      constructionHistory=False)[0]
    _rename_shapes(ctl)
    _set_color(ctl, color)
    return ctl


def _make_curve(name, points, size, color):
    scaled = [(p[0] * size, p[1] * size, p[2] * size) for p in points]
    ctl = cmds.rename(cmds.curve(name=name, degree=1, point=scaled), name)
    _rename_shapes(ctl)
    _set_color(ctl, color)
    return ctl


def _offset_groups(ctl, match_to=None):
    """Crea los grupos OFF y DRV encima del control.

    OFF  ->  coloca el control sin ensuciar sus canales.
    DRV  ->  capa libre para constraints, correctivos o set driven keys.
    """
    base = _swap_suffix(ctl, "")
    off = cmds.createNode("transform", name=base + OFF_SUFFIX)
    drv = cmds.createNode("transform", name=base + DRV_SUFFIX)

    if match_to:
        for node in (off, drv, ctl):
            cmds.delete(cmds.parentConstraint(match_to, node))

    cmds.parent(drv, off)
    cmds.parent(ctl, drv)
    return off, drv


def _lock_hide(node, attrs):
    for attr in attrs:
        plug = "{0}.{1}".format(node, attr)
        if not cmds.objExists(plug):
            continue
        try:
            cmds.setAttr(plug, lock=True, keyable=False, channelBox=False)
        except RuntimeError:
            pass


# =============================================================================
# MATEMATICAS DEL POLE VECTOR
# =============================================================================

def _world_pos(node):
    return om.MVector(*cmds.xform(node, query=True, worldSpace=True,
                                  translation=True))


def _chain_length(joints):
    return sum((_world_pos(joints[i + 1]) - _world_pos(joints[i])).length()
               for i in range(len(joints) - 1))


def _pole_vector_position(start, mid, end, distance=None):
    """Posicion del pole vector, dentro del plano que forman los tres joints.

    Se proyecta el joint medio sobre la linea raiz-punta y se sale de esa
    proyeccion hacia el medio. Asi el control queda siempre delante o detras
    del codo, nunca de lado, y el codo no se mueve al crear el constraint.
    """
    p0, p1, p2 = _world_pos(start), _world_pos(mid), _world_pos(end)

    line = p2 - p0
    if line.length() < 1e-5:
        raise RuntimeError("El primer y el ultimo joint estan en el mismo sitio.")

    point = p1 - p0
    projection = p0 + line * ((point * line) / (line * line))
    arrow = p1 - projection

    if arrow.length() < 1e-5:
        # Cadena perfectamente recta: no hay plano. Usamos el eje Z del medio.
        matrix = cmds.xform(mid, query=True, worldSpace=True, matrix=True)
        arrow = om.MVector(matrix[8], matrix[9], matrix[10])

    if distance is None:
        distance = ((p1 - p0).length() + (p2 - p1).length()) * 0.5

    return projection + arrow.normal() * distance


# =============================================================================
# CONSTRUCCION PRINCIPAL
# =============================================================================

def build_fkik(selection=None, limb_name=None, ctl_size=None, pv_distance=None,
               mid_index=None, lock_attrs=True, hide_drivers=True):
    """Monta controles, ikHandle, switch y blend sobre tres cadenas existentes.

    selection     cualquiera de las tres cadenas. None = seleccion actual.
    limb_name     prefijo para los nodos comunes. Por defecto se deduce del
                  primer joint (brazo_L_JNT -> brazo_L).
    ctl_size      radio de los controles. None = 15% de la cadena.
    pv_distance   separacion del pole vector. None = media cadena.
    mid_index     indice del joint que hace de codo o rodilla.
                  None = el del medio.
    lock_attrs    bloquea los canales que el animador no debe tocar.
    hide_drivers  apaga la visibilidad de las cadenas FK e IK.
    """
    cmds.undoInfo(openChunk=True)
    try:
        bind, fk_joints, ik_joints = _resolve_chains(selection)

        limb = limb_name or _base_name(bind[0])
        if mid_index is None:
            mid_index = len(bind) // 2
        if not 0 < mid_index < len(bind) - 1:
            raise RuntimeError(
                "mid_index debe apuntar a un joint intermedio de la cadena.")

        if ctl_size is None:
            ctl_size = max(_chain_length(bind) * 0.15, 0.01)

        # ---------------------------------------------------------------
        # 1. Grupo raiz de los controles
        # ---------------------------------------------------------------
        root_grp = cmds.createNode("transform", name=limb + "_FKIK" + GRP_SUFFIX)

        # ---------------------------------------------------------------
        # 2. Controles FK
        # ---------------------------------------------------------------
        fk_ctls, fk_offs = [], []
        for i, jnt in enumerate(fk_joints):
            ctl = _make_circle(_swap_suffix(jnt, CTL_SUFFIX), ctl_size, COLOR_FK)
            off, _ = _offset_groups(ctl, match_to=jnt)
            # La jerarquia de controles copia la del esqueleto: es lo que
            # permite usar parentConstraint sin dobles transformaciones.
            cmds.parent(off, fk_ctls[i - 1] if i else root_grp)
            cmds.parentConstraint(ctl, jnt, maintainOffset=True)
            fk_ctls.append(ctl)
            fk_offs.append(off)

        # ---------------------------------------------------------------
        # 3. Control IK, pole vector e ikHandle
        # ---------------------------------------------------------------
        ik_ctl = _make_curve(_swap_suffix(ik_joints[-1], CTL_SUFFIX),
                             _CUBE, ctl_size, COLOR_IK)
        ik_off, _ = _offset_groups(ik_ctl, match_to=ik_joints[-1])
        cmds.parent(ik_off, root_grp)

        pv_ctl = _make_curve(limb + "_PV" + CTL_SUFFIX, _DIAMOND,
                             ctl_size * 0.6, COLOR_PV)
        pv_off, _ = _offset_groups(pv_ctl)
        pv_pos = _pole_vector_position(ik_joints[0], ik_joints[mid_index],
                                       ik_joints[-1], pv_distance)
        cmds.xform(pv_off, worldSpace=True, translation=list(pv_pos))
        cmds.parent(pv_off, root_grp)

        handle, effector = cmds.ikHandle(
            startJoint=ik_joints[0], endEffector=ik_joints[-1],
            solver="ikRPsolver", name=limb + "_IKH")
        cmds.rename(effector, limb + "_EFF")
        cmds.setAttr(handle + ".visibility", 0)
        cmds.poleVectorConstraint(pv_ctl, handle)
        cmds.parent(handle, ik_ctl)

        # El ikHandle posiciona la punta pero no la orienta: de eso se
        # encarga el control con un orientConstraint. Si fuese
        # parentConstraint estariamos peleando con el solver por el translate.
        cmds.orientConstraint(ik_ctl, ik_joints[-1], maintainOffset=True)

        # ---------------------------------------------------------------
        # 4. Control de switch
        # ---------------------------------------------------------------
        switch_ctl = _make_curve(limb + "_FKIK" + CTL_SUFFIX, _CROSS,
                                 ctl_size * 1.2, COLOR_SWITCH)
        switch_off, _ = _offset_groups(switch_ctl, match_to=bind[-1])
        cmds.xform(switch_off, relative=True, worldSpace=True,
                   translation=(0, ctl_size * 2.5, 0))
        cmds.parent(switch_off, root_grp)
        cmds.parentConstraint(bind[-1], switch_off, maintainOffset=True)

        cmds.addAttr(switch_ctl, longName=SWITCH_ATTR, attributeType="float",
                     min=0, max=1, defaultValue=0, keyable=True)
        switch_plug = "{0}.{1}".format(switch_ctl, SWITCH_ATTR)

        # ---------------------------------------------------------------
        # 5. Blend de las dos cadenas sobre la de bind
        # ---------------------------------------------------------------
        reverse_node = cmds.createNode("reverse", name=limb + "_FKIK_REV")
        cmds.connectAttr(switch_plug, reverse_node + ".inputX")

        for i, jnt in enumerate(bind):
            # Raiz: parentConstraint, porque necesita heredar posicion.
            # Resto: orientConstraint, porque su posicion ya viene por
            # jerarquia y escribir en su translate romperia el hueso.
            if i == 0:
                con = cmds.parentConstraint(fk_joints[i], ik_joints[i], jnt,
                                            maintainOffset=True)[0]
            else:
                con = cmds.orientConstraint(fk_joints[i], ik_joints[i], jnt,
                                            maintainOffset=True)[0]

            command = getattr(cmds, cmds.nodeType(con))
            fk_alias, ik_alias = command(con, query=True, weightAliasList=True)
            cmds.connectAttr(switch_plug, "{0}.{1}".format(con, ik_alias))
            cmds.connectAttr(reverse_node + ".outputX",
                             "{0}.{1}".format(con, fk_alias))
            cmds.setAttr(con + ".interpType", 2)   # shortest, evita flips

        # Visibilidad de cada set de controles
        cmds.connectAttr(reverse_node + ".outputX", fk_offs[0] + ".visibility")
        cmds.connectAttr(switch_plug, ik_off + ".visibility")
        cmds.connectAttr(switch_plug, pv_off + ".visibility")

        if hide_drivers:
            for driver_root in (fk_joints[0], ik_joints[0]):
                if not cmds.listConnections(driver_root + ".visibility",
                                            source=True, destination=False):
                    cmds.setAttr(driver_root + ".visibility", 0)

        # ---------------------------------------------------------------
        # 6. Enganche al padre de la cadena de bind (clavicula, cadera...)
        # ---------------------------------------------------------------
        parents = cmds.listRelatives(bind[0], parent=True, fullPath=True)
        if parents:
            cmds.parentConstraint(parents[0], fk_offs[0], maintainOffset=True)
            print("[FK/IK] El control FK raiz sigue a {0}."
                  .format(_short(parents[0])))
        else:
            cmds.warning(
                "La cadena de bind no tiene padre: el control FK raiz se "
                "queda suelto en el mundo.")

        # Las cadenas driver las emparentas tu: el script no toca tu esqueleto.
        for driver, label in ((fk_joints[0], "FK"), (ik_joints[0], "IK")):
            driver_parent = cmds.listRelatives(driver, parent=True, fullPath=True)
            bind_parent = parents[0] if parents else None
            if (driver_parent or [None])[0] != bind_parent:
                cmds.warning(
                    "La cadena {0} no cuelga del mismo sitio que la de bind. "
                    "Asegurate de que las tres siguen al mismo padre o el "
                    "brazo se separara al mover el cuerpo.".format(label))

        # ---------------------------------------------------------------
        # 7. Bloqueo de atributos
        # ---------------------------------------------------------------
        if lock_attrs:
            for ctl in fk_ctls:
                _lock_hide(ctl, ["tx", "ty", "tz", "sx", "sy", "sz", "v"])
            _lock_hide(ik_ctl, ["sx", "sy", "sz", "v"])
            _lock_hide(pv_ctl, ["rx", "ry", "rz", "sx", "sy", "sz", "v"])
            _lock_hide(switch_ctl, ["tx", "ty", "tz", "rx", "ry", "rz",
                                    "sx", "sy", "sz", "v"])

        # ---------------------------------------------------------------
        # 8. Metadatos para el snap
        # ---------------------------------------------------------------
        data = {
            "bindJnts": [_short(j) for j in bind],
            "fkJnts": [_short(j) for j in fk_joints],
            "ikJnts": [_short(j) for j in ik_joints],
            "fkCtls": [_short(c) for c in fk_ctls],
            "ikCtl": _short(ik_ctl),
            "pvCtl": _short(pv_ctl),
            "ikHandle": _short(handle),
            "midIndex": mid_index,
            "pvDistance": pv_distance,
        }
        cmds.addAttr(switch_ctl, longName=META_ATTR, dataType="string")
        meta_plug = "{0}.{1}".format(switch_ctl, META_ATTR)
        cmds.setAttr(meta_plug, json.dumps(data), type="string")
        cmds.setAttr(meta_plug, lock=True, keyable=False, channelBox=False)

        cmds.select(switch_ctl)
        print("[FK/IK] Sistema '{0}' montado sobre {1} joints. "
              "Switch: {2}".format(limb, len(bind), _short(switch_ctl)))
        return data

    finally:
        cmds.undoInfo(closeChunk=True)


# =============================================================================
# SNAP FK <-> IK
# =============================================================================

def _resolve_switch(switch_ctl=None):
    if switch_ctl is None:
        selection = cmds.ls(selection=True) or []
        candidates = [s for s in selection
                      if cmds.objExists("{0}.{1}".format(s, META_ATTR))]
        if not candidates:
            raise RuntimeError(
                "Selecciona el control de switch (el que tiene el atributo "
                "{0}).".format(SWITCH_ATTR))
        switch_ctl = candidates[0]

    plug = "{0}.{1}".format(switch_ctl, META_ATTR)
    if not cmds.objExists(plug):
        raise RuntimeError(
            "{0} no es un control de switch de este sistema.".format(switch_ctl))
    return switch_ctl, json.loads(cmds.getAttr(plug))


def snap_to_fk(switch_ctl=None):
    """Pasa de IK a FK copiando la pose actual de la cadena IK."""
    cmds.undoInfo(openChunk=True)
    try:
        switch_ctl, data = _resolve_switch(switch_ctl)

        # Leemos TODAS las rotaciones antes de tocar nada: al rotar el
        # control del hombro cambiaria la lectura de los hijos.
        rotations = [cmds.xform(j, query=True, worldSpace=True, rotation=True)
                     for j in data["ikJnts"]]

        for ctl, rotation in zip(data["fkCtls"], rotations):
            cmds.xform(ctl, worldSpace=True, rotation=rotation)

        cmds.setAttr("{0}.{1}".format(switch_ctl, SWITCH_ATTR), 0)
        print("[FK/IK] Snap a FK completado.")
    finally:
        cmds.undoInfo(closeChunk=True)


def snap_to_ik(switch_ctl=None):
    """Pasa de FK a IK colocando el control IK y el pole vector."""
    cmds.undoInfo(openChunk=True)
    try:
        switch_ctl, data = _resolve_switch(switch_ctl)
        fk_joints = data["fkJnts"]

        end_pos = cmds.xform(fk_joints[-1], query=True, worldSpace=True,
                             translation=True)
        end_rot = cmds.xform(fk_joints[-1], query=True, worldSpace=True,
                             rotation=True)
        pv_pos = _pole_vector_position(fk_joints[0],
                                       fk_joints[data["midIndex"]],
                                       fk_joints[-1],
                                       data.get("pvDistance"))

        cmds.xform(data["ikCtl"], worldSpace=True, translation=end_pos)
        cmds.xform(data["ikCtl"], worldSpace=True, rotation=end_rot)
        cmds.xform(data["pvCtl"], worldSpace=True, translation=list(pv_pos))

        cmds.setAttr("{0}.{1}".format(switch_ctl, SWITCH_ATTR), 1)
        print("[FK/IK] Snap a IK completado.")
    finally:
        cmds.undoInfo(closeChunk=True)


# =============================================================================
# INTERFAZ
# =============================================================================

_WINDOW = "fkikControlsWindow"


def show_ui():
    if cmds.window(_WINDOW, exists=True):
        cmds.deleteUI(_WINDOW)

    cmds.window(_WINDOW, title="FK / IK Controls", width=340, sizeable=True)
    cmds.columnLayout(adjustableColumn=True, rowSpacing=6,
                      columnOffset=("both", 10))

    cmds.separator(height=8, style="none")
    cmds.text(label="Selecciona cualquiera de las tres cadenas\n"
                    "(bind, FK o IK) y pulsa Montar.", align="left")
    cmds.separator(height=8, style="in")

    name_field = cmds.textFieldGrp(label="Nombre  ", text="",
                                   annotation="Vacio = se deduce del primer joint",
                                   columnWidth2=(60, 240))
    size_field = cmds.floatFieldGrp(label="Tam. ctl  ", numberOfFields=1,
                                    value1=0.0,
                                    annotation="0 = 15% de la cadena",
                                    columnWidth2=(60, 80))
    pv_field = cmds.floatFieldGrp(label="Dist. PV  ", numberOfFields=1,
                                  value1=0.0, annotation="0 = media cadena",
                                  columnWidth2=(60, 80))
    lock_box = cmds.checkBox(label="Bloquear atributos de los controles",
                             value=True)
    hide_box = cmds.checkBox(label="Ocultar las cadenas FK e IK", value=True)

    cmds.separator(height=8, style="in")

    def _wrap(function):
        def inner(*_):
            try:
                function()
            except RuntimeError as error:
                cmds.confirmDialog(title="FK / IK Controls",
                                   message=str(error), button=["Vale"])
        return inner

    def _build():
        build_fkik(
            limb_name=cmds.textFieldGrp(name_field, query=True,
                                        text=True).strip() or None,
            ctl_size=cmds.floatFieldGrp(size_field, query=True,
                                        value1=True) or None,
            pv_distance=cmds.floatFieldGrp(pv_field, query=True,
                                           value1=True) or None,
            lock_attrs=cmds.checkBox(lock_box, query=True, value=True),
            hide_drivers=cmds.checkBox(hide_box, query=True, value=True))

    cmds.button(label="Montar sistema FK / IK", height=38,
                command=_wrap(_build))

    cmds.separator(height=10, style="in")
    cmds.text(label="Con el control de switch seleccionado:", align="left")
    cmds.rowLayout(numberOfColumns=2, columnWidth2=(160, 160),
                   columnAttach=[(1, "both", 2), (2, "both", 2)])
    cmds.button(label="Snap a FK", height=30, command=_wrap(snap_to_fk))
    cmds.button(label="Snap a IK", height=30, command=_wrap(snap_to_ik))
    cmds.setParent("..")
    cmds.separator(height=10, style="none")

    cmds.showWindow(_WINDOW)


# =============================================================================
# ARRANQUE
# =============================================================================
# Esta es la linea que abre la ventana al ejecutar el script.
show_ui()
```


### Generacion y emparentamiento de controladores

*Maya · Advanced*

Renombra la curva base, genera la jerarquia con su offset group, alinea con matchTransform, congela transformaciones y aplica el tipo de constraint elegido (Parent, Orient, Point o combinados). Ajusta nombres de atributos/convenciones a tu escena real antes de usarla.

```python
# ctrlSetupWin.py
# ---------------------------------------------------------------------------
# Herramienta modular de generacion y emparentamiento de controladores (UI)
# Proyecto: Rigging anatomico - Tyto alba
#
# NOTA: esta es una reconstruccion funcional basada en la descripcion de la
# memoria (no es una recuperacion byte-a-byte del archivo original). Replica
# el comportamiento documentado: renombra la curva base, genera la jerarquia
# con su offset group, alinea con matchTransform, congela transformaciones y
# aplica el tipo de constraint elegido (Parent, Orient, Point o combinados).
# Ajusta nombres de atributos/convenciones a tu escena real antes de usarla.
# ---------------------------------------------------------------------------

import maya.cmds as cmds

WINDOW_NAME = "ctrlSetupWin"
CONSTRAINT_TYPES = ["Parent", "Orient", "Point", "Parent + Point"]


def _offset_group_name(ctrl_name):
    return "{0}_grp".format(ctrl_name)


def build_controller_setup(curve, target_joint, ctrl_suffix="_ctrl",
                            constraint_type="Parent", maintain_offset=False):
    """
    Convierte una curva base en un controlador completo:
      1. Renombra la curva segun la convencion <joint>_ctrl
      2. Crea el grupo de compensacion (offset group) como padre
      3. Alinea el offset group con el joint diana (matchTransform)
      4. Congela transformaciones del controlador
      5. Aplica el constraint elegido entre el controlador y el joint

    curve         : nombre de la curva NURBS que sera el controlador
    target_joint  : joint sobre el que se va a montar el control
    ctrl_suffix   : sufijo de nomenclatura para el controlador
    constraint_type : "Parent" | "Orient" | "Point" | "Parent + Point"
    maintain_offset : si True, conserva el offset entre ctrl y joint
    """
    if not cmds.objExists(curve):
        cmds.error("No existe la curva: {0}".format(curve))
    if not cmds.objExists(target_joint):
        cmds.error("No existe el joint diana: {0}".format(target_joint))

    # 1) Renombrar curva base segun convencion del rig
    base_name = target_joint.replace("_jnt", "").replace("_c_jnt", "")
    ctrl_name = cmds.rename(curve, base_name + ctrl_suffix)

    # 2) Generar jerarquia con grupo de compensacion
    offset_grp = cmds.group(ctrl_name, name=_offset_group_name(ctrl_name))

    # 3) Alinear transformacion con el joint diana (posicion + rotacion)
    cmds.matchTransform(offset_grp, target_joint, position=True, rotation=True)

    # 4) Congelar transformaciones del controlador (deja el ctrl en estado limpio)
    cmds.makeIdentity(ctrl_name, apply=True, translate=True, rotate=True,
                       scale=True, normal=False)

    # 5) Aplicar el tipo de constraint deseado, manteniendo coherencia de ejes
    if constraint_type == "Parent":
        cmds.parentConstraint(ctrl_name, target_joint, maintainOffset=maintain_offset)
    elif constraint_type == "Orient":
        cmds.orientConstraint(ctrl_name, target_joint, maintainOffset=maintain_offset)
    elif constraint_type == "Point":
        cmds.pointConstraint(ctrl_name, target_joint, maintainOffset=maintain_offset)
    elif constraint_type == "Parent + Point":
        cmds.parentConstraint(ctrl_name, target_joint, maintainOffset=maintain_offset)
        cmds.pointConstraint(ctrl_name, target_joint, maintainOffset=maintain_offset)
    else:
        cmds.warning("Tipo de constraint no reconocido: {0}".format(constraint_type))

    return ctrl_name, offset_grp


def show_window():
    """UI minima: elegir curva, joint diana y tipo de constraint, y construir."""
    if cmds.window(WINDOW_NAME, exists=True):
        cmds.deleteUI(WINDOW_NAME)

    cmds.window(WINDOW_NAME, title="Control Setup", widthHeight=(320, 220))
    cmds.columnLayout(adjustableColumn=True, rowSpacing=8, columnAttach=("both", 12))

    cmds.text(label="Curva base (controlador):")
    curve_field = cmds.textFieldButtonGrp(
        buttonLabel="<<", buttonCommand=lambda: cmds.textFieldButtonGrp(
            curve_field, edit=True,
            text=(cmds.ls(selection=True) or [""])[0]))

    cmds.text(label="Joint diana:")
    joint_field = cmds.textFieldButtonGrp(
        buttonLabel="<<", buttonCommand=lambda: cmds.textFieldButtonGrp(
            joint_field, edit=True,
            text=(cmds.ls(selection=True) or [""])[0]))

    cmds.text(label="Tipo de constraint:")
    constraint_menu = cmds.optionMenu()
    for c in CONSTRAINT_TYPES:
        cmds.menuItem(label=c)

    def _on_build(*_):
        curve = cmds.textFieldButtonGrp(curve_field, query=True, text=True)
        joint = cmds.textFieldButtonGrp(joint_field, query=True, text=True)
        ctype = cmds.optionMenu(constraint_menu, query=True, value=True)
        ctrl, grp = build_controller_setup(curve, joint, constraint_type=ctype)
        cmds.inViewMessage(amg="Controlador creado: <hl>{0}</hl>".format(ctrl),
                            pos="midCenter", fade=True)

    cmds.button(label="Construir controlador", command=_on_build,
                backgroundColor=(0.35, 0.6, 0.35))

    cmds.showWindow(WINDOW_NAME)


if __name__ == "__main__":
    show_window()
```


### Diagnostico automatico del rig

*Maya · Advanced*

Detectar los dos errores reales que se encontraron y corrigieron durante el proyecto:
(a) nodos unitConversion con factor de conversion incorrecto, originados por atributos tipados como "double" en lugar de "doubleAngle" (confusion grados/radianes).
(b) grupos de correccion de pluma usando pointConstraint (solo posicion) en vez de parentConstraint (posicion + rotacion), lo que provoca desincronizacion entre el gizmo/visual y la rotacion real.                                                                                    Ademas incluye comprobaciones generales de higiene de rig: constraints duplicados, suma de pesos en switches FK/IK, y desalineacion de pivote entre un controlador y su joint diana. Ajusta nombres/convenciones a tu escena real antes de usarla.

```python
# rig_diagnostic.py
# ---------------------------------------------------------------------------
# Script de diagnostico automatico del rig (control de calidad)
# Proyecto: Rigging anatomico - Tyto alba
#
# NOTA: esta es una reconstruccion funcional basada en la descripcion de la
# memoria (no es una recuperacion byte-a-byte del archivo original). Replica
# las comprobaciones documentadas y esta pensada, en particular, para
# detectar los dos errores reales que se encontraron y corrigieron durante
# el proyecto:
#   (a) nodos unitConversion con factor de conversion incorrecto, originados
#       por atributos tipados como "double" en lugar de "doubleAngle"
#       (confusion grados/radianes)
#   (b) grupos de correccion de pluma usando pointConstraint (solo posicion)
#       en vez de parentConstraint (posicion + rotacion), lo que provoca
#       desincronizacion entre el gizmo/visual y la rotacion real
# Ademas incluye comprobaciones generales de higiene de rig: constraints
# duplicados, suma de pesos en switches FK/IK, y desalineacion de pivote
# entre un controlador y su joint diana. Ajusta nombres/convenciones a tu
# escena real antes de usarla.
# ---------------------------------------------------------------------------

import maya.cmds as cmds

# Tolerancia para comparaciones de punto flotante (posicion/pivote, pesos)
EPSILON = 1e-3

# Factor de conversion esperado grados->radianes para nodos unitConversion
# que provienen de un atributo correctamente tipado como doubleAngle.
DEGREES_TO_RADIANS = 0.017453292519943295


def check_duplicate_constraints():
    """
    (1) Constraints duplicados: mas de un constraint del mismo tipo
        actuando sobre el mismo nodo destino suele ser un resto de
        iteraciones anteriores del setup y genera conflictos de pesos.
    """
    issues = []
    constraint_types = ["parentConstraint", "orientConstraint",
                         "pointConstraint", "scaleConstraint"]
    for ctype in constraint_types:
        for node in cmds.ls(type=ctype) or []:
            targets = cmds.listConnections(node, type="transform",
                                            source=False, destination=True) or []
            for target in set(targets):
                same_type_on_target = [
                    n for n in (cmds.listConnections(target, type=ctype,
                                                       source=True,
                                                       destination=False) or [])
                ]
                if len(set(same_type_on_target)) > 1:
                    issues.append(
                        "{0}: {1} constraints '{2}' duplicados sobre este nodo"
                        .format(target, len(set(same_type_on_target)), ctype))
    return sorted(set(issues))


def check_attribute_angle_typing(nodes=None):
    """
    (2) Atributos "double" que deberian ser "doubleAngle": causa raiz del
        bug de unitConversion documentado en la memoria. Un atributo de
        rotacion/angulo tipado como double simple no aplica la conversion
        grados/radianes esperada por los nodos aguas abajo.
    """
    issues = []
    nodes = nodes or cmds.ls(type="transform")
    angle_keywords = ("rot", "angle", "twist", "bend")

    for node in nodes:
        user_attrs = cmds.listAttr(node, userDefined=True) or []
        for attr in user_attrs:
            if not any(k in attr.lower() for k in angle_keywords):
                continue
            full = "{0}.{1}".format(node, attr)
            if not cmds.objExists(full):
                continue
            attr_type = cmds.attributeQuery(attr, node=node, attributeType=True)
            if attr_type == "double":
                issues.append(
                    "{0}: atributo de angulo '{1}' tipado como 'double' "
                    "(deberia ser 'doubleAngle')".format(node, attr))
    return issues


def check_unit_conversion_factors():
    """
    (3) Nodos unitConversion con factor incorrecto: verifica que el
        conversionFactor de cada unitConversion conectado a un canal de
        rotacion sea el esperado (grados a radianes). Un factor de 1.0
        (heredado de un atributo mal tipado como double) es la firma del
        bug documentado en la memoria.
    """
    issues = []
    for node in cmds.ls(type="unitConversion") or []:
        factor = cmds.getAttr("{0}.conversionFactor".format(node))
        outputs = cmds.listConnections(node, source=False, destination=True,
                                        plugs=True) or []
        rotation_targets = [p for p in outputs if "rotate" in p.lower()]
        if not rotation_targets:
            continue
        if abs(factor - DEGREES_TO_RADIANS) > EPSILON and abs(factor - 1.0) < EPSILON:
            issues.append(
                "{0}: conversionFactor={1:.6f} (esperado ~{2:.6f}) sobre {3} "
                "-> probable atributo origen tipado como 'double'"
                .format(node, factor, DEGREES_TO_RADIANS, rotation_targets))
    return issues


def check_feather_correction_constraints(pattern="*_corr_grp"):
    """
    (4) Grupos de correccion de pluma con pointConstraint en vez de
        parentConstraint: el bug documentado provoca que el grupo de
        correccion siga la posicion del control pero no su rotacion,
        desincronizando el gizmo respecto al resultado visual real.
    """
    issues = []
    for grp in cmds.ls(pattern, type="transform") or []:
        has_point = bool(cmds.listConnections(grp, type="pointConstraint",
                                               source=True, destination=False))
        has_parent = bool(cmds.listConnections(grp, type="parentConstraint",
                                                source=True, destination=False))
        has_orient = bool(cmds.listConnections(grp, type="orientConstraint",
                                                source=True, destination=False))
        if has_point and not (has_parent or has_orient):
            issues.append(
                "{0}: usa pointConstraint sin parent/orientConstraint "
                "-> no hereda rotacion (bug de correccion de pluma)".format(grp))
    return issues


def check_fkik_switch_weights(pattern="*_ikfk_blend*"):
    """
    (5) Switches FK/IK: la suma de pesos de los constraints implicados en
        el blend deberia ser 1.0 en todo momento; una suma distinta indica
        un blend mal cableado (channels sueltos, reverse node faltante, etc).
    """
    issues = []
    for node in cmds.ls(pattern) or []:
        weight_attrs = [a for a in (cmds.listAttr(node, keyable=True) or [])
                         if "weight" in a.lower()]
        if len(weight_attrs) < 2:
            continue
        total = 0.0
        for attr in weight_attrs:
            full = "{0}.{1}".format(node, attr)
            if cmds.objExists(full):
                total += cmds.getAttr(full)
        if abs(total - 1.0) > EPSILON:
            issues.append(
                "{0}: suma de pesos FK/IK = {1:.3f} (esperado 1.0)"
                .format(node, total))
    return issues


def check_controller_pivot_alignment(ctrl_pattern="*_ctrl", tolerance=0.01):
    """
    (6) Desalineacion de pivote: compara la posicion del pivote de cada
        controlador con la de su joint diana (si existe uno con el mismo
        prefijo de nombre) para detectar offsets accidentales introducidos
        durante el modelado de la curva o el agrupado.
    """
    issues = []
    for ctrl in cmds.ls(ctrl_pattern, type="transform") or []:
        base_name = ctrl.replace("_ctrl", "")
        candidate_joint = base_name + "_jnt"
        if not cmds.objExists(candidate_joint):
            continue
        ctrl_pos = cmds.xform(ctrl, query=True, worldSpace=True,
                               rotatePivot=True)
        joint_pos = cmds.xform(candidate_joint, query=True, worldSpace=True,
                                translation=True)
        dist = sum((c - j) ** 2 for c, j in zip(ctrl_pos, joint_pos)) ** 0.5
        if dist > tolerance:
            issues.append(
                "{0}: pivote desalineado respecto a {1} (distancia={2:.4f})"
                .format(ctrl, candidate_joint, dist))
    return issues


def run_full_diagnostic():
    """Ejecuta todas las comprobaciones y devuelve/imprime un reporte agrupado."""
    report = {
        "Constraints duplicados": check_duplicate_constraints(),
        "Atributos double vs doubleAngle": check_attribute_angle_typing(),
        "Factores de unitConversion": check_unit_conversion_factors(),
        "Correccion de plumas (point vs parentConstraint)":
            check_feather_correction_constraints(),
        "Suma de pesos FK/IK": check_fkik_switch_weights(),
        "Alineacion de pivotes ctrl/joint": check_controller_pivot_alignment(),
    }

    total_issues = sum(len(v) for v in report.values())
    print("=" * 70)
    print("DIAGNOSTICO DEL RIG - {0} incidencia(s) encontrada(s)".format(total_issues))
    print("=" * 70)
    for section, issues in report.items():
        print("\n[{0}] ({1})".format(section, len(issues)))
        if not issues:
            print("  OK - sin incidencias")
        else:
            for issue in issues:
                print("  - {0}".format(issue))

    if total_issues == 0:
        cmds.inViewMessage(amg="Diagnostico: <hl>sin incidencias</hl>",
                            pos="midCenter", fade=True)
    else:
        cmds.inViewMessage(
            amg="Diagnostico: <hl>{0}</hl> incidencia(s) - revisar Script Editor"
            .format(total_issues), pos="midCenter", fade=True)

    return report


if __name__ == "__main__":
    run_full_diagnostic()
```

