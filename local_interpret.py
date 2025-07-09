
def local_interpret(prs: float) -> str:
    """
    Interpret the PRS score.
    """
    print("Your polygenic risk score is:" + str(prs))
    print()
    
    if prs > 1.2:
        print("Alzheimer's disease risk: HIGH RISK")
    elif prs > 0.8:
        print("Alzheimer's disease risk: MODERATE RISK")
    else:
        print("Alzheimer's disease risk: LOW RISK")
        
        
        
        
        