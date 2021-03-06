from exercise1 import *
from exercise2 import *


floor0 = COLOR(COLORE1)((PROD([floor(40.1,21.4),Q(1.2)])))
floor1 = COLOR(COLORE2)(T([1,2,3])([0.6,0.6,1.2])(PROD([floor(38.9,20.2),Q(1.2)])))
floor2 = COLOR(COLORE3)(T([1,2,3])([1.2,1.2,2.4])(PROD([floor(37.7,19),Q(1.2)])))
floor3 = COLOR(COLORE4)(T([1,2,3])([1.8,1.8,3.6])(PROD([floor(36.5,17.8),Q(1.2)])))

steps_t=S([3])([0.8])(STRUCT([floor0,floor1,floor2,floor3]))

circle = MAP(sphere1)(domain(18))
columns1 = STRUCT([COLOR(COLORE3)(T([1,2])([0.4,3.4])(PROD([circle,Q(11.3)])))])

columns_est = STRUCT(NN(13)([T(1)(2.8), columns1]))
columns_ovest = STRUCT(NN(1)([T(2)(14.2), columns_est]))

columns2 = STRUCT([COLOR(COLORE3)(T([1,2])([3.2,3.5])(PROD([circle,Q(11.3)])))])

columns_sud = STRUCT(NN(4)([T(2)(2.8), columns2]))
columns_nord = STRUCT(NN(1)([T(1)(33.7), columns_sud]))

floor4a=T([3])([3.7])(STRUCT([columns_est,columns_ovest,columns_sud,columns_nord]))

columns3 = STRUCT([COLOR(COLORE1)(T([1,2])([8.4,6.3])(PROD([circle,Q(11.3)])))])

internal_front_columns = STRUCT(NN(2)([T(2)(2.8), columns3]))
internal_back_columns = STRUCT(NN(1)([T(1)(24.2),internal_front_columns]))

floor4b= T([3])([3.7])(STRUCT([internal_front_columns,internal_back_columns]))

#walls

wall_est = (T([1,2])([7.4,5.8])(PROD([floor(26.2,1),Q(10.75)])))

wall_ovest = (T([1,2])([7.4,14.2])(PROD([floor(26.2,1),Q(10.75)])))

wall_nord = (T([1,2])([11.4,6.8])(PROD([floor(1,7.4),Q(10.75)])))

wall_sud1 = (T([1,2])([27.2,6.8])(PROD([floor(2.7,2.5),Q(10.75)])))

wall_sud2 = (T([1,2])([27.2,11.7])(PROD([floor(2.7,2.5),Q(10.75)])))

floor4c=COLOR(COLORE1)(T([3])([3.7])(STRUCT([wall_est,wall_ovest,wall_nord,wall_sud1,wall_sud2])))



#capitelli

capitello = COLOR(COLORE4)((T([1,2,3])([-0.6,2.4,1.2])(PROD([floor(2,2),Q(0.6)]))))

cap_est = STRUCT(NN(13)([T(1)(2.8), capitello] ))
cap_ovest = STRUCT(NN(1)([T(2)(14.2), cap_est] ))

capitello2 = COLOR(COLORE4)((T([1,2,3])([2.2,2.5,1.2])(PROD([floor(2,2),Q(0.6)]))))

cap_sud = STRUCT(NN(4)([T([2])(2.8), capitello2]))
cap_nord = STRUCT(NN(1)([T(1)(33.7), cap_sud]))

capitello3 = COLOR(COLORE3)((T([1,2,3])([7.4,2.5,1.2])(PROD([floor(2,2),Q(0.6)]))))

cap_isud = STRUCT(NN(4)([T([2])(2.8), capitello3]))
cap_inord = STRUCT(NN(1)([T(1)(24.2), cap_isud]))

floor5=T([3])([13.2])(STRUCT([cap_est,cap_ovest,cap_sud,cap_nord,cap_isud,cap_inord]))


#travi

trave_est = COLOR(COLORE3)((T([1,2,3])([2.6,2.8,1.5])(PROD([floor(34.2,1.2),Q(1.2)]))))
trave_ovest = STRUCT(NN(1)([T([2])(14.2),trave_est]))

trave_sud=COLOR(COLORE3)((T([1,2,3])([2.6,2.8,1.5])(PROD([floor(1.2,15.4),Q(1.2)]))))
trave_sud1=COLOR(COLORE1)((T([1,2,3])([2.6,2.8,1.5])(PROD([floor(1.2,15.4),Q(1.2)]))))

trave_est1 =COLOR(COLORE4)((T([1,2,3])([3.8,2.8,2.7])(PROD([floor(4.2,1.2),Q(1.2)]))))
trave_ovest1 = STRUCT(NN(1)([T([2])(14.2),trave_est1]))

trave_nord =STRUCT(NN(1)([T([1])(33.6),trave_sud]))
trave_nord1=STRUCT(NN(1)([T([1])(33.6),trave_sud1]))

trave_interna1=COLOR(COLORE4)((T([1,2,3])([7.8,5.8,1.5])(PROD([floor(1.2,9.4),Q(1.2)]))))
trave_interna2=STRUCT(NN(1)([T([1])(24.2),trave_interna1]))

trave_interna3 = COLOR(COLORE4)((T([1,2,3])([27.2,6.8,0.9])(PROD([floor(2.7,7.4),Q(1.2)]))))

floor6=T([3])([13.5])(STRUCT([trave_est,trave_ovest,trave_est1,trave_ovest1,trave_sud,trave_nord,trave_interna1,trave_interna2,trave_interna3]))

floor7=T([3])([14.7])(STRUCT([trave_sud1,trave_nord1]))


#triangolo
triangolo_s=(T([1,2,3])([1.9,1.2,2.6])(PROD([triangle_generator(17.3,3),Q(1.2)])))
triangolo_south=R([1,3])(PI*3/2)(R([1,2])(PI/2)(triangolo_s))
north = STRUCT(NN(1)([T([1])(33.6), triangolo_south]))


floor8=COLOR(COLORE4)(T([3])([16.2])(STRUCT([triangolo_south,north])))


VIEW(S([1,2,3])([1.8,1.8,1.8])(STRUCT([steps_t,floor4a,floor4b,floor4c,floor5,floor6,floor7,floor8])))
