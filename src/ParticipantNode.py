class ParticipantNode:
    def __init__(self, name):
        self.name = name
        self.neighbors : list[ParticipantNode]= None
    def __repr__(self) -> str:
        return f"{self.name} : {','.join([n.name for n in self.neighbors])}"