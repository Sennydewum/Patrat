import turtle
import Patrat


""""
- primul parametru -- gradele pentru desen
- parametrul 2 - valoarea initiala pentru r (nuanta de rosu pentru culoarea dormata in rgb)
- parametrul 3 - valoarea initiala pentru g (nuanta de verde pentru culoarea dormata in rgb)
- parametrul 4 - valoarea initiala pentru b (nuanta de albastru pentru culoarea dormata in rgb)
- parametrul 5 - valoarea cu care modificam valoarea lui r (sa ne incadram intre 0, 255 pentru 100 de pasi)
- parametrul 5 - valoarea cu care modificam valoarea lui g (sa ne incadram intre 0, 255 pentru 100 de pasi)
- parametrul 5 - valoarea cu care modificam valoarea lui b (sa ne incadram intre 0, 255 pentru 100 de pasi)





Exemplu

avem culoarea rgb - (100, 255, 0)
calculam rm gm si bm

rm
pentru ca avem r = 100 putem sa punem -1 ca sa ajungem la 0 in 100 de pasi
sau + 1 -- 200 in 100 de pasi

gm
-1 sau -2

bm 
+1 sau +2
"""

Patrat.forma(91,100,255,0,-1,-2,1)
