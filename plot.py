import numpy as np
import matplotlib.pyplot as plt

vendas=np.random.randint(1000,3000,50)
meses = np.arange(1,51)

plt.plot(meses, vendas,color='blue', marker='o', linestyle='dashed')
plt.axis([0, 50, 0,max(vendas)+200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.show()