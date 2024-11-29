from mcda.outranking.electre import *
from electre_config import *
from models.candidate import *

class Classifier:
    def __init__(self, candidate_list: list[Candidate]):
        self.candidate_list = candidate_list

    def classify(self):

        dataset = PerformanceTable(
            [candidato.competency_scores for candidato in self.candidate_list], scales=scales
        )

        electre_tri = ElectreTri(
            dataset, W, profiles, I, P, V, lambda_=0.7, categories=categories
        )

        return electre_tri.assign().data
