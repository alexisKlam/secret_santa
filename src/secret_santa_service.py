
from ParticipantNode import ParticipantNode


def generate_all_secret_santa( participants: list[str], couples : list[(str,str)] ) -> list[list[str]]  :
    
    validate(participants, couples)

    participant_nodes =init_participant_nodes(participants, couples)
    
    allPaths = []
    
    for participant_node in participant_nodes.values():
        # find first path
        # path = find_path(participant_node, [], len(participants))
        # if(len(path) == len(participants)):
        #     return path

        # find all paths
        find_all_paths(participant_node, [], len(participants), allPaths)
      
        
    return allPaths

def generate_single_secret_santa( participants: list[str], couples : list[(str,str)] ) -> str :
    
    validate(participants, couples)

    participant_nodes =init_participant_nodes(participants, couples)
    
    for participant_node in participant_nodes.values():
        path = find_path(participant_node, [], len(participants))
        if(len(path) == len(participants)):
            return path
        
    return []

def find_path(participant_node : ParticipantNode, path : list[str], totalParticipants : int ):
    currentPath = path+[participant_node.name]
    if(len(currentPath) == totalParticipants):
        if(path[0] in [n.name for n in participant_node.neighbors]):
            return currentPath
        else:
            return []
            
    for neighbor in [n for n in participant_node.neighbors if n.name not in path]:
       resultPath= find_path(neighbor, currentPath, totalParticipants)
       if(len(resultPath) == totalParticipants):
           return resultPath
      
    return currentPath


def find_all_paths(participant_node : ParticipantNode, path : list[str], totalParticipants : int, result : list[list[str]] ):
    currentPath = path+[participant_node.name]
    if(len(currentPath) == totalParticipants):
        if(path[0] in [n.name for n in participant_node.neighbors]):
            result.append(currentPath)
        else:
            return
            
    for neighbor in [n for n in participant_node.neighbors if n.name not in path]:
       find_all_paths(neighbor, currentPath, totalParticipants, result)
      
      
    


def init_participant_nodes(participants: list[str], couples: list[str,str]):
    participantNodes = {}
    
    for participant in participants:
        participantNodes[participant] = ParticipantNode(participant)
     
    
    for couple in couples:
        coupleValidNeighbors = [p for p in participantNodes.values() if p.name != couple[0] and p.name != couple[1]]
        participantNodes[couple[0]].neighbors =coupleValidNeighbors
        participantNodes[couple[1]].neighbors =coupleValidNeighbors

    for participantNode in participantNodes.values():
        if(participantNode.neighbors == None):
            participantNode.neighbors = [p for p in participantNodes.values() if p.name != participantNode.name]
    
    return participantNodes



def validate( participants: list[str], couples : list[(str,str)]) :
    # validate list of participants has no duplicate
    participants_set = set(participants)
    if len(participants_set) != len(participants):
        raise Exception("Duplicate participant")
    
    if(len(participants) ==0):
        raise Exception("No participants")
    
    # validate couples are in participants
    for couple in couples:
        if couple[0] not in participants_set or couple[1] not in participants_set:
            raise Exception("Couple not in participants")
    
    # validate couples are not the same person
    for couple in couples: 
        if couple[0] == couple[1]:
            raise Exception("Couple is the same person")
    
    # validate couples are not the same
    couples_set = set(couples)
    if len(couples_set) != len(couples):
        raise Exception("Duplicate couple")

    # validate couple has a unique participant
    for couple in couples:
        if couple[0] == couple[1]:
            raise Exception("Couple has a unique participant")
    
    # validate cannot be in two couples
    unique_couple_member = set()
    for couple in couples:
        if(couple[0] in unique_couple_member or couple[1] in unique_couple_member):
            raise Exception("Cannot be in two couples")
        unique_couple_member.add(couple[0])
        unique_couple_member.add(couple[1])
     


