import unittest
from component_manager import ComponentManager

class TestAdd(unittest.TestCase):

    def test_add_two_component(self):
        cm = ComponentManager()
        cm.add_component('pgm1')
        cm.add_component('pgm2')
        self.assertTrue(len(cm.dep_graph) == 2)


class TestMakeDependent(unittest.TestCase):
    def test_make_dependent(self):
        cm = ComponentManager()
        cm.add_component('pgm1')
        cm.add_component('pgm2')
        cm.make_dependent('pgm1', 'pgm2')

        print 'depends graph', cm.dep_graph
        print 'used by graph', cm.usedby_graph

        self.assertTrue(len(cm.dep_graph['pgm2']) == 0)
        self.assertTrue(len(cm.usedby_graph['pgm1']) == 0)

        self.assertTrue('pgm1' in cm.usedby_graph['pgm2'])
        self.assertTrue('pgm2' in cm.dep_graph['pgm1'])


class TestRemove(unittest.TestCase):
    def test_remove(self):
        cm = ComponentManager()
        cm.add_component('A')
        cm.add_component('B')
        cm.add_component('C')
        cm.add_component('D')
        cm.make_dependent('A', 'B')
        cm.make_dependent('B', 'C')
        cm.make_dependent('D', 'C')
        #cm.print_graph()

        cm.remove('A')

        cm.print_graph()

    def test_remove_cycle(self):
        cm = ComponentManager()
        cm.add_component('A')
        cm.add_component('B')
        cm.add_component('C')
        cm.add_component('D')
        cm.add_component('E')
        cm.make_dependent('A', 'B')
        cm.make_dependent('B', 'C')
        cm.make_dependent('C', 'D')
        cm.make_dependent('D', 'B')
        cm.make_dependent('E', 'D')
        cm.remove('A')
        cm.print_graph()

if __name__ == '__main__':
    unittest.main()
