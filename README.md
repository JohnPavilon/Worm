# Virus informáticos y vida artificial

# 1. Introducción

En 1981 apareció el primer virus de computadora y la historia de este fenómeno
ha sido muy importante porque se ha convertido en toda una industria y además,
los mecanismos para “infectar” sistemas de cómputo tienen interés por sí mismo.
Y aunque hoy día el problema de los virus informáticos podríamos calificarlo de
menor, pues ya se conocen todos los posibles mecanismos de infección, no deja
de ser interesante verlo a través de la óptica de la vida artificial. De alguna
manera, finalmente, un virus informático es un organismo que se auto-replica. Y
aunque “vivan” dentro de la computadora, esto no elimina la posibilidad de
clasificarlos como una forma de vida.

Cuando un programador decide que su software cause algún problema en la
computadora, hablamos de malware, de programas dañinos en nuestra máquina.
Hay muchas maneras en que estos programas puedan ser ejecutados,
normalmente sin el consentimiento del usuario. A esto se le ha dado en llamar
virus informático por la analogía con los virus biológicos.

Cabe decir que la palabra “virus” hace referencia a lo venenoso. En términos
biológicos, una infección viral se pone en marcha por un virus inyectando su
información genética a las células del individuo que va a ser infectado. Al infectar
las células, éstas producen réplicas del virus y el individuo entonces enferma
cuando el número de estas réplicas sobrepasa la capacidad inmunológica del
cuerpo. Así pues, un virus de computadora es un programa en código nativo, en
código de máquina, que se copia a sí mismo (o bien hace una copia modificada de
sí mismo), en los programas ejecutables de la computadora. Cuando estos
programas infectados son ejecutados, el código viral se ejecuta y el virus se
replica más veces, en ocasiones infectando a más programas o bien a través de
mecanismos de transmisión de datos, por ejemplo, el correo electrónico.
La capacidad de un virus informático para infectar puede ser enorme y hacer su
labor de reproducción en el sector de arranque del disco duro (que implicaría
nuevas potenciales infecciones cada vez que se enciende la computadora), o bien,
en un manejador de dispositivos (device driver) e incluso, la consola de intérpretes
de comandos. Las formas de replicación de un virus informático son variadas y
muchas veces, muy ingeniosas.

Lo escrito en este documento ha sido extraido en su totalidad del libro "JUGANDO A SER DIOS Experimentos en vida artificial"
escrito por el Dr. Manuel López Michelone y publicado por la UNAM. Véase el "Capítulo VI – Virus informáticos y vida artificial"
redactado en el libro antiormente mencionado.

# 2. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Worm/ adjunto a su contenido. Además de lo anterior, deberá tener instalado las bibliotecas Numpy, Matplotlib y PyQt5, en caso de no tenerlos instalados consulte los siguientes enlaces: 
<br />
<div align="center">
    https://sites.google.com/site/clasesdesde0/python-plot (Instalación de Matplotlib y Numpy)
</div>
<br />
<div align="center">
    https://pythones.net/pyqt-instalacion-y-codigo-tutorial/ (Instalación de PyQt5)
</div>
<br />

Posteriormente, se ejecutará el archivo gusano.py localizado en Worm/, este archivo se puede ejecutar dentro de una terminal (esto se puede realizar utilizando el comando "python gusano.py", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "gusano.py" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Cabe resaltar que se trata de un programa sencillo, por lo que al momento de ejecutarse se verá los resultados de inmediato. Por último les dejo capturas de pantalla que ilustran mejor el proceso de ejecución de programa.

# Capturas de pantalla

<p align="center">
  Ejecutamos la consola de comandos (Presiona Win+r y escribimos el comando "cmd")
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/Gphm2V1R/imagen-2022-03-10-231011.png"</img>
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/Gh2874fr/imagen-2022-03-10-230633.png"</img>
</p>
<br />
<p align="center">
  Primeramente veremos que la consola se encuentra ubicada en el directorio raíz, escribimos "cd" seguido de la dirección de la carpeta en donde se encuentra ubicado el archivo "gusano.py".
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/7Ymc4WX0/imagen-2022-03-10-231331.png"</img>
</p>
<br />
<p align="center">
  Comprobamos que efectivamente está el archivo "gusano.py" con el comando "dir"
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/MHG7mdRJ/imagen-2022-03-10-231638.png"</img>
</p>
<br />
<p align="center">
  Escribimos el siguiente comando: "python gusano.py", con esto habremos ejecutado el programa cuya salida será imprimir en pantalla el código fuente del mismo.
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/rmZ0Mcd7/imagen-2022-03-10-231918.png"</img>
</p>
<br />
<br />
<p align="center">
  No sólo eso, además se replicó el programa creando nuevas carpetas en el directorio actual y guardando una copia del mismo en cada nueva carpeta. Podemos comprobar esto escribiendo nuevamente "dir".
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/1zn5w647/imagen-2022-03-10-232243.png"</img>
</p>
<br />
<br />
<p align="center">
  Si ingresamos a cualquiera de las carpetas, veremos que efectivamente se encuentra un nuevo archivo "gusano.py"; si se desea salir de la consola, escribe "exit". Hemos creado un programa autoreplicante.
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/nL8NSQ0P/imagen-2022-03-10-232525.png"</img>
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/Y0m1PjXd/imagen-2022-03-10-232733.png"</img>
</p>
<br />
<p align="center">
  <img src="https://i.postimg.cc/ZRvcGfnP/imagen-2022-03-10-232823.png"</img>
</p>

# Funcionamiento del programa

El programa emula el funcionamiento de un gusano informático en su forma más sencilla, en este caso sólo nos interesa la capacidad de autoreplicación del código
hacia otras localidades en memoria. Primeramente el programa almacena la dirección de ejecución además del nombre del archivo, posteriormente llama y utiliza la misma consola
de comandos del sistema operativo Windows para ejecutar los comandos "crear directorio" y "copiar archivo", siendo que se crea en este caso las carpetas "copiaX" donde X es el valor i del iterador presente en el programa para luego copiar el programa "gusano.py" en las carpetas creadas (si se preguntan el porque del nombre de los directorios, la respuesta es que no hay razón de ser, simplemente son nombres aleatorios dados para realizar pruebas).


# 4. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Worm/ junto a una somera descripción de los mismos:

Worm/

1. README.md: Es el archivo que está leyendo en este momento
2. gusano.py: Ejecuta el programa autoreplicante

