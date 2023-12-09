import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        """Kortilta velotetaan hinta jos rahaa on"""
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        """Testitapaus: Kortilta ei veloteta jos raha ei riitä"""
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_kortille_ladataan_positiivinen_summa(self):
        """Testitapaus: Kortille ladataan positiivinen summa"""
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, 10)
        maksukortti_mock.lataa.assert_called_with(10)

    def test_kortille_ei_ladata_negatiivista_summaa(self):
        """Testitapaus: Kortille ei ladata negatiivista summaa"""
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, -10)
        maksukortti_mock.lataa.assert_not_called()