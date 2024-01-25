# на базі програми з однією функцією пишу її виклик різними способами.
# 1)
# import some_function


# some_function.some_function("alex")

# 2)
# from some_function import some_function


# some_function("alex")

# 3)
# from some_function import some_function as sf


# sf("alex")


# 4)
# import some_function as sf


# sf.some_function("alex")

# 5)
from some_function import *


some_function("alex")
