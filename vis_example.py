import oxidd

mgr = oxidd.bdd.BDDManager(1024, 1024, 1)

# Variables
x = mgr.new_var()
y = mgr.new_var()
z = mgr.new_var()
w = mgr.new_var()

# Function
f = (x & y) | (x & w) | (~z & w)

# Visualize
mgr.visualize([(f, "f")], [(x, "x"), (y, "y"), (z, "z"), (w, "w")])
mgr.dump_dddmp_file("test.dddmmp", [(f, "f")], [(x, "x"), (y, "y"), (z, "z"), (w, "w")])


# Create a manager for up to 100,000,000 nodes with an apply cache for
# 1,000,000 entries and 1 worker thread
manager = oxidd.bdd.BDDManager(100_000_000, 1_000_000, 1)

# Add variables to the bdd
x = [manager.new_var() for i in range(6)]

# These three are the same
# assert (x[0] & x[1]).satisfiable()
# assert (x[0].__and__(x[1])).satisfiable()
# x[0] & x[1]
(x[0] & x[1]).eval([(x[0], True), (x[1], False)])

# Get the BDD
manager.dump_all_dot_file("dump")
# Put it in https://dreampuf.github.io/GraphvizOnline/


mgr_zdd = oxidd.zbdd.ZBDDManager(1024, 1024, 1)
singletons = [mgr_zdd.new_singleton() for _ in range(3)]
x0 = singletons[0].var_boolean_function()
x1 = singletons[1].var_boolean_function()
x2 = singletons[2].var_boolean_function()
f = x0.imp(x1 | x2)
mgr_zdd.visualize([(f, "f")], [(singletons[i], "x"+str(i)) for i in range(3)])


