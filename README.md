# Tarea 3 Sistemas Distribuidos - Alejandro Diaz
Video : [a link] (https://youtu.be/XNSfb9WFVxM)

##Funcionamiento
Para buildear la imagen
```sh
sudo docker build -t hadoop .
```

Para correr el contenedor
```sh
sudo docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```

Luego ingresar al bash del contenedor
```sh
sudo docker exec -it hadoop bash
```

Despues, crear las carpetas necesarias de hadoop
```sh
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input
```

Dar permisos al usurio hduser
```sh
sudo chown -R hduser .
```

Luego, ingresar los documentos procesador al input de hadoop
```sh
hdfs dfs -put ./examples/docs*/*.txt input
```

Despues ingresar a la carpeta examples y ejecutar el codigo de mapper reducer
```sh
cd examples
```
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py
```

Para comprobar que se ejecuto el codigo
```sh
hdfs dfs -cat /user/hduser/output/*
```

Despues, copiar el archivo de output de hadoop hacia el contenedor local, con el nombre data.txt
```sh
hdfs dfs -copyToLocal output/part-00000 ./data.txt
```

Luego, dentro de la carpeta examples, probar el browser ejecutando el archivo browser.py y pasando de parametros las palabras separadas por espacios
```sh
sudo python3 browser.py
```
