# desafio_kanban

Mi nombre es Lucía Urquiola, soy Licenciada en Ingeniería Biológica con un perfil en Bioinformática. Descubrí esta oportunidad a través de la comunidad de MujeresIT, que compartió el anuncio, y estoy muy contenta de haber avanzado a esta siguiente etapa de selección. Actualmente, trabajo como docente de programación e informática en la UDELAR en un cargo part-time, y estoy interesada en unirme a su equipo para seguir aprendiendo y aplicando mis conocimientos en el desarrollo de sistemas de gestión empresarial.

En este repositorio se adjuntan cada una de las partes del desafío propuesto, siguiendo la siguiente estructura:

La primera sección del desafío corresponde a una investigación de **conceptos fundamentales** para el cargo. 
A continuación se muestran las preguntas planteadas enlazadas a la respuesta.

01.a - [En el ámbito de las aplicaciones de negocio, qué significan las siglas:  CRM, ERP, GRP, MRP, SCM. Qué resuelven estas aplicaciones, ejemplos de algunos con su alcance.
](docs/01-a.txt)

01.b - [En el ámbito del desarrollo de software, indique para qué se utilizan y/o a qué hacen referencia las siglas:  HTML, XML, CSV, JSON, YAML.](docs/01-b.txt)

01.c - [¿Qué son Web Services?  ¿En qué se diferencia una API REST de un SOAP Server?](docs/01-c.txt)

01.d - [A qué hace referencia el Patrón de Arquitectura de Diseño de Software conocido como Modelo Vista Controlador (MVC). ¿Cuál es su utilidad?](docs/01-d.txt)

La segunda sección del desafío corresponde a la creación de este repositorio siguiendo buenas prácticas en el desarrollo colaborativo.

La tercera sección del desafío se encuentra en la carpeta ["sql"](sql/). La misma contiene dos archivos pdf, uno con cada parte del desafío de consultas estructuradas.

La cuarta sección del desafío se encuentra en la carpeta ["python"](python/). La misma tiene una carpeta app, una carpeta models y data. 
La carpeta app y models fueron dadas en el desafío, la carpeta data se agregó para guardar ahí los CSV a partir del cual se ingresan los datos en el programa.
La carpeta models se modificó y se hizo para cada clase un archivo python donde se definen. Estas clases son funcionario, recibo_sueldo y detalle_recibo.
La clase recibo_sueldo esta relacionada tanto con la clase funcionario (a través de id_funcionario) y de detalle_recibo (a través de id_detalle).

Se creó un archivo main el cual despliega un menú de opciones, y el cual puede usarse para cargar datos en la base de datos referente a funcionarios, recibos y detalles a partir de CSVs, 
se puede actualizar la información de nombre y cargo de un funcionario a partir de su cédula de identidad, y se puede eliminar todos los recibos asociados a un funcionario a partir de su
cédula. 

Toda la funcionalidad se desarrollo en un archivo llamado utils.py. Allí se encuentran funciones para ingresar datos de cada una de las clases a partir de CSVs, los de actualizar, eliminar, y consultar datos de la base de datos.
