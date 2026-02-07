"""Check your arrows
You have a quiver of arrows, but some have been damaged. The quiver contains arrows with an optional range information (different types of targets are positioned at different ranges), so each item is an arrow.
You need to verify that you have some good ones left, in order to prepare for battle:

anyArrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
If an arrow in the quiver does not have a damaged status, it means it's new.

The expected result is a boolean, indicating whether you have any good arrows left.

Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

"""


import codewars_test as test
from solution import any_arrows

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(any_arrows([]), False, "Should handle empty quiver")
        test.assert_equals(any_arrows([{'range': 5, 'damaged': False}]), True, "Should handle quiver with undamaged arrows")
        test.assert_equals(any_arrows([{'range': 5, 'damaged': False},{'range': 15, 'damaged': True}]), True, "Should handle quiver with undamaged arrows")
        test.assert_equals(any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]), True, "Should handle quiver with undamaged arrows")
        test.assert_equals(any_arrows([{'range': 10, 'damaged': True}, {'damaged': True}]), False, "Should handle quiver with damaged arrows")


def any_arrows(arrows):
    for arrow in arrows:
        if arrow['damaged'] in arrows:
            return "New" #Danificada
        elif arrow['damaged']:
            return True #Boa
        else:
            return False

def any_arrows(arrows):
    return any(not i.get('dagamed', False) for i in arrows)