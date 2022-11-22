class Course:
    
    def __init__(self):
        self.Fee()
        self.available_batches()
        
    def Fee(self):
        raise NotImplementedError
    
    def available_batcher(self):
        raise NotImplementedError
    
    def __repr__(self):
        return 'Fee: {0.fee} | Batches available: {0.batches}'.format(self)
    

class DSA(Course):
    
    def Fee(self):
        self.fee = 9000
    
    def available_batches(self):
        self.batches = 4
        
    def __str__(self):
        return "DSA"
        

class SDE(Course):
    
    def Fee(self):
        self.fee = 1000
    
    def available_batches(self):
        self.batches = 4
        
    def __str__(self):
        return "SDE"


class STL(Course):
    
    def Fee(self):
        self.fee = 1000
    
    def available_batches(self):
        self.batches = 4
        
    def __str__(self):
        return "STL"
    
    
class ComplexCourse:
    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)
    
    
class ComplexCourse(ComplexCourse):
    
    def Fee(self):
        self.fee = 9000

    def available_batches(self):
        self.batches = 6
        
def construct_course(cls):
    
    course = cls()
    course.Fee()
    course.available_batches()
    
    return course


if __name__ == '__main__':
    
    dsa = DSA()
    sde = SDE()
    stl = STL()
    
    complex_course = construct_course(ComplexCourse)
    # complex_course1 = construct_course(Course)
    print(complex_course)
    # print(complex_course1)