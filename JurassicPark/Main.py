#!/usr/bin/python3
from Dinosaur import *
from Zone import *
from Park import *

jurassicPark = Park("Jurassic Park")

try:
    jurassicPark.loadZones("data/zones.csv")
    jurassicPark.loadDinosaurs("data/dinos.csv")

    print(jurassicPark)


    jurassicPark.relocate("Blue","TY")
    jurassicPark.save("output/dinos.csv")

    print(jurassicPark)

except FileNotFoundError as e:
    print("File not found !!")
