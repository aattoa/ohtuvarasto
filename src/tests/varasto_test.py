import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(0)
        self.varasto = Varasto(0, -1)
        self.varasto = Varasto(10, -1)
        self.varasto = Varasto(10, 1)
        self.varasto = Varasto(10, 11)
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(0)
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(0)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        self.varasto.lisaa_varastoon(1000000)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
        self.varasto.lisaa_varastoon(1)
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)
        saatu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(saatu_maara, 0)
        saatu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu_maara, 6)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        self.varasto.ota_varastosta(-1)
        self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
