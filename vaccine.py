"""
Class Vaccine. Has properties of first_dose, second_dose and booter. Will be inherited by the Resident Class.
"""


class Vaccine:
    def __init__(self, first_dose, second_dose, booster):
        self.first_dose = first_dose
        self.second_dose = second_dose
        self.booster = booster

    def first_dose_given(self):
        return True

    def second_dose_given(self):
        return True

    def booster_dose_given(self):
        return True
