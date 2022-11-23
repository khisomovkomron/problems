from abc import ABC, abstractmethod
import copy

"""
AbstractClass(ABC) - The interface that describes the clone() method.
Class(AbstractClass) - The Object/Product that implements the Prototype interface.
Client - The client application that uses and creates the ProtoType.
"""


class IProtoType(ABC):
    
    @staticmethod
    @abstractmethod
    def clone(mode):
        """A static interface for Prototype"""
        

class Document(IProtoType):
    
    def __init__(self, name, l):
        self.name = name
        self.list = l
        
    def clone(self, mode):
        if mode == 1:
            doc_list = self.list  # creates reference to initial object, modifies initial object
        if mode == 2:
            doc_list = self.list.copy()  #
        if mode == 3:
            doc_list = copy.deepcopy(self.list)  # make new object, does not modify initial object
            
        return type(self)(
            self.name,
            doc_list
        )
    
    def __str__(self):
        return f'{id(self)}\tname={self.name}\tlist={self.list}'
        
    
if __name__ == '__main__':
    
    ORIGINAL_DOC = Document('Original', [[1, 2, 3, 4], [5, 6, 7, 8]])
    print(ORIGINAL_DOC)
    print()

    # DOCUMENT_COPY_1 = ORIGINAL_DOC.clone(1)
    # DOCUMENT_COPY_1.name = 'COPY 1'
    # DOCUMENT_COPY_1.list[1][2] = 200
    # print(DOCUMENT_COPY_1)
    # print(ORIGINAL_DOC)
    # print('doc_list = self.list')
    # print()
    #
    #
    DOCUMENT_COPY_2 = ORIGINAL_DOC.clone(2)
    DOCUMENT_COPY_2.name = 'COPY 2'
    DOCUMENT_COPY_2.list[1][0] = '1234'
    print(DOCUMENT_COPY_2)
    print(ORIGINAL_DOC)
    print('doc_list = self.list.copy()')
    print()
    #
    #
    # DOCUMENT_COPY_3 = ORIGINAL_DOC.clone(3)
    # DOCUMENT_COPY_3.name = 'COPY 3'
    # DOCUMENT_COPY_3.list[1][0] = '1234'
    # print(DOCUMENT_COPY_3)
    # print(ORIGINAL_DOC)
    # print('doc_list = copy.deepcopy(self.list)')
    # print()
    #
    # DOCUMENT_COPY_4 = ORIGINAL_DOC.clone(3)
    # DOCUMENT_COPY_4.name = 'COPY 4'
    # DOCUMENT_COPY_4.list[1][0] = '5678'
    # print(DOCUMENT_COPY_4)
    # print(ORIGINAL_DOC)
    # print('doc_list = copy.deepcopy(self.list)')
    # print()
