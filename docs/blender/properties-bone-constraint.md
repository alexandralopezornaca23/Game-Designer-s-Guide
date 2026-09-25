# Properties > Bone Constraint


| | Action | Shortcut / Location | Level | Notes |
|---|---|---|---|---|
| ⛓️ | **Bone Constraint: qué es y cómo se compara con Object Constraints** | *Panel Properties > Bone Constraint (icono de hueso con cadena, solo en Pose Mode)* | Intermediate | Aplica constraints al HUESO seleccionado en vez de a todo el Object; funciona igual que Properties > Object Constraints (misma cabecera con ojo/flecha/X/Influence, mismo concepto de Target/Owner Space) pero solo está disponible en Pose Mode. Comparte los mismos 27 constraints ya documentados en Object Constraints (Motion Tracking: 3, Transform: 11, Relationship: 8, todos idénticos) y añade 2 exclusivos de hueso dentro de la categoría Tracking: Inverse Kinematics y Spline IK. |
| 🦾 | **Add Bone Constraint > Tracking: Inverse Kinematics** | *Panel Properties > Bone Constraint > Add Bone Constraint > Tracking* | Advanced | Exclusivo de huesos. Convierte la cadena de huesos hasta cierta profundidad en una cadena de Inverse Kinematics: en vez de rotar cada hueso a mano (Forward Kinematics), se mueve un único hueso/objetivo final y el resto de la cadena se dobla automáticamente para alcanzarlo; es la base de cualquier rig de piernas o brazos. |
| ➰ | **Add Bone Constraint > Tracking: Spline IK** | *Panel Properties > Bone Constraint > Add Bone Constraint > Tracking* | Advanced | Exclusivo de huesos. En vez de apuntar a un único punto como el IK normal, hace que una cadena de huesos siga la forma completa de una curva (por ejemplo, para animar una cola, una serpiente o un tentáculo con huesos en vez de aplicar el modifier Curve directamente sobre la malla). |

