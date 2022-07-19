# Función 1. Creación de una población con alelos al azar

import scipy
        
def build_population(G, p):
    """Para la creación de la población se ingresan dos variables, 
        ```G```  es el número de individuos de la población, 
        donde cada individuo tiene dos cromosomas, que contienen alelo "A" o "a" y 
        ```p```  es la probabilidad o nivel de ocurrencia de expresión del alelo dominante
    """
    
    population = [] 
    """Se crea la lista vacía para generar y agregar los resultados de la función"""
    
    for i in range(G):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
     """evaluo alelo 2 y comparo con el nivel de ocurrencia del alelo
        de esta manera los pares de alelos de la población se formarán aleatoriamente"""
        population.append((allele1, allele2))
     """Se usa .ppend para agregar a la lista creada"""
    return population
     """return me regresa la lista creada"""

#Función 2. Conteo de pares de alelos.

def compute_frequencies(population):
    """ En esta función se cuentan las 
    frecuencias genotípicas obtenidas
    """
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

#Función 3. Reproducción de la población. (Creación de una nueva población)

def reproduce_population(population):
    """ Para la reproducción de la población se debe crear una nueva población 
        para cada individuo nuevo se cumplirá que:
        - Los padres se seleccionan aleatoriamente 
        - La desendecia recibe un cromosoma de cada uno de los padres.        
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
          #next()
        new_generation.append(offspring)
    return new_generation