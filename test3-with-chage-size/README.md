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
