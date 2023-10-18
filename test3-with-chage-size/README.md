> python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 2945941, bytes  
result.png = 1433280, bytes  


> python encrypt_stegotest.py   
you message:  Test text


> python compare_2images.py   
1.jpg - 1.png =  0.0
1.jpg - new.png =  0.19764235376052372


> python change_size.py   
$ python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 3015692, bytes  
result.png = 1433280, bytes  


> python compare_2images.py   
1.jpg - 1.png =  0.0  
1.jpg - new (result).png =  0.19764235376052372  


> python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 3015692, bytes  
result.png = 1808759, bytes  


> $ python encrypt_stegotest.py   
$   
нет вывода сообщения (не смог расшифровать после изменения (уменьшения) размера и возврату к исходному)


> python change_size.py   
(теперь увеличили и вернули к обратному размеру сторон corupt)$ python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 3032261, bytes  
result.png = 1433280, bytes  


ПРИ увеличении:  

> python encrypt_stegotest.py   
you message:  	z   


Некорректная расшифровка сообщения  


> $ python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 3032261, bytes  
result.png = 2150616, bytes  



После добавления линий в corupt в редакторе изображений текст получилось корректно расшифровать  


> python encrypt_stegotest.py   
you message:  Test text  


> python size_of_img.py   
1.jpg = 509631, bytes  
1.png = 1270493, bytes  
before.png = 1433280, bytes  
new.png = 1124811, bytes  
corupt.png = 2912856, bytes  
result.png = 1778164, bytes  


> python compare_2images.py   
1.jpg - 1.png =  0.0  
1.jpg - new (result).png =  2076.6991091884656


Контейнер с сообщением до:
![](https://raw.githubusercontent.com/unton3ton/citXXX-stego_with_bitreverse/main/test3-with-chage-size/before.png)

Голограмма с повреждением:
![](https://raw.githubusercontent.com/unton3ton/citXXX-stego_with_bitreverse/main/test3-with-chage-size/corupt.png)

Контейнер с сообщением после уменьщения до 1000х1000 (и возврату размеров к 1024х1024) голограммы:
![](https://raw.githubusercontent.com/unton3ton/citXXX-stego_with_bitreverse/main/test3-with-chage-size/result_%D0%BF%D1%80%D0%B8_%D1%83%D0%BC%D0%B5%D0%BD%D1%8C%D1%88%D0%B5%D0%BD%D0%B8%D0%B8_%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D0%B0_corupt_%D0%B8_%D0%B2%D0%BE%D0%B7%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D0%B8_%D0%BA_%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%BE%D0%BC%D1%83.png)

Контейнер с сообщением после увеличения до 1050х1050 (и возврату размеров к 1024х1024) голограммы:
![](https://raw.githubusercontent.com/unton3ton/citXXX-stego_with_bitreverse/main/test3-with-chage-size/result_%D0%BF%D1%80%D0%B8%20%D1%83%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B8.png)
