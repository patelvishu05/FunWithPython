#!/usr/bin/python3
import unittest
from Dinosaur import *
from Zone import *
from Park import *

class TestStringMethods(unittest.TestCase):

    def runTests(self):
        pokemonPark = Park("Pokemon Park")

        try:
            pokemonPark.loadZones("data/region.csv")
            pokemonPark.loadDinosaurs("data/pokemon.csv")

            print(pokemonPark)

            pokemonPark.relocate("Pikachu","ALO")
            pokemonPark.save("output/pokemon.csv")

            print(pokemonPark)

        except FileNotFoundError as e:
            print("File not found !!")

    def fileLines(self,fileName):
        file = open(fileName,"r")
        lines = file.read().splitlines()
        file.close()
        return lines

    def test(self):
        self.runTests()
        self.assertEqual(self.fileLines('expected/expected1.csv'),self.fileLines('output/pokemon.csv'))

if __name__ == '__main__':
    unittest.main()