# condition if 75 marks got than print distinction but without change reult function now create decore

def decore_distinct(result):
    def distinct(marks):
        result(marks)
        for m in marks:
            if m>=75:
                print("Distinct")
            
    return distinct

@decore_distinct
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("Fails")
            break
    else:
        print("Pass") 

marks=[50,40,85,95,75,60]   
result(marks)
# result=decore_distinct(result)
# result(marks)