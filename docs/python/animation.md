# Animation


## Animation


### Insertar keyframe de posición en el frame actual

*Blender · Basic*

```python
import bpy
obj = bpy.context.active_object
obj.keyframe_insert(data_path="location",
                    frame=bpy.context.scene.frame_current)
```


### Insertar keyframe en el frame actual

*Maya · Basic*

Sobre el objeto seleccionado.

```python
import maya.cmds as cmds
cmds.setKeyframe()
```


### Mirror de animación

*Maya · Advanced*

Busca controladores por convencion de nombre (*_l_ctrl -> *_r_ctrl), lee los atributos animables (keyables) de cada controlador izquierdo y replica sus curvas de animacion al lado derecho equivalente, invirtiendo los canales que lo requieren. Incluye tambien la variante restringida al rango de tiempo visible en la Time Slider. Ajusta nombres/convenciones y los canales a invertir a tu escena real antes de usarla.

```python
# mirror_animation_scripts.py
# ---------------------------------------------------------------------------
# Herramientas de espejado de animacion (izquierda -> derecha)
# Proyecto: Rigging anatomico - Tyto alba
#
# NOTA: esta es una reconstruccion funcional basada en la descripcion de la
# memoria (no es una recuperacion byte-a-byte del archivo original). Replica
# el comportamiento documentado: busca controladores por convencion de
# nombre (*_l_ctrl -> *_r_ctrl), lee los atributos animables (keyables) de
# cada controlador izquierdo y replica sus curvas de animacion al lado
# derecho equivalente, invirtiendo los canales que lo requieren. Incluye
# tambien la variante restringida al rango de tiempo visible en la Time
# Slider. Ajusta nombres/convenciones y los canales a invertir a tu escena
# real antes de usarla.
# ---------------------------------------------------------------------------

import maya.cmds as cmds

LEFT_TOKEN = "_l_"
RIGHT_TOKEN = "_r_"

# Canales que tipicamente deben invertirse al espejar de un lado a otro
# (depende de como este orientado cada joint/ctrl; ajustar segun el rig).
MIRROR_INVERT_ATTRS = ["translateX", "rotateY", "rotateZ"]


def find_left_controllers(pattern="*_l_ctrl"):
    """Devuelve todos los controladores del lado izquierdo segun convencion."""
    return cmds.ls(pattern, type="transform") or []


def get_mirror_name(left_name):
    """Convierte el nombre de un controlador izquierdo en su par derecho."""
    if LEFT_TOKEN not in left_name:
        cmds.warning("El nombre no sigue la convencion *_l_*: {0}".format(left_name))
        return None
    return left_name.replace(LEFT_TOKEN, RIGHT_TOKEN)


def _keyable_animated_attrs(node):
    """Lista los atributos keyable de 'node' que tienen curvas de animacion."""
    attrs = cmds.listAttr(node, keyable=True) or []
    animated = []
    for attr in attrs:
        full = "{0}.{1}".format(node, attr)
        if cmds.objExists(full) and cmds.listConnections(full, type="animCurve"):
            animated.append(attr)
    return animated


def mirror_controller_animation(left_ctrl, start_frame=None, end_frame=None,
                                 invert_attrs=None):
    """
    Copia la animacion de un controlador izquierdo a su equivalente derecho.

      1. Resuelve el nombre del controlador derecho por convencion
      2. Detecta los atributos animados (con curvas) del controlador izquierdo
      3. Copia cada curva al controlador derecho (cutCopyPaste)
      4. Invierte los canales indicados en invert_attrs (por defecto los
         definidos en MIRROR_INVERT_ATTRS) multiplicando sus valores por -1
      5. Si se especifica start_frame/end_frame, recorta la copia a ese
         rango (pensado para usarse con el rango visible de la Time Slider)

    left_ctrl     : nombre del controlador origen (lado izquierdo)
    start_frame   : primer frame a copiar (None = toda la curva)
    end_frame     : ultimo frame a copiar (None = toda la curva)
    invert_attrs  : lista de atributos a invertir; None usa MIRROR_INVERT_ATTRS
    """
    if not cmds.objExists(left_ctrl):
        cmds.error("No existe el controlador: {0}".format(left_ctrl))

    right_ctrl = get_mirror_name(left_ctrl)
    if not right_ctrl or not cmds.objExists(right_ctrl):
        cmds.error("No existe el controlador espejo: {0}".format(right_ctrl))

    if invert_attrs is None:
        invert_attrs = MIRROR_INVERT_ATTRS

    animated_attrs = _keyable_animated_attrs(left_ctrl)
    if not animated_attrs:
        cmds.warning("Sin atributos animados en: {0}".format(left_ctrl))
        return right_ctrl, []

    copied = []
    for attr in animated_attrs:
        src = "{0}.{1}".format(left_ctrl, attr)
        dst = "{0}.{1}".format(right_ctrl, attr)
        if not cmds.objExists(dst):
            continue

        # 2-3) Copiar la curva de animacion del canal (rango completo o acotado)
        if start_frame is not None and end_frame is not None:
            cmds.copyKey(src, time=(start_frame, end_frame))
            cmds.pasteKey(dst, time=(start_frame, end_frame), option="replace")
        else:
            cmds.copyKey(src)
            cmds.pasteKey(dst, option="replace")

        # 4) Invertir el canal si corresponde a la lista de inversion
        if attr in invert_attrs:
            cmds.scaleKey(dst, valueScale=-1, valuePivot=0)

        copied.append(attr)

    return right_ctrl, copied


def mirror_all(pattern="*_l_ctrl", use_time_slider_range=False,
                invert_attrs=None):
    """
    Recorre todos los controladores izquierdos que cumplan 'pattern' y
    espeja su animacion al lado derecho.

    use_time_slider_range : si True, limita la copia al rango actualmente
                             visible en la Time Slider (playbackOptions);
                             si False, copia el rango completo de cada curva.
    """
    start_frame = end_frame = None
    if use_time_slider_range:
        start_frame = cmds.playbackOptions(query=True, minTime=True)
        end_frame = cmds.playbackOptions(query=True, maxTime=True)

    results = {}
    for left_ctrl in find_left_controllers(pattern):
        try:
            right_ctrl, attrs = mirror_controller_animation(
                left_ctrl, start_frame=start_frame, end_frame=end_frame,
                invert_attrs=invert_attrs)
            results[left_ctrl] = (right_ctrl, attrs)
        except RuntimeError as exc:
            cmds.warning("Fallo al espejar {0}: {1}".format(left_ctrl, exc))

    cmds.inViewMessage(
        amg="Animacion espejada en <hl>{0}</hl> controladores".format(len(results)),
        pos="midCenter", fade=True)
    return results


if __name__ == "__main__":
    # Ejemplo: espejar solo dentro del rango visible en la Time Slider
    mirror_all(use_time_slider_range=True)
```

