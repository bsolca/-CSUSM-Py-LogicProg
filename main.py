from kanren import run, eq, membero, var, conde, Relation, facts

# [1] logic programming. It asks for 1 number, x, such that x == 5
print ("[1] equal:")
x = var()
run(1, x, eq(x, 5))
print (run(1, x, eq(x, 5)))

# Multiple variables and multiple goals can be used simultaneously
print ("\n [2] Multiple variables:")
z = var()
print(run(1, x, eq(x, z),
          eq(z, 3)))

# unification, an advanced form of pattern matching
print ("\n [3] unification:")
print (run(1, x, eq((1, 2), (1, x))))

# Member usage
print ("\n [1] equal:")
print(run(2, x, membero(x, (1, 2, 3)),  # x is a member of (1, 2, 3)
          membero(x, (2, 3, 4))))  # x is a member of (2, 3, 4)

# Logic variable
z = var('test')
print (z)

# Multiple variable at one
a, b, c = var('a'), var('b'), var('c')
print(a)
print(b)
print(c)

# Data store and relationship
parent = Relation()
facts(parent, ("Homer", "Bart"),
      ("Homer", "Lisa"),
      ("Abe", "Homer"))

print(run(1, x, parent(x, "Bart")))

print(run(2, x, parent("Homer", x)))

# Intermediate variables for more complex queries
y = var()
print(run(1, x, parent(x, y),
          parent(y, 'Bart')))


# Separate relationship. conde() is a goal constructor for logic AND and OR
def grandparent(x, z):
    y = var()
    return conde((parent(x, y), parent(y, z)))


print(run(1, x, grandparent(x, 'Bart')))
