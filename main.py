import math
import numpy as np
from numpy.core.numeric import NaN

def cylinder_area(r:float,h:float) -> float:
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
    try:
        if r > 0 and h > 0:
            return 2*math.pi*r*r + 2*math.pi*r*h
        else:
            return NaN
    except: # jeśli zostanie podany zły typ danych to funkcja zwróci NaN
        return NaN

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    array = np.array([]) # tworzenie pustego obiektu typu numpy.array
    try:
        if n >=0:
            for i in range(n):
                if i == 0:
                    array = np.append(array, np.array([0])) # do obiektu typu numpy.array dodajemy 0
                elif i == 1:
                    array = np.append(array, np.array([1])) # do obiektu typu numpy.array dodajemy 1
                else:
                    array = np.append(array, np.array([array[-1] + array[-2]])) # do obiektu typu numpy.array dodajemy sumę jego dwóch ostatnich elementów
            return array
        else:
            return None
    except:
        return None

def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    try:
        Minv = np.linalg.inv(M) #utworzenie macierzy odwrotnej, jeśli to możliwe
    except:
        Minv = NaN # jeśli utworzenie macierzy okaże się, że nie da się utworzyć macierzy
    Mt = np.transpose(M)
    Mdet = np.linalg.det(M)
    return Minv, Mt, Mdet

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """

    cust_matrix = np.zeros((m,n)) # tworzymy macierz o wymiarach m na n wypełnioną zerami, aby móc jej pola uzupełnić właściwymi wartościami
    for i in range(m):
        for j in range(n):
            if i > j:
                cust_matrix[i,j] = i 
            else:
                cust_matrix[i,j] = j
    return cust_matrix
