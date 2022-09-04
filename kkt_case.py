from gurobipy import *

M_bound=1E3

# Pri = Model('Primal model')
# x1=Pri.addVar(lb=-M_bound,ub=0,name="x1")
# x2=Pri.addVar(lb=0,ub=M_bound,name="x2")
# x3=Pri.addVar(lb=0,ub=M_bound,name="x3")
# x4=Pri.addVar(lb=-M_bound,ub=M_bound,name="x4")
# Pri.addConstr(x1+x2-3*x3+x4>=5,'Con1')
# Pri.addConstr(2*x1+2*x3-x4<=4,'Con2')
# Pri.addConstr(x2+x3+x4==6,'Con3')
# Pri.setObjective(2*x1+3*x2-5*x3+x4,GRB.MINIMIZE)
# Pri.optimize()
# print(Pri.Objval)
#
# Dual=Model('Dual model')
# y1=Dual.addVar(lb=0,ub=M_bound,name="y1")
# y2=Dual.addVar(lb=-M_bound,ub=0,name="y2")
# y3=Dual.addVar(lb=-M_bound,ub=M_bound,name="y3")
# Dual.addConstr(y1+2*y2>=2,'Dual_Con1')
# Dual.addConstr(y1+y3<=3,'Dual_Con2')
# Dual.addConstr(-3*y1+2*y2+y3<=-5,'Dual_Con3')
# Dual.addConstr(y1-y2+y3==1,'Dual_Con4')
# Dual.setObjective(5*y1+4*y2+6*y3,GRB.MAXIMIZE)
# Dual.optimize()
# print(Dual.Objval)

M=1E5
KKT=Model('KKT model')
x1=KKT.addVar(lb=-M_bound,ub=0,name="x1")
x2=KKT.addVar(lb=0,ub=M_bound,name="x2")
x3=KKT.addVar(lb=0,ub=M_bound,name="x3")
x4=KKT.addVar(lb=-M_bound,ub=M_bound,name="x4")

y1=KKT.addVar(lb=0,ub=M_bound,name="y1")
y2=KKT.addVar(lb=-M_bound,ub=0,name="y2")
y3=KKT.addVar(lb=-M_bound,ub=M_bound,name="y3")

u1=KKT.addVar(vtype=GRB.BINARY,name="u1")
u2=KKT.addVar(vtype=GRB.BINARY,name="u2")

u3=KKT.addVar(vtype=GRB.BINARY,name="u3")
u4=KKT.addVar(vtype=GRB.BINARY,name="u4")
u5=KKT.addVar(vtype=GRB.BINARY,name="u5")

KKT.addConstr(x1+x2-3*x3+x4>=5,'KKT_Con1')
KKT.addConstr(2*x1+2*x3-x4<=4,'KKT_Con2')
KKT.addConstr(x2+x3+x4==6,'KKT_Con3')

KKT.addConstr(y1<=M*u1,'Com_Pri11')
KKT.addConstr(x1+x2-3*x3+x4-5<=M*(1-u1),'Com_Pri12')
KKT.addConstr(y2>=-M*u2,'Com_Pri21')
KKT.addConstr(2*x1+2*x3-x4-4>=-M*(1-u2),'Com_Pri22')

KKT.addConstr(y1+2*y2>=2,'KKT_Dual1')
KKT.addConstr(y1+y3<=3,'KKT_Dual2')
KKT.addConstr(-3*y1+2*y2+y3<=-5,'KKT_Dual3')
KKT.addConstr(y1-y2+y3==1,'KKT_Dual4')

KKT.addConstr(x1>=-M*u3,'Com_Dual11')
KKT.addConstr(2-y1-2*y2>=-M*(1-u3),'Com_Dual12')
KKT.addConstr(x2<=M*u4,'Com_Dual21')
KKT.addConstr(3-y1-y3<=M*(1-u4),'Com_Dual22')
KKT.addConstr(x3<=M*u5,'Com_Dual31')
KKT.addConstr(-5+3*y1-2*y2-y3<=M*(1-u5),'Com_Dual32')

# KKT.setObjective(2*x1+3*x2-5*x3+x4)
KKT.setObjective(5*y1+4*y2+6*y3)

KKT.ModelSense=GRB.MAXIMIZE
# KKT.ModelSense=GRB.MINIMIZE
KKT.optimize()
print(KKT.Objval)