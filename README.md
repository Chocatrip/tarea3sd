# Tarea 3 Sistemas Distribuidos - Alejandro Diaz
Video : https://youtu.be/XNSfb9WFVxM

# Funcionamiento
1. Para buildear la imagen
```sh
sudo docker build -t hadoop .
```

2. Para correr el contenedor
```sh
sudo docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```

3. Luego ingresar al bash del contenedor
```sh
sudo docker exec -it hadoop bash
```

4. Despues, crear las carpetas necesarias de hadoop
```sh
hdfs dfs -mkdir /user
```
```sh
hdfs dfs -mkdir /user/hduser
```
```sh
hdfs dfs -mkdir input
```

5. Dar permisos al usurio hduser
```sh
sudo chown -R hduser .
```

6. Luego, ingresar los documentos procesador al input de hadoop
```sh
hdfs dfs -put ./examples/docs*/*.txt input
```

7. Despues ingresar a la carpeta examples y ejecutar el codigo de mapper reducer
```sh
cd examples
```
```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py
```

8. Para comprobar que se ejecuto el codigo
```sh
hdfs dfs -cat /user/hduser/output/*
```

9. Despues, copiar el archivo de output de hadoop hacia el contenedor local, con el nombre data.txt
```sh
hdfs dfs -copyToLocal output/part-00000 ./data.txt
```

10. Luego, dentro de la carpeta examples, probar el browser ejecutando el archivo browser.py y pasando de parametros las palabras separadas por espacios
```sh
sudo python3 browser.py
```
