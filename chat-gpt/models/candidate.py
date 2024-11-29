from person import Person

class Candidate:
    def __init__(self, record: Person, experience, soft_skills, hard_skills, team_work, problem_solving):
        self.person_record = record
        self.experience = experience
        self.soft_skills = soft_skills
        self.hard_skills = hard_skills
        self.team_work = team_work
        self.problem_solving = problem_solving

    @property
    def competencies(self):
        return f'''
            experience: {self.experience}
            soft skills: {self.soft_skills}
            hard skills: {self.hard_skills}
            team work: {self.team_work}
            problem solving: {self.problem_solving}
        '''
    
    def score(self, competency):
        mapping = {
            'bad':     0,
            'regular':  0.5,
            'good':      0.75,
            'great':    1
        }

        return mapping.get(competency.lower(), 0)

    @property
    def competency_scores(self):
        return [
            self.score(self.experience),
            self.score(self.soft_skills),
            self.score(self.hard_skills),
            self.score(self.team_work),
            self.score(self.problem_solving),
        ]
    
    def __str__(self):
        return f'''
            {self.person_record}
            {self.competencies}
        '''