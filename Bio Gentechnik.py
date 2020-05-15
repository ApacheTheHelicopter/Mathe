# Genvariationen mit Generationen ausrechnen

# Parentalgeneration

# Strings nehmen und miteinander randomizen?
# So, dass man dann alle Kombinationen hat
# Übelst unnötig eigentlich

# -- 1. Objekt

    # 1. Allel
allel1 = " Hoher Ertrag "

    # 2. Allel
allel2 = " Niedriger Ertrag "

# -- 2. Objekt

    # 3. Allel
allel3 = " lange Vegetationszeit "

    # 4. Allel
allel4 = " kurze Vegetationszeit "

# randomizer

# ich hab irgendwie das Gefühl, dass das nicht die effizienteste Methode ist
# Da kann man doch bestimmmt ne function von machen

rand11 = (allel1+allel1)
print(rand11)
print()

# stack

rand12 = (allel1+allel2)
print(rand12)
print()
rand13 = (allel1+allel3)
print(rand13)
print()
"""
rand21 = (allel2+allel1)
print(rand21)
print()
# /stack
"""


rand22 = (allel2+allel2)
print(rand22)
print()

# stack

rand23 = (allel2+allel3)
print(rand23)
print()
"""
rand31 = (allel3+allel1)
print(rand31)
print()

rand32 = (allel3+allel2)
print(rand32)
print()
# /stack
"""


rand33 = (allel3+allel3)
print(rand33)
print()

# /randomizer

# Output hat jetzt mehrere doppelte
# 3 doppelte wegen 11 22 33

# 1 doppelter pro stack
    # Also
        # 12
        # 21

        # 13
        # 31

        # 23
        # 32