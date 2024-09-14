Class DecimalToBinary:
    def __init__():
        binary = findBinary(233, "")
    
    def findBinary(decimal, result){
        if decimal == 0:
            return result
        
        result = decimal % 2 + result
        return findBinary(decimal // 2, result)
    }
