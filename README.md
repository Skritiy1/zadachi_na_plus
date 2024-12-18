1. Пояснение к задаче accuracy (классификации)
   рассмотрим пример: массив с ноликами [1, 3, 5], массив с крестиками [2, 4, 10]
   тогда на числовой прямой числа c подсчетом accuracy будут выглядить так:
   
   <img width="541" alt="image" src="https://github.com/user-attachments/assets/aca11e1d-690a-4094-b296-088369b8f2cc">

   соответсвенно маскимальное accuracy = 2/3 (при этом мы берем максимально возможное accuracy, то есть сначала считаем слева нолики, справа крестики и потом наоборот), то есть можем взять любую точку с accuracy = 2/3: возьмем точку между 1 и 2, тогда result = (1+2)/2 = 1,5

   input: [1, 3, 5], [2, 4, 10]

   output: 1,5

   <img width="662" alt="image" src="https://github.com/user-attachments/assets/90ac2cb0-b48c-4377-bd19-56456e209c10">

   
2. Пояснение к задаче regress
   рассмотрим пример: координаты ноликов [[2, 3], [1, 5], [5, 3]], координаты крестиков [[7, 8], [0,0], [-2, -3]], главная точка - [5, 5], коэф k = 3

   Графически это будет выгляить так:
   <img width="1393" alt="image" src="https://github.com/user-attachments/assets/b85b3e3b-0af2-44ae-b141-ba751a1de266">

   Получается, что нам нужно найти 3 ближайших точки к точке [5, 5], это будут точки [2, 3], [5, 3], [7, 8], из которых две точки относятся к ноликам и одна к крестикам, то есть наша главная точка принадлежит к крестикам

   input:
   
   3

   [[2, 3], [1, 5], [5, 3]]

   [[7, 8], [0,0], [-2, -3]]
   
   [5, 5]
   
   output:

   Точка [5, 5] относится к ноликам, кол-во ближайших ноликов 2, кол-во ближайших крестиков 1

<img width="750" alt="image" src="https://github.com/user-attachments/assets/b77af9ee-49d5-4f7b-88d2-ae5102251d67">

3. Пояснение к задаче claster
   на вход идет 2 массива точек, определим прямую сначала для первого, потом для второго используя метод наименьших квадратов
   Найдем коэф K
<img width="629" alt="image" src="https://github.com/user-attachments/assets/9033ee20-c14a-4237-8244-34583c6c2fc8" />

Найдем коэф b

<img width="956" alt="image" src="https://github.com/user-attachments/assets/5c3dd00f-68c6-49ec-bbf1-3b071ae13634" />

Графически будет выглядить так
<img width="1457" alt="image" src="https://github.com/user-attachments/assets/deb27b39-95f1-4b88-94ca-bcf952043bff" />

формулы брались с сайта https://portal.tpu.ru/SHARED/m/MBB/uchebnaya_rabota/Model/Tab/Interp_app.pdf
