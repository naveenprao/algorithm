import logging


class ComponentManager(object):
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.dep_graph = dict()
        self.usedby_graph = dict()

    def add_component(self, component):
        if component in self.dep_graph:
            return

        self.dep_graph[component] = set()
        self.usedby_graph[component] = set()

    def make_dependent(self, source, target):
        if source not in self.dep_graph or target not in self.dep_graph:
            return

        self.dep_graph[source].add(target)
        self.usedby_graph[target].add(source)

    def get_dependent_components(self, component):
        visited = set()

        def _get_dep_comp(comp):
            for dependency in self.dep_graph[comp]:
                if dependency not in visited:
                    visited.add(dependency)
                    _get_dep_comp(dependency)

        visited.add(component)
        _get_dep_comp(component)

        return visited

    def remove(self, component):
        if len(self.usedby_graph[component]) > 0:
            print 'Component used by : ', self.usedby_graph[component]
            print 'Try removing referencing components first!'
            return
        else:
            # find dependencies
            dependencies = self.get_dependent_components(component)
            can_delete = set()

            logging.debug('dep %s' % dependencies)

            # decide which dependency can be deleted based on usedBy info
            for dep_comp in dependencies:
                logging.debug('%s, %s, %s', dep_comp, self.usedby_graph[dep_comp], (self.usedby_graph[dep_comp] - dependencies))
                if len(self.usedby_graph[dep_comp] - dependencies) == 0:
                    can_delete.add(dep_comp)

            logging.debug('can_delete %s' % can_delete)

            for surviving_comp in (dependencies - can_delete):
                self.usedby_graph[surviving_comp] = self.usedby_graph[surviving_comp] - can_delete

            logging.debug('surviving_comp %s' % surviving_comp)

            # For all surviving components the dependents should be removed from can_delete
            for surviving_comp in (dependencies - can_delete):
                dependents = self.get_dependent_components(surviving_comp)
                can_delete = can_delete - dependents

            logging.debug('Final can delete %s'%can_delete)

            for deletable in can_delete:
                self.dep_graph.pop(deletable, None)
                self.usedby_graph.pop(deletable, None)

    def print_graph(self):
        logging.debug('dep-graph %s' % self.dep_graph)
        logging.debug('usedby-graph %s' % self.usedby_graph)
