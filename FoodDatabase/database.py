#!usr/bin/python
# -*- coding: utf-8 -*-

class Database(object):
    _graph = {}
    _extract_status = {}
    _graphEdited = False
    _states = ["valid","invalid",
               "granularity_staged", "coverage_staged"]


    def __init__(self, graph=None):
        if graph is None or type(graph) is not str:
            raise TypeError("Provide a string as argument in Database ctor")
        self._graph = {"core": [graph]}


    def add_edge(self, child, parent):
        currentParent = self._graph[parent]
        if child not in currentParent:
            currentParent.append(child)


    def labels_edited(self, nodeEdited):
        for keyLabel, valuesLabel in self._extract.items():
            if keyLabel in self._extract_status:
                continue            
            currentStateLabel = self._states[0]
            for node in nodeEdited:
                parentId = node[1]
                if parentId in valuesLabel:
                    currentStateLabel = self._states[2]
                childsParentGraph = self._graph[parentId]
                sameValue = list(set(valuesLabel)&set(childsParentGraph))
                if len(sameValue) > 0:
                    currentStateLabel = self._states[3]
                    break
            self._extract_status[keyLabel] = currentStateLabel


    def add_nodes(self, nodes):            
        for node in nodes:
            newId = node[0]
            parentId = node[1]
            if parentId not in self._graph:
                self._graph[parentId] = [newId]                
            if parentId is not None:
                self.add_edge(newId, parentId)

        if self._graphEdited is True:
            self.labels_edited(nodes)
        else:
            self._graphEdited = True


    def add_extract(self, extractDict):
       self._extract = extractDict

       fusionList = []
       for nodes in self._graph.values():
        for node in nodes:
            fusionList.append(node)
        
       for keyLabel, valuesLabel in extractDict.items():
            labelUnmatching = [node for node in valuesLabel if node not in fusionList]
            if len(labelUnmatching) > 0:
                self._extract_status[keyLabel] = self._states[1]


    def get_extract_status(self):
        return self._extract_status
