import unittest
from  secret_santa_service import *
class Test_Secret_Santa_Service(unittest.TestCase):

    def test_should_throw_if_duplicate_participant(self):
        self.assertRaises(Exception,generate_single_secret_santa, ["a","a"], [])
    
    def test_should_throw_if_duplicate_couple(self):
        self.assertRaises(Exception,generate_single_secret_santa, ["a","b"], [("a","b"),("a","b")])

    def test_should_throw_if_couple_is_the_same_person(self):
        self.assertRaises(Exception,generate_single_secret_santa,["a","b"], [("a","a")])


    def test_should_throw_if_couple_not_in_participants(self):
        self.assertRaises(Exception,generate_single_secret_santa, ["a","b"], [("a","c")])


    def test_should_throw_if_no_participant(self):
        self.assertRaises(Exception,generate_single_secret_santa, [], [])

    def test_should_generate(self):
        generate_single_secret_santa( ["a","b","c","d"], [("a","c")])

    def test_should_generate_with_no_couple(self):
        solution = generate_single_secret_santa( ["a","b","c"], [])
        self.assertTrue(Test_Secret_Santa_Service.__check_if_solution_valid(solution, ["a","b","c"], []))
    
    def test_should_generate_no_result(self):
        solution =  generate_single_secret_santa( ["a","b","c"], [("a","b")])
        self.assertEqual(len(solution),0)
    
    def test_should_generate_bis(self):
        solution = generate_single_secret_santa( ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"], [("Florent", "Jessica"), ("Coline", "Emilien")])
        self.assertTrue(Test_Secret_Santa_Service.__check_if_solution_valid(solution, ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"], [("Florent", "Jessica"), ("Coline", "Emilien")]))
    
    
    def test_should_not_validate_solution(self):
        self.assertFalse(Test_Secret_Santa_Service.__check_if_solution_valid(["a","b","c"], ["a","b","c"], [("a","b")]))

    def __check_if_solution_valid(solution :list[str], participants:list[str], couples:list[(str,str)]):
        if(len(solution) != len(participants)):
            return False
        for participant in participants:
            if(participant not in solution):
                return False
        constraints = {}
        for couple in couples:
            constraints[couple[0]] = couple[1]
            constraints[couple[1]] = couple[0]
        
        for i in range(len(solution)):
            if(solution[i] == constraints.get(solution[(i+1)%len(solution)])):
                return False
       
        return True
    


        
