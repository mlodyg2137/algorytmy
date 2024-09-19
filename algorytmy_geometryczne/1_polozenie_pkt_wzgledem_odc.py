def orientation(A, B, P):
    # wzor = (Bx - Ax)*(Py - Ay) - (By - Ay)*(Px - Ax)
    cross_product = ((B[0] - A[0])*(P[1] - A[1]) - (B[1] - A[1])*(P[0] - A[0]))
    if cross_product > 0:
        print("lezy po lewej")
    elif cross_product < 0:
        print("lezy po prawej")
    else:
        print("lezy na")

A = (1, 1)
B = (4, 4)
P = (2, 3)

orientation(A, B, P)
